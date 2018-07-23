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


class AnotherAccountTests(BaseTests):
    # Login with existing twitter account 
    @pytest.mark.first
    def test_login_new_twitter_account(self):
        try:
            accounthelper = AccountHelper()
            expectedDisplayName2=accounthelper.name
            expectedSoociiId2=accounthelper.name

            # Twitter Login button on Soocii
            self.sociushelper.click_twitter_login_button()
            self.syshelper.login_twitter_account(config.TWITTER_ACCOUNT, config.TWITTER_ACCOUNT_PWD)

            self.sociushelper.create_account(
                expectedDisplayName2,
                expectedSoociiId2,
                accounthelper.email)

            # confirm acquiring permission dialog
            self.sociushelper.click_confirm_recommended_celebrity()

            # confirm acquiring permission dialog
            self.sociushelper.click_require_permission_button()

            self.sociushelper.click_onboading_step()

            self.sociushelper.login_point()
            # expect seeing discover page
            self.assertTrue(self.sociushelper.is_discover())
            displayName, soociiId = self.sociushelper.get_personal_info()
            self.assertTrue(expectedDisplayName2==displayName,
                u"expect value {}, but return unexpected {}".format(expectedDisplayName2, displayName))
            self.assertTrue(expectedSoociiId2==soociiId,
                u"expect value {}, but return unexpected {}".format(expectedSoociiId2, soociiId))

            # switch to home and back to soocii
            self.syshelper.press_home_key()
            self.syshelper.start_soocii()
            displayName, soociiId = self.sociushelper.get_personal_info()
            self.assertTrue(expectedDisplayName2==displayName,
                u"expect value {}, but return unexpected {}".format(expectedDisplayName2, displayName))
            self.assertTrue(expectedSoociiId2==soociiId,
                u"expect value {}, but return unexpected {}".format(expectedSoociiId2, soociiId))

        except:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_twitter_createaccount")
            raise
        finally:
            # delete the account for next time
            self.sociushelper.click_delete_account_button()

    def test_login_new_google_account(self):
        try:
            expectedDisplayName=config.NEW_GOOGLE_ACCOUNT_NAME
            expectedSoociiId=config.NEW_GOOGLE_ACCOUNT_ID

            # google Login button on Soocii
            self.sociushelper.click_google_login_button()
            self.syshelper.login_google_account()

            # flow to create new account
            self.sociushelper.create_account(
                config.NEW_GOOGLE_ACCOUNT_NAME,
                config.NEW_GOOGLE_ACCOUNT_ID
                )
            self.sociushelper.click_confirm_recommended_celebrity()

            # confirm acquiring permission dialog
            self.sociushelper.click_require_permission_button()

            self.sociushelper.click_onboading_step()

            self.sociushelper.login_point()

            # expect seeing discover page
            self.assertTrue(self.sociushelper.is_discover())
            displayName, soociiId = self.sociushelper.get_personal_info()
            self.assertTrue(expectedDisplayName==displayName,
                u"expect value {}, but return unexpected {}".format(expectedDisplayName, displayName))
            self.assertTrue(expectedSoociiId==soociiId,
                u"expect value {}, but return unexpected {}".format(expectedSoociiId, soociiId))

            # switch to home and back to soocii
            self.syshelper.press_home_key()
            self.syshelper.start_soocii()
            displayName, soociiId = self.sociushelper.get_personal_info()
            self.assertTrue(expectedDisplayName==displayName,
                u"expect value {}, but return unexpected {}".format(expectedDisplayName, displayName))
            self.assertTrue(expectedSoociiId==soociiId,
                u"expect value {}, but return unexpected {}".format(expectedSoociiId, soociiId))
        except:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_login_new_google_account")
            raise
        finally:
            # delete the account for next time
            self.sociushelper.click_delete_account_button()

