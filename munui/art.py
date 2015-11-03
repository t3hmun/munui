#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Drawing box-art, text-ui layouts.

author : Manish Parekh (t3hmun at gmail dot com)
created: 06 August 2015
license: GPL3 (http://www.gnu.org/licenses/gpl-3.0.en.html)
"""

import shutil

# Standard boxart characters, available in most code pages.
btl = '┌'
bh = '─'
btr = '┐'
bbl = '└'
bbr = '┘'
bv = '│'
bml = '├'
bmr = '┤'

term_width, term_height = shutil.get_terminal_size()
default_width = term_width - 2
nl = '\n'


def top(width=default_width):
    """ The top box-art line. """
    return btl + bh * (width - 2) + btr


def bottom(width=default_width):
    """ The bottom box-art line. """
    return bbl + bh * (width - 2) + bbr


def middle(width=default_width):
    """ The middle box-art line. """
    return bml + bh * (width - 2) + bmr


def prompt(width=default_width):
    """ Bottom box-art line with a connector on the bottom left. """
    return bml + bh * (width - 2) + bbr


def msg(message, width=default_width, connect=None):
    """ An box with a message.

    connect:
    This refers to the postion of the box in relation to others.
    May be set to 'top', 'bottom', 'middle' or 'prompt' default None.
    Sets appropriate box art connecting to other parts.
    """
    message = wrap(message, width)
    if connect is None:
        box = top(width) + nl + message + nl + bottom(width)
    elif connect is "top":
        box = top(width) + nl + message
    elif connect is "bottom":
        box = middle(width) + nl + message + nl + bottom(width)
    elif connect is "middle":
        box = middle(width) + nl + message

    return box


def numlist(itemlist, width=default_width, truncate=None, connect=None,
            numspace='auto', start=1):
    """ A numbered list. No title or message. """

    if numspace is 'auto':
        # Calculate the space required for numbers.
        # Count the text len of the smallest and largest number.
        # Smallest may have negative sign therefore longer.
        longestNum = max(len(str(start)), len(str(start + len(itemlist))))
        numspace = longestNum + 2  # Add spaces for gutter and divider.

    if truncate is 'oneline':
        truncate = default_width

    i = start - 1
    entries = []
    for item in itemlist:
        i += 1
        if truncate is not None:
            # Left border + right border a space = 3, space needed to avoid
            #  triggering the wrapping algorithm.
            item = item[0:truncate - numspace - 3]
        numstr = (str(i) + ".").rjust(numspace)
        if len(numstr) > numspace:
            num = num[0:-numspace]  # Front tuncating.
        entries.append(numstr + item)

    text = '\n'.join(entries)
    return msg(text, width, connect=connect)


def wrap(text, width=default_width, left=bv, right=bv, gapchars=[' ', '-']):
    """ Wrap text between left and right within width. """
    text_len = len(text)
    line_len = width - len(left) - len(right)
    lines = []
    position = 0
    start = 0
    # Don't use a linebreak int he first half of the line to avoid splitting.
    min_line_len = line_len / 2
    while position < text_len:
        # Move positions forward
        start = position
        position += line_len
        if position > text_len:
            position = text_len
        furthest_position = position

        # A slice that is smaller or equal to the max line len.
        slice = text[start:position]
        # Search for existing newline, use it if it exists.
        newlinePos = slice.find("\n")
        if newlinePos >= 0:
            # The newline is not included.
            line = text[start:start + newlinePos]
            line = left + line.ljust(line_len) + right
            lines.append(line)
            # Continue after the newline (newlines are added via the list).
            position = start + newlinePos + 1
            continue

        # This triggers on the final line, after all of the newlines.
        if position is text_len:
            line = text[start:position]
            line = left + line.ljust(line_len) + right
            lines.append(line)
            break

        # Search backward for possible gap to insert newline.
        while text[position - 1] not in gapchars:
            position -= 1
            # No break point found so force a break at the max len line.
            if position <= start + min_line_len:
                position = furthest_position
                break

        line = text[start:position]
        line = left + line.ljust(line_len) + right
        lines.append(line)

    return '\n'.join(lines)
