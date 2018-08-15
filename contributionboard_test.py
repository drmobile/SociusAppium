# -*- coding: utf-8 -*-
#coding=utf-8
import os
import re
import sys
import pytest
import logging
import unittest
import subprocess
import time

from appium import webdriver

import config
from RAT import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

path1 = "./test_resources/."

# logger
logger = logging.getLogger()
logFormatter = logging.Formatter(
    '[%(asctime)-15s][%(filename)s][%(funcName)s#%(lineno)d] %(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(logFormatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

class contributionBoardTests(BaseTests):
    def test_contribution_Board(self):
        try:
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account(config.EMAIL_ACCOUNT, config.EMAIL_PWD)

            #self.sociushelper.click_require_permission_button()

            self.sociushelper.click_onboading_step()

            self.sociushelper.login_point()

            self.sociushelper.swipe_to_aboutme()

            self.sociushelper.click_contributionboard()

            self.sociushelper.wait_transition(2)

            self.sociushelper.swipe_left()

            self.sociushelper.wait_transition(2)

            self.sociushelper.swipe_left()

            self.sociushelper.wait_transition(2)

            self.sociushelper.leave_button()

            self.sociushelper.wait_transition(5)
        except:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_contribution_Board")
            raise    