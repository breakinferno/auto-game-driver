# -*- coding: utf-8 -*-
from ..schema import Task
from .pages.general import pages as general_pages
from .pages.boss import pages as boss_pages
from .pages.dreamless import pages as dreamless_pages
from .conditional_actions.boss import conditional_actions
from .pages.synthesis import pages as synthesis_pages
# 合并所有页面
boss_task = Task()
boss_task.pages = general_pages + boss_pages + dreamless_pages  # 合并通用页面和boss页面
boss_task.conditionalActions = conditional_actions  # 添加boss专属条件动作

synthesis_task = Task()
synthesis_task.pages = synthesis_pages  # 合成页面