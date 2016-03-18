#!/usr/bin/env python

import logging
import os
import subprocess
import sys
import time

# Set up logger
logger = logging.getLogger(sys.argv[0])
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
logger.addHandler(sh)

sleep_time = int(sys.argv[1])

logger.info('Running every %s seconds' % sleep_time)
logger.info('Launching command: %s' % ' '.join(sys.argv[2:]))

running = False
exited = False

# Loop until signal received
try:
    while True:
        running = True
		
        logger.debug('Launching command...')
        subprocess.call(sys.argv[2:])
        logger.debug('Command completed.')
		
        running = False
        if exited:
            break
        time.sleep(sleep_time)
except Exception, ex:
	logger.exception(ex)

def on_signal(self, signum, _frame):
    '''See signal callback registration: :py:func:`signal.signal`.
    This callback performs a clean shutdown when a SIGTERM or SIGINT is received.
    '''
    global exited
    logger.info('Received signal %i from frame: %s' % (signum, _frame))
    exited = True
    if not running:
        sys.exit()

signal.signal(signal.SIGTERM, on_signal)
signal.signal(signal.SIGINT, on_signal)
