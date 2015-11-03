#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Simple console based dialogs using box-art.

author : Manish Parekh (t3hmun at gmail dot com)
created: 07 August 2015
license: GPL3 (http://www.gnu.org/licenses/gpl-3.0.en.
html)
"""
from munui import *


def list_select_confirm(items, full_text=True, title=None, multi_select=False,
                        truncate=None, width=art.default_width, abort=None,
                        start=1):
    """ Prompt user to make selection and then ask for confirmation.

    Does not ask for confirmation on abort.
    """
    confirmed = False
    while not confirmed:
        res = list_select(items, title, multi_select, truncate, width, abort,
                          start)

        # Deal with abort response without confirming.
        if res is None:
            return None

        if type(res) is list:
            theydid = "You selected item(s): '" + \
                "', '".join([(items[x] if full_text else x + 1) for x in res])\
                + "'."
        else:
            if full_text:
                theydid = "You selected: '" + items[res] + "'."
            else:
                theydid - "You selected item: '" + res + "'."
        instructions = " Press c to confirm or r to retry."
        if abort:
            instructions += " Press '" + abort + "' to abort."

        valid_response = False
        error = None
        while not valid_response:
            print(art.msg(theydid, connect="top"))
            print(art.msg(instructions, connect="middle"))
            # This will only trigger if this loops on invalid input.
            if error:
                print(art.msg(error, connect="middle"))

            response = prompt(width)
            if response is 'c':
                return res
            elif response is 'r':
                return list_select_confirm(items, full_text, title,
                                           multi_select, truncate, width,
                                           abort, start)
            elif response is abort:
                return None
            else:
                error = "Ivalid response '" + response + "', try again."


def prompt(width):
    """ Display a prompt connected to the bottom of the previous block. """
    print(art.prompt(width))
    return input(art.bbl + ">>")


def list_select(
        items, title=None, multi_select=False, truncate=None,
        width=art.default_width, abort=None, start=1):
    """ Prompt the user to make a selection from a numbered list of items.

    If abort is enabled then None is returned on abort.
    If multiselect is enabled an array of indexes is returned.
    """

    lines = []
    if title:
        lines.append(art.msg(title, width, "top"))
        lines.append(art.numlist(items, width, truncate, "middle", start=start))
    else:
        lines.append(art.numlist(items, width, truncate, "top", start=start))

    if multi_select:
        instructions = "Select one or more items by typing the numbers" \
            " separated with spaces and then press enter."
    else:
        instructions = "Select one item by typing the number and pressing" \
            " enter."

    if abort:
        instructions += (" Type '" + abort + "' to abort")

    lines.append(art.msg(instructions, width, "middle"))
    dialog = '\n'.join(lines)

    # These are the numbers seen by the user, not indexes.
    valid = lambda x: x >= start and x < start + len(items)

    valid_response = False
    while not valid_response:
        print(dialog)
        response = prompt(width)
        if response is abort:
            return None
        error = None
        if multi_select:
            result = []
            try:
                for item in response.split():
                    num = int(item)  # This is potential ValueError
                    if not valid(num):
                        raise ValueError()
                    # Remove start to convert to index.
                    result.append(num - start)
                    valid_response = True
            except ValueError:
                error = "Invalid entry '" + item + "'. Try again."
                valid_response = False
        else:
            try:
                num = int(response)
                if not valid(num):
                    raise ValueError()
                result = num - 1  # Convert to index.
                valid_response = True
            except ValueError:
                error = "Invalid response '" + response + "'. Try again."
                valid_response = False
        if not valid_response:
            if not error:
                error = "No response, try again."
            errormsg = art.msg(error, connect="middle")
            dialog = '\n'.join(lines + [errormsg])

    return result
