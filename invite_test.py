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

class InviteTests(BaseTests):	
	def test_invite(self):
		try:
			#登入現有帳號測邀請好友功能
			self.sociushelper.click_login_by_email_link()
			self.sociushelper.login_account("invite@test.com", "test123")
			self.sociushelper.click_require_permission_button()
			self.sociushelper.click_onboading_step()
			
			self.sociushelper.login_point()

			self.assertTrue(self.sociushelper.check_invite(), "check_invite failed")
		except:
			self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
			self.syshelper.capture_screen("test_invite")
			raise




