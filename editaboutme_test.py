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

class EditaboutmeTests(BaseTests):
    def test_num_of_fans_follows(self):
        try:
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("carolinecheng28@gmail.com","soocii123")

            self.sociushelper.click_require_permission_button()

            self.sociushelper.swipe_to_aboutme()

            #check/get fans and follow of number in aboutme
            fans_a = self.sociushelper.get_number_with_id("tv_fans_count")
            follow_a = self.sociushelper.get_number_with_id("tv_following_count")
            self.sociushelper.swipe_to_friendlist()
          #  self.sociushelper.swipe_to_friendlist()



            self.assertTrue(self.sociushelper.check_num_of_fans_follow(fans_a))
            self.assertTrue(self.sociushelper.check_num_of_fans_follow(follow_a))
        except:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_num_of_fans_and_follow")
            raise        

    def test_edit_aboutme(self):
        try:
            # login for new
            accounthelper = AccountHelper()

            # Create new account button on Soocii
            self.sociushelper.click_create_new_account_using_email_button()

            # flow to create new account
            self.sociushelper.create_account(
                accounthelper.name,
                accounthelper.name,
                accounthelper.email,
                "password1234")

            # confirm to follow recommended celebrity
            #self.sociushelper.click_confirm_recommended_celebrity()

            self.sociushelper.click_confirm_recommended_celebrity()
            # confirm acquiring permission dialog
            self.sociushelper.click_require_permission_button()

            self.sociushelper.swipe_to_aboutme()

            self.sociushelper.edit_infophoto()

            self.sociushelper.edit_username_and_introduction()

            self.sociushelper.check_text("tv_display_name", "edit display")

            self.sociushelper.check_text("tv_about_me", "Hello welcome to my broatcast!!!")

        except Exception as e:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_edit_aboutme")
            raise
            






