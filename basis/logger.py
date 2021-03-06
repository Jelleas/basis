import colorama
colorama.init()

import logging
import textwrap
import contextlib

__all__ = ["enable", "disable", "emphasize", "highlight", "context"]


_DISABLED = True

def enable():
    global _DISABLED
    _DISABLED = False

def disable():
    global _DISABLED
    _DISABLED = True

def init():
    # create logger with 'spam_application'
    logger = logging.getLogger('basis')
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    file_handler = logging.FileHandler('basis.log')
    file_handler.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    formatter = logging.Formatter('%(message)s')
    console_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def _log(text):
    if _DISABLED:
        return
    text = f"{_cur_ctx()}|  {textwrap.indent(str(text), '  ' * _indentation)}"
    _logger.info(text)

def _indent():
    global _indentation
    _indentation += 1

def _dedent():
    global _indentation
    _indentation -= 1

def _push_ctx(ctx):
    _ctxs.append("{:14s}".format(ctx)[:14] + "  ")

def _pop_ctx():
    _ctxs.pop()

def _cur_ctx():
    return _ctxs[-1]

def emphasize(text):
    return f"\033[96m{text}\033[0m"

def highlight(text):
    return f"\033[92m{text}\033[0m"

@contextlib.contextmanager
def context(ctx=None):
    _push_ctx(ctx)
    _indent()
    try:
        yield _log
    finally:
        _dedent()
        _pop_ctx()

_ctxs = []
_indentation = -1
_logger = init()
