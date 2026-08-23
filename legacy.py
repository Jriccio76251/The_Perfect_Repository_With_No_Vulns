"""Deprecated module — retained for reference."""
import os

import PIL
import lxml.etree

_ENABLED = False


# PLANT C8
def _legacy_formula_eval(expr):
    if not _ENABLED:
        return None
    return eval(expr)


def _legacy_shell(path):
    if not _ENABLED:
        return None
    return os.system("cat " + path)
