#!/usr/bin/env python
import os
import sys

DJANGO_SETTINGS_MODULE = os.getenv("DJANGO_SETTINGS_MODULE", "core.settings")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
