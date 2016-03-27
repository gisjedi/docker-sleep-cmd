#!/usr/bin/env python

import logging
import logging.config
import os
import signal
import subprocess
import sys
import time

from logging_conf import CONFIG
logging.config.dictConfig(CONFIG)
logger = logging.getLogger(sys.argv[0])

sleep_time = float(os.getenv('SLEEP_SECONDS', 5))
command = sys.argv[1:]

logger.info('Running every %s seconds. Command: %s' % (sleep_time, ' '.join(command)))

running = False
exited = False


def on_signal(signum, frame):
    """This callback performs a clean shutdown when a SIGTERM or SIGINT is received.

    :param signum:
    :param frame:
    :return:
    """
    global exited
    logger.info('Received signal %i from frame: %s' % (signum, frame))

    exited = True
    if not running:
        sys.exit()

signal.signal(signal.SIGTERM, on_signal)
signal.signal(signal.SIGINT, on_signal)

# Loop until signal received
try:
    while True:
        running = True

        logger.debug('Launching command...')
        subprocess.Popen(sys.argv[1:])

        running = False
        if exited:
            break
        time.sleep(sleep_time)
except Exception, ex:
    logger.exception(ex)