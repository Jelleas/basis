import colorama
colorama.init()

import logging
import textwrap
import contextlib


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
    text = f"{_ctxs[-1]}|  {textwrap.indent(str(text), '  ' * _indentation)}"
    _logger.info(text)

def _indent():
    global _indentation
    _indentation += 1

def _dedent():
    global _indentation
    _indentation -= 1

def _set_ctx(ctx):
    _ctxs.append("{:12s}".format(ctx)[:12])

def emphasize(text):
    return f"\033[93m{text}\033[0m"

@contextlib.contextmanager
def context(ctx=None):
    _set_ctx(ctx)
    _indent()
    yield _log
    _dedent()
    _ctxs.pop()

_ctxs = []
_indentation = -1
_logger = init()
