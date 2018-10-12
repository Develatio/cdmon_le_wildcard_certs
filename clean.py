#!/usr/bin/env python3

from decouple import config
from cdmon_automator import CDMON

try:
    cdmon = CDMON()

    cdmon.login()

    cdmon.work_on("develat.io")

    cdmon.delete_record("TXT", "_acme-challenge")

    cdmon.terminate()
except Exception as ex:
    cdmon.terminate()
