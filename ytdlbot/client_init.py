#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - client_init.py
# 12/29/21 16:20
#

__author__ = "AXD <AXD@FPS>"

import os

from pyrogram import Client

from config import APP_HASH, APP_ID, PYRO_WORKERS, TOKEN


def create_app(session="ytdl", workers=PYRO_WORKERS):
    _app = Client(session, APP_ID, APP_HASH,
                  bot_token=TOKEN, workers=workers,
                  ipv6=os.getenv("ipv6", False),
                  # proxy={"hostname": "host.docker.internal", "port": 1080}
                  )

    return _app
