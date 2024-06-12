# -*- coding: utf-8 -*-
import time
from paddleocr import PaddleOCR
from multiprocessing import current_process
import numpy as np
from schema import OcrResult, Position
from config import ProcessConfig
import logging


ocrIns: PaddleOCR = None

if current_process().name == "task":
    logging.disable(logging.WARNING)  # 关闭WARNING日志的打印
    ocrIns = PaddleOCR(use_angle_cls=False, use_gpu=True, lang="ch",show_log=False)

last_time = time.time()


def ocr(img: np.ndarray) -> list[OcrResult]:
    global last_time
    diffTime = time.time() - last_time
    if ProcessConfig.OcrInterval > 0 and diffTime < ProcessConfig.OcrInterval:  # 限制OCR调用频率
        if wait_time := ProcessConfig.OcrInterval - diffTime > 0:
            time.sleep(wait_time)
    last_time = time.time()
    results = ocrIns.ocr(img)[0]
    if not results:
        return []
    res = []
    for result in results:
        text = result[1][0]
        position = result[0]
        x1, y1, x2, y2 = position[0][0], position[0][1], position[2][0], position[2][1]
        position = Position(x1=x1, y1=y1, x2=x2, y2=y2)
        confidence = result[1][1]
        res.append(OcrResult(text=text, position=position, confidence=confidence))
    return res
