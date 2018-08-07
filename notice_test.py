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

class NoticeTest(BaseTests):
    def test_notification_center(self):
        try:
            #測試通知中心by有通知
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("poi098@gmail.com", "poi098")
            #self.sociushelper.click_require_permission_button()
            self.sociushelper.click_onboading_step()

            try:
                self.sociushelper.login_point()
                self.sociushelper.swipe_discover()
            except:
                pass    
                
            self.sociushelper.click_notification_button()
            try:
                self.assertTrue(self.sociushelper.click_notification_detail())
                self.sociushelper.waitii()
                self.sociushelper.go_back()
                self.sociushelper.go_back()
            except:
                self.sociushelper.leave_button()
        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_notification_center")
            raise

    def test_blank_notification_center(self):
        try:
            #測試通知中心by無通知(創新帳號)
            accounthelper = AccountHelper()
            self.sociushelper.click_create_new_account_using_email_button()
            self.sociushelper.create_account(
                accounthelper.name,
                accounthelper.name,
                accounthelper.email,
                "password1234")
            self.sociushelper.click_confirm_recommended_celebrity()
            self.sociushelper.click_onboading_step()

            try:
                self.sociushelper.login_point()
                self.sociushelper.swipe_discover()
            except:
                pass    
                
            self.sociushelper.click_notification_button()
            try:
                self.assertTrue(self.sociushelper.click_notification_detail())
                self.sociushelper.go_back()
                self.sociushelper.go_back()
            except:
                self.sociushelper.leave_button()
        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_blank_notification_center")
            raise
        finally:
            self.sociushelper.click_delete_account_button()

    def test_push_notification(self):
        try:
            #測試推播通知設定
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("poi098@gmail.com", "poi098")
            self.sociushelper.click_require_permission_button()
            self.sociushelper.click_onboading_step()

            try:
                self.sociushelper.login_point()
                self.sociushelper.swipe_discover()
            except:
                pass

            self.sociushelper.click_hamburger_button()
            self.sociushelper.click_push_button()
            self.sociushelper.stop_push_button()
            self.sociushelper.start_push_button()
            self.sociushelper.leave_button()
        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_push_notification")
            raise

