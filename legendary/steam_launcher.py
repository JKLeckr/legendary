#!/usr/bin/env python3
# coding: utf-8

import os
from multiprocessing import freeze_support


def _disable_double_click_console_hold():
    if os.name != 'nt':
        return

    try:
        from legendary.lfs import windows_helpers
    except Exception:
        return

    windows_helpers.double_clicked = lambda: False


def main():
    freeze_support()
    _disable_double_click_console_hold()

    from legendary.cli import main as legendary_main

    return legendary_main()


if __name__ == '__main__':
    main()
