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

class PostsTests(BaseTests):
    def test_edit_posts(self):
        havefile()
        try:

            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("channing@gmail.com", "zxasqw123")

            self.sociushelper.click_require_permission_button()


            self.sociushelper.swipe_to_newsfeed()
            self.sociushelper.swipe_refresh()

            self.sociushelper.click_viedo_to_share()##click viedo button in about me,and share viedo

            self.sociushelper.swipe_to_aboutme()
            
            self.sociushelper.check_and_refresh_share_posts()
            self.sociushelper.swipe_loading()
            self.sociushelper.check_post_title("video from about me")
            
            self.sociushelper.check_post()

        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_edit_post")
            raise

    def test_firstposts(self):
        try:
            nofile()
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("channing@gmail.com", "zxasqw123")

            self.sociushelper.click_require_permission_button()


            self.sociushelper.swipe_to_newsfeed()
            self.sociushelper.swipe_refresh()

            self.sociushelper.new_local_video_post()



        except:
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_firstposts")
            raise

    def test_comments(self):
        try:
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("channing@gmail.com", "zxasqw123")

            self.sociushelper.click_require_permission_button()

            self.sociushelper.swipe_to_aboutme()
            self.sociushelper.swipe_loading()
            check_a = self.sociushelper.check_like_num(["like", u"個棒"]) # (a) to get like of number

            self.sociushelper.swipe_like()#click like
            check_b = self.sociushelper.check_like_num(["like", u"個棒"]) # (b) to get like of number
            self.assertTrue(check_b > check_a) #After click like_bt , compare (a) with (b) count whether +1
            self.sociushelper.swipe_like()#keep like
            self.sociushelper.swipe_and_send_message("this is qa message")#input message to share_EditText ,and click send button
            self.sociushelper.is_message("this is qa message")#if message visibility
            self.syshelper.press_back_key()
        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_comments")
            raise
        finally:
            pass

    def test_share_posts(self):
        try:
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("channing@gmail.com", "zxasqw123")
            self.sociushelper.click_require_permission_button()

            self.sociushelper.swipe_to_aboutme()
            self.sociushelper.swipe_loading()
            #self.sociushelper.swipe_posts()#click share button
            self.sociushelper.swpie_share_posts()#click share posts button
            self.sociushelper.swipe_share_posts_to_soocii()

            self.sociushelper.input_send_share_message("this is share post testing")#input message and click send button

            self.sociushelper.swipe_refresh()
            self.sociushelper.swipe_loading()
            self.assertTrue(self.sociushelper.check_share_posts())#make sure


        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_share_posts")
            raise
        finally:
            pass


    def test_upload_picture(self):
        try:

            nofile()#delete all file

            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("channing@gmail.com", "zxasqw123")

            self.sociushelper.click_require_permission_button()


            self.sociushelper.swipe_to_newsfeed()
            self.sociushelper.swipe_refresh()

            self.sociushelper.click_share_picture()#click image button in about me,and share photo

            self.sociushelper.check_and_refresh_share_posts()
            #come back to aboutme,to check share posts is exist (picture)
            
            self.sociushelper.check_post_title("upload img from local")

        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_upload_picture")
            raise
        finally:
            pass

    def test_check_and_share_record(self):

        try:
            nofile()#clear all file

            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("channing@gmail.com", "zxasqw123")
            self.sociushelper.click_require_permission_button()
            havefile()#put file to test case (photo and viedo)
            self.sociushelper.waitii()

            self.sociushelper.swipe_to_newsfeed()
            self.sociushelper.swipe_refresh()

            self.sociushelper.click_viedo_to_share()##click viedo button in about me,and share viedo

            self.sociushelper.check_and_refresh_share_posts()
            #come back to aboutme,to check share posts is exist (viedo)
            
            self.sociushelper.check_post_title("video from about me")

        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_check_and_share_record")
            raise
        finally:
            pass
    def test_share_posts_to_otherapp(self):
        try:
            self.sociushelper.click_login_by_email_link()
            self.sociushelper.login_account("channing@gmail.com", "zxasqw123")

            # confirm acquiring permission dialog
            self.sociushelper.click_require_permission_button()

            self.sociushelper.swipe_to_aboutme()
            self.sociushelper.swipe_loading()
            self.assertTrue(self.sociushelper.check_share_otherapp_posts())
        except :
            self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            self.syshelper.capture_screen("test_share_posts_to_otherapp")
            raise
