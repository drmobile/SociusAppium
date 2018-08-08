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

from lib.syshelper import SysHelper
from lib.sociushelper import SociusHelper
from lib.accounthelper import AccountHelper
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

#please run facebookaccount_test.py first!
class MissionsTests(BaseTests):
	
	def test_missions_of_aboutme(self):
		try:
			#登入現有帳號(kennyOppoT)測試
			self.sociushelper.click_login_by_email_link()
 			self.sociushelper.login_account("kenny@oppo.com", "333333")
 			self.sociushelper.click_require_permission_button()
			self.sociushelper.click_onboading_step()
			
			self.sociushelper.login_point()

			self.assertTrue(self.sociushelper.check_aboutme_coin(), "check_aboutme_coin failed")
			self.assertTrue(self.sociushelper.check_aboutme_gift(), "check_aboutme_gift failed")
			self.assertTrue(self.sociushelper.check_aboutme_missions(), "check_aboutme_mission failed")
		except:
			self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
			self.syshelper.capture_screen("test_missions_of_aboutme")
			raise
		finally:
			# dont delete this account
			self.sociushelper.click_logout_button()

	def test_missions_of_soociipoint(self):
		try:
			#創新帳號測試
			accounthelper = AccountHelper()
			self.sociushelper.click_create_new_account_using_email_button()
			self.sociushelper.create_account(
                accounthelper.name,
                accounthelper.name,
                accounthelper.email,
                "password1234")
			self.sociushelper.click_confirm_recommended_celebrity()
			#self.sociushelper.click_require_permission_button()
			self.sociushelper.click_onboading_step()
			self.sociushelper.login_point()
			self.assertTrue(self.sociushelper.check_menu_ad(), "check_menu_ad failed")
		except:
			self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
			self.syshelper.capture_screen("test_missions_of_soociipoint")
		finally:
			self.sociushelper.click_delete_account_button()


