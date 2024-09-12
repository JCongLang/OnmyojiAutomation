
# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import io
import sys
import traceback
from airtest.core.api import *

code = r"""if exists(Template(r"tpl1725872395192.png", record_pos=(0.004, 0.117), resolution=(1600, 900)), timeout = 5):
        finishTouch(screen_width, screen_height)"""
script_path = r"""C:\Users\LangJicong\AppData\Local\Temp\AirtestIDE\Scripts\untitled.air\untitled.py"""
if len("android://127.0.0.1:5037/127.0.0.1:7555?cap_method=ADBCAP&touch_method=MAXTOUCH&") > 0:
    connect_device("android://127.0.0.1:5037/127.0.0.1:7555?cap_method=ADBCAP&touch_method=MAXTOUCH&")

if script_path:
    if os.path.isfile(script_path):
        script_path = os.path.dirname(script_path)
    try:
        os.chdir(script_path)
    except:
        pass


def setup_io():
    sys.stdout = sys.__stdout__ = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8", line_buffering=True)
    sys.stderr = sys.__stderr__ = io.TextIOWrapper(
        sys.stderr.buffer, encoding="utf-8", line_buffering=True)
    

def my_exec(code, script_path, globals=None, locals=None, description='source string'):
    try:
        exec(code, globals, locals)
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args
        line_number = err.lineno
        print(traceback.format_exc())
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
        # print(ProjectManager.trans_script_to_html(traceback.format_exc(), script_path))
        print(traceback.format_exc(limit=-3))
    else:
        return ""


if sys.stdout.encoding and 'asc' in sys.stdout.encoding.lower():
    try:
        setup_io()
    except:
        pass

try:
    my_exec(code, script_path)
except:
    print(traceback.format_exc())
