#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgitb
import sys

cgitb.enable()
sys.path.insert(0, "../src")

from includes.enc_print import enc_print
from includes.css_js import catch_files

enc_print("Content-type: text/css; charset=utf-8")
enc_print("")

catch_files("./files", ".css", enc_print)
