#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Basic functionality testing scratch-pad. """
from munui.art import *

# When True the piping will be correct but the console output will not.
# Screen output will be correct when piped into cat.
#piped = True
piped = False
if piped:
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print(msg(
    "I need to write a long sentence to test out the wrapping. I need to write"
    " a long sbntence to test out the wrapping. I need to write a long "
    "sentence to test out the wrapping. I need to write a long sentence to "
    "test out the wrapping. I need to write a long sentence to test out the "
    "wrapping. I need to write a long sentence to test out the wrapping. "
    "Nowforasinglegiantblock"
    "withnospacessothaticanchackthatthesoaceslalalalala"
    "lalalalalalalathingworksyeah."))

print(msg("top", connect="top"))
print(msg("middle", connect="middle"))
print(msg("bottom", connect="bottom"))

print(numlist(["This choice.", "That choice.", "Yet another choise."]))
