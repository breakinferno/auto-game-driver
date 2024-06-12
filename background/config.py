# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field
import yaml
import os
from constant import task_config_path, process_config_path
from process import wait_exit

class ProcessConfig(BaseModel):
    WindowClass: str = Field("", title="窗口Class")
    WindowName: str = Field("", title="窗口名称")
    OcrInterval: float = Field(0.5, title="OCR间隔时间", ge=0)


class Step(BaseModel):
    Name: str=Field("stepName", title="操作名称")
    Content: str=Field("stepContent", title="操作文本")
    Image: str=Field("/", title="操作图片")
class Task(BaseModel):
    Name: str = Field("taskName", title="任务名称")
    Description: str = Field("taskDescription", title="任务详细描述")
    Steps: list[Step] = Field([], title="任务步骤")

class TaskConfig(BaseModel):
    TaskInterval: float = Field(0.1, title="任务间隔时间")
    Tasks: list[Task] = Field([], title="任务列表")



# 判断是否存在Window配置文件
if os.path.exists(process_config_path):
    with open(process_config_path, "r", encoding="utf-8") as f:
        process_config = ProcessConfig(**yaml.safe_load(f))
else:
    process_config = ProcessConfig()
    with open(process_config_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(process_config.dict(), f)

# 判断是否存在Tasks配置文件
if os.path.exists(task_config_path):
    with open(task_config_path, "r", encoding="utf-8") as f:
        task_config = TaskConfig(**yaml.safe_load(f))
else:
    task_config = TaskConfig()
    with open(task_config_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(task_config.dict(), f)

if len(task_config.Tasks) == 0:
    print("请在项目config目录下的tasks.yaml中添加Tasks")
    wait_exit()
