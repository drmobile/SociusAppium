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


class SearchTests(BaseTests):
    def test_search_game_user(self):
        try:
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account(config.EMAIL_ACCOUNT, config.EMAIL_PWD)

            self.sociushelper.click_require_permission_button()

            self.sociushelper.click_onboading_step()
            # click search
            self.sociushelper.check_search_button()
            self.assertTrue(self.sociushelper.check_game_tag())
            self.sociushelper.search_name("batt")
            self.assertTrue(self.sociushelper.check_tag_num())
            self.sociushelper.check_result_tag()
            self.assertTrue(self.sociushelper.check_result_game_tag())
            self.sociushelper.check_result_tag_share()
            self.sociushelper.check_search_user_button()
            self.assertTrue(self.sociushelper.check_search_username())

        except:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_search_game_user")
            raise
    def test_search_northrace(self):
        try:
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account(config.EMAIL_ACCOUNT, config.EMAIL_PWD)
            self.sociushelper.click_require_permission_button()

            self.sociushelper.click_onboading_step()
            self.sociushelper.check_search_button()
            self.sociushelper.search_name(u"北區聯賽")
            self.assertTrue(self.sociushelper.check_northrace())
        except:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_search_northrace")
            raise

