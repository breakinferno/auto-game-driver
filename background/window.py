# -*- coding: utf-8 -*-
import re
import win32gui
import sys
from ctypes import windll
from config import process_config
from process import wait_exit
from constant import root_path


def get_scale_factor():
    try:
        windll.shcore.SetProcessDpiAwareness(1)  # 设置进程的 DPI 感知
        scale_factor = windll.shcore.GetScaleFactorForDevice(
            0
        )  # 获取主显示器的缩放因子
        return scale_factor / 100  # 返回百分比形式的缩放因子
    except Exception as e:
        print("Error:", e)
        return None


hwnd = 0
width_ratio = 1.0
height_ratio = 1.0
real_w = 1920
real_h = 1080
w = 1920
h = 1080


def init_window():
    hwnd = win32gui.FindWindow(process_config.WindowClass, process_config.WindowName)
    if hwnd == 0:
        print("未找到游戏窗口")
        wait_exit()

    # Window
    left, top, right, bot = win32gui.GetClientRect(hwnd)
    w = right - left
    h = bot - top
    scale_factor = get_scale_factor()
    width_ratio = w / 1920 * scale_factor
    height_ratio = h / 1080 * scale_factor
    real_w = int(w * scale_factor)
    real_h = int(h * scale_factor)
    # 判断 root_path 中是否包含中文或特殊字符
    special_chars_pattern = r"[\u4e00-\u9fa5\!\@\#\$\%\^\&\*\(\)]"
    if bool(re.search(special_chars_pattern, root_path)):
        print("请将项目路径移动到纯英文路径下")
        wait_exit()