#!/usr/bin/env python3

import sys
from decouple import config
from cdmon_automator import CDMON

try:
    cdmon = CDMON()

    cdmon.login()

    cdmon.work_on("develat.io")

    cdmon.create_record("TXT", {
        "redirect_type": "custom",
        "subdomain": "_acme-challenge",
        "value": config("CERTBOT_VALIDATION", "Make sure to put a value here")
    })

    cdmon.terminate()
except Exception as ex:
    cdmon.terminate()
    sys.exit(ex)
