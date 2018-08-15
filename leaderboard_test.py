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

class LeaderBoardTests(BaseTests):
    def test_Leader_Board(self):
        try:
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account(config.EMAIL_ACCOUNT, config.EMAIL_PWD)

            self.sociushelper.click_require_permission_button()

            self.sociushelper.click_onboading_step()

            self.sociushelper.click_leaderboard()

            self.sociushelper.wait_transition(1)

            self.sociushelper.swipe_left()

            self.sociushelper.wait_transition(1)

            self.sociushelper.swipe_left() 

            self.sociushelper.wait_transition(1)

            if(not(self.sociushelper.is_empty_leaderboard())):
                self.sociushelper.click_button_with_id("iv_avatar_1st")

                self.sociushelper.wait_transition(1)

                self.sociushelper.click_button_with_id("navi_menu")

                self.sociushelper.wait_transition(1)

                self.sociushelper.click_button_with_id("follow_btn")

                #如果有出現 追蹤人數已達上限 把它點掉
                try:
                    self.sociushelper.wait_transition(1)
                    self.sociushelper.click_button_with_id("btn_confirm")
                except:
                    pass
                
                if(self.sociushelper.check_follow_btn()):
                    self.sociushelper.swipe_left()

                    self.sociushelper.wait_transition(1)

                    self.sociushelper.swipe_left()  

            self.sociushelper.click_button_with_id("navi_menu")

        except:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_Leader_Board")
            raise    
