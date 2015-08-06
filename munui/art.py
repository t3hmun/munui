""" Drawing box-art, text-gui layouts. """
import shutil

btl = '┌'
bh = '─'
btr = '┐'
bbl = '└'
bbr = '┘'
bv = '│'
bml = '├'
bmr = '┤'

term_width, term_height = shutil.get_terminal_size()
newline = '\n'


def top(width=term_width):
    """ The top box-art line. """
    return btl + bh * (width - 2) + btr


def bottom(width=term_width):
    """ The bottom box-art line. """
    return bbl + bh * (width - 2) + bbr


def middle(width=term_width):
    """ The middle box-art line. """
    return bml + bh * (width - 2) + bmr


def msg(message, width=term_width):
    """ An independent box with a message. """
    message = wrap(message, width)
    box = top(width) + message + bottom(width)
    return box


def wrap(text, width=term_width, left=bv, right=bv, gapchars=[' ', '-']):
    """ Wrap text between left and right within width. """
    total_len = len(text)
    line_len = width - len(left) - len(right)
    # If everything fits on a single line.
    if(total_len < line_len):
        return left + text.ljust(line_len) + right
    lines = []
    position = 0
    start = 0
    while position < total_len:
        start = position
        position += line_len
        if position > total_len:
            position = total_len
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
            position = newlinePos + 1
            continue

        # Search for possible gap to insert newline.
        while text[position - 1] not in gapchars:
            position -= 1
            # No break point find so force a break at the max len line.
            if position == start:
                position = furthest_position
                break

        line = text[start:position]
        line = left + line.ljust(line_len) + right
        lines.append(line)
    return ''.join(lines)
