# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 16:17
# @Author  : 饭盆里
# @File    : contest.py
# @Software: PyCharm
# @desc    :
import os
import signal
import subprocess

import pytest


@pytest.fixture(scope='class',autouse=True)
def record():
    cmd = "scrcpy --record tmp.mp4"
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid,signal.CTRL_C_EVENT)