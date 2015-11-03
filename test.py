#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Basic functionality testing scratch-pad. """
from munui.art import *
from munui.dialog import *

# When True the piping will be correct but the console output will not.
# Screen output will be correct when piped into cat.
#piped = True
piped = False
if piped:
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# This just tests the word wrapping in a box.
print(msg(
    "I need to write a long sentence to test out the wrapping. I need to write"
    " a long sbntence to test out the wrapping. I need to write a long "
    "sentence to test out the wrapping. I need to write a long sentence to "
    "test out the wrapping. I need to write a long sentence to test out the "
    "wrapping. I need to write a long sentence to test out the wrapping. "
    "Nowforasinglegiantblock"
    "withnospacessothaticanchackthatthesoaceslalalalala"
    "lalalalalalalathingworksyeah."))

# This just shows different blocks connecting together.
print(msg("top", connect="top"))
print(msg("middle", connect="middle"))
print(msg("bottom", connect="bottom"))


testlist = ['First option', 'Second Option', \
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARRRGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", \
'The third option was a testing thing-a-me-bobbin, and so is this.']

# This is just a numbered list.
print(numlist(testlist))

print(numlist(testlist, truncate='oneline', start=10))


# This is the first real feature demo.
# A dialog asking the user to selct from a list of options.
# The index(es) of the selected items is returned.
sel = list_select_confirm(
    ['one', 'two', 'three', 'four'], title="A lovely selection", abort='a',
    multi_select=True, start = 3)

print("Index(es) " + str(sel) + " was selected")
