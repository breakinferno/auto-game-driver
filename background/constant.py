# -*- coding: utf-8 -*-
import os

# Paths
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
process_config_path = os.path.join(root_path, "configs", "process.yaml")
task_config_path = os.path.join(root_path, "configs", "tasks.yaml")
task_config_folders_path = os.path.join(root_path, "configs", "tasks")
model_path = os.path.join(root_path, "models/yolo.onnx")
