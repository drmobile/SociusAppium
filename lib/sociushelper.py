
# -*- coding: utf-8 -*-
#coding=utf-8
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base import AppiumBaseHelper


class SociusHelper(unittest.TestCase, AppiumBaseHelper):
    def __init__(self, driver, platformName, platformVersion):
        AppiumBaseHelper.__init__(self, driver, platformName, platformVersion)

    def click_facebook_login_button(self):
        self.wait_transition(1)
        self.click_button_with_id("img_facebook_login")
        self.wait_transition(1)

    def click_twitter_login_button(self):
        self.click_button_with_id("img_twitter_login")
        self.wait_transition(3)

    def click_google_login_button(self):
        self.click_button_with_id("img_gplus_login")
        self.wait_transition(1)

    def click_create_new_account_using_email_button(self):
        self.click_button_with_id("other_login")
        self.wait_transition(1)
        self.click_textview_with_text([u"Email註冊","Email register"])
        self.wait_transition(1)

    def click_login_by_email_link(self):
        self.click_button_with_id("other_login")
        self.wait_transition(1)
        self.click_textview_with_text([u"Email登入","Email login"])
        self.wait_transition(1)

    def start_logger_activity(self):
        # The function does not work due to missing android:exported=”true” for the activity
        # self.driver.start_activity('me.soocii.socius.staging', 'me.soocii.socius.core.logger.LogCaptureActivity')
        self.click_button_with_id("navi_menu")
        self.wait_transition(1)
        el = self.wait.until(EC.presence_of_element_located((By.ID, "tv_app_version")))
        self.assertIsNotNone(el)
        for i in range(1, 11): el.click()
        self.driver.open_notifications()
        self.wait_transition(1)
        # Click on "Soocii Logger" or expand Soocii notification
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        self.swipe_right()#for oppo
        for el in items:
            self.logger.info(u'Check text view: {}'.format(el.text))
            if el.text == "Soocii Logger":
                self.logger.info(u'Found text view: {}'.format(el.text))
                el.click()
                self.wait_transition(1)
                return
        # Expand Soocii notification
        for el in items:
            if "Soocii" in el.text:
                el.click()
                self.wait_transition(1)
                # Click on "Soocii Logger"
                items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
                for el in items:
                    if el.text == "Soocii Logger":
                        el.click()
                        self.wait_transition(1)
                        return

    def waitii(self):
        self.wait_transition(3)

    def click_revoke_facebook(self):
        self.start_logger_activity()
        self.click_button_with_id("btn_revoke_fb")

    def click_delete_account_button(self):
        self.start_logger_activity()
        self.wait_transition(3)
        self.click_button_with_id("btn_delete_account")
        self.wait_transition(2)

    def click_delete_and_revoke_account_button(self):
        self.start_logger_activity()
        self.click_button_with_id("btn_delete_account")
        self.click_button_with_id("btn_revoke_fb")

    def click_logout_button(self):
        self.start_logger_activity()
        self.click_button_with_id("btn_logout")
        self.wait_transition(1)
        # logout confirmation
        self.click_button_with_text(["Logout", u"登出"])

    def click_require_permission_button(self):
        # only require for Android6+
        if self.isAndroid5():
            return
        self.wait_transition(2)
        self.click_textview_with_text([u"確認","Confirm"])
        self.wait_transition(10)
        # allow all system permissions
        if self.isAndroid7up():
            self.allow_system_permissions(3)
        else:
            self.allow_system_permissions(4)
        self.wait_transition(1)
      
    def click_require_photo_permission_button(self):
        if self.isAndroid5():
            return
        self.wait_transition(2)
        self.click_textview_with_text([u"確認","Confirm"])
        self.allow_system_permissions(1)
        self.wait_transition(1)

    def click_onlinevideocard(self):
        self.click_button_with_id("iv_screenshot")
        self.wait_transition(2)
        self.press_back_key()
        self.press_back_key()

    def click_videocard(self):
        self.swipe_tofind()
        self.wait_transition(1)
        self.click_button_with_id("post_right_top")
        self.wait_transition(2)
        self.press_back_key()
        self.press_back_key()

    def click_comment(self):
        self.click_textview_with_id("tv_comments")
        self.wait_transition(1.5)

    def skip_floating_ball_guide_mark(self):
        el = self.wait.until(EC.presence_of_element_located((By.ID, "permission_video")))
        self.assertIsNotNone(el)

        # tap on screen to skip
        center_x = self.window_size["width"] / 2
        center_y = self.window_size["height"] / 2
        self.driver.tap([(center_x, center_y)], 500)
        self.wait_transition(6)

    def login_account(self, email, pwd):
        self.send_text_with_id("email_value", email)
        self.logger.info('sent email: {}'.format(email))
        self.send_text_with_id("password_value", pwd)
        self.logger.info('sent password: {}'.format(pwd))
        self.click_button_with_id("login")
        # transition to next page
        self.wait_transition(6)

    def create_account(self,displayName, soociiId, email=None, pwd=None, confirmEmail=None, confirmPwd=None):
        self.Brosew_photo()
        self.wait_transition(2)
        self.send_text_with_id("display_name_value", displayName)
        self.logger.info('sent display name: {}'.format(displayName))
        self.send_text_with_id("soocii_id_value", soociiId)
        self.logger.info('sent soocii id: {}'.format(soociiId))
        self.click_textview_with_id("gender_value")
        self.wait_transition(1)
        self.click_textview_with_text([u"男","Male"])
        # email_value
        if email is not None:
            self.send_text_with_id("email_value", email)
            #self.send_text_with_id("email_confirm_value", email if confirmEmail is None else confirmEmail)
            self.logger.info('sent email: {}'.format(email))
        # password_value
        if pwd is not None:
            self.send_text_with_id("password_value", pwd)
            #self.send_text_with_id("password_confirm_value", pwd if confirmPwd is None else confirmPwd)
            self.logger.info('sent password: {}'.format(pwd))
        self.click_button_with_id("register")
        # transition to next page
        self.wait_transition(5)
    def Brosew_photo(self):
        self.click_button_with_id("avatar")
        self.wait_transition(2)
        self.click_textview_with_text([u"選擇照片","Browse photo"])
        self.wait_transition(1)
        self.click_require_photo_permission_button()

        if self.is_album()==False : #check whether in the album
            self.click_button_with_id("avatar")
            self.wait_transition(2)
            self.click_textview_with_text([u"選擇照片","Browse photo"])
            self.wait_transition(1)


        self.wait_transition(2)
        photofold = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RelativeLayout")))
        photofold[0].click()

        self.wait_transition(1)
        if self.isAndroid5():
            photobtn = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.view.View")))
            photobtn[1].click()

        else:
            try:

                photobtn = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.view.ViewGroup")))
                photobtn[0].click()
                self.assertTrue(is_edit_photo_page())
            except:
                photobtn[1].click()

        self.wait_transition(2)
        self.click_textview_with_id("action_next")

    def Take_photo(self):
        self.click_button_with_id("avatar")
        self.wait_transition(2)
        self.click_textview_with_text([u"拍攝照片","Take photo"])
        self.wait_transition(2)
        self.click_require_photo_permission_button()
        self.wait_transition(2)
        self.click_camera_shot()
        self.wait_transition(3)
        self.click_next()
        self.wait_transition(1)
        self.click_textview_with_id("action_next")
        self.wait_transition(1)

        self.wait_transition(2)
    def add_followers(self):
        self.wait_transition(3)
        self.click_button_with_id("add_follow_confirm")
        self.wait_transition(5)
        self.click_button_with_id("add_follow_confirm")
        # transition to next page
        self.wait_transition(1)
    def add_followers_email(self):
        self.wait_transition(3)
        self.click_button_with_id("add_follow_confirm")
        # transition to next page
        self.wait_transition(1)
    def __visibility_of_textview(self, tt):
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            if el.text in tt:
                return True
        return False

    def __visibility_of_button(self, id):
        item = self.wait.until(EC.presence_of_element_located((By.ID,id)))
        if item is None:
            return False
        else: 
            return True

    def is_message(self,tt):# today
        self.wait_transition(2)
        self.click_button_with_id("tv_comments")
        check = self.wait.until(EC.presence_of_all_elements_located((By.ID,"tv_comment_msg")))
        cname=check[len(check)-1].text
        cname.index(tt)

    def is_album(self):
        return self.__visibility_of_textview(["Select photo", u"選取相片"])

    def is_first_contact(self):
        return self.__visibility_of_textview(["chat",u"開始對話"])

    def is_discover(self):
        return self.__visibility_of_textview(["Discovery", u"探索"])

    def is_newsfeed(self):
        return self.__visibility_of_textview(["Newsfeed", u"即時動態"])

    def is_aboutme(self):
        return self.__visibility_of_textview(["Me", u"關於我"])

    def is_FAQ(self):
        return self.__visibility_of_textview(["FAQ", u"常見問題"])

    def is_Contact(self):
        return self.__visibility_of_textview(["Contact", u"聯絡我們"])

    def is_viedo_like_comment_share(self):
        return self.__visibility_of_textview(["like", u"個棒"])

    def is_edit_video_page(self):
        return self.__visibility_of_textview(["Edit video", u"編輯影片"])

    def is_edit_photo_page(self):
        return self.__visibility_of_textview(["Next", u"下一步"])

    def is_sharing(self):

        try:
            if self.__visibility_of_button("button2"):  #for oppo share 
                return True
        except:
            if self.__visibility_of_textview(u"選擇你要分享的App"):
                return True


    def is_faqwebview(self):
        wv=self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"android.webkit.WebView")))
        if wv is None:
            return False
        return True

    def swipe_makesure(self):
        self.wait_transition(2)
        self.click_button_with_id("add_follow_confirm")
        self.wait_transition(1)


    def swipe_picture(self):
        self.click_textview_with_text(["Image",u"圖片"])
        self.wait_transition(1)

    def swpie_share_posts(self):
        self.swipe_tofind()
        self.click_textview_with_id("tv_shares")
        self.wait_transition(1)

    def swipe_share_posts_to_soocii(self):
        self.click_button_with_id("menu_share_to_soocii")
        self.wait_transition(1)

    def swipe_share_posts_to_otherapp(self):
        self.click_button_with_id("menu_share_to_other")
        self.wait_transition(1)

    def swipe_discover(self):
        self.wait_transition(2)
        self.click_button_with_id("tv_discovery")
        self.wait_transition(1)
        return

    def swipe_to_newsfeed(self):
        self.wait_transition(2)
        self.click_button_with_id("tv_feed")
        return
    def swipe_to_find_friend(self):
        self.wait_transition(5)
        self.click_button_with_id("navi_menu")
        self.wait_transition(2)
        self.click_textview_with_text(u"尋找朋友")
        self.wait_transition(1)

    def swipe_to_friendlist(self):
        self.wait_transition(1)
        self.swipe_to_aboutme()
        self.wait_transition(3)
        self.click_button_with_id("tv_following_count")
        self.wait_transition(0.5)

    def swipe_to_aboutme(self):
        self.wait_transition(2)
        self.click_textview_with_id("icon_profile")
        self.wait_transition(2)

    def swipe_to_support(self):
        self.click_button_with_id("navi_menu")
        self.wait_transition(2)
        self.click_textview_with_text(u"客服姐姐")
        self.wait_transition(2)

    def swipe_to_fans(self):
        self.wait_transition(2)
        self.click_textview_with_text([u"粉絲","Follower"])

    def swipe_to_suggest(self):
        self.wait_transition(2)
        self.click_textview_with_text(["Suggest",u"用戶推薦"])

    def swipe_to_SearchId(self):
        self.press_back_key()
        self.wait_transition(2)
        self.click_button_with_id("iv_search_icon")
        self.wait_transition(2)
        self.click_textview_with_text(u"用戶")
    def swipe_to_faq(self):
        self.wait_transition(2)
        self.click_textview_with_id("rl_faq")

    def swipe_to_contact(self):
        self.wait_transition(2)
        self.click_textview_with_id("rl_contact_us")

    def swipe_refresh(self):
        self.wait_transition(2.5)
        self.swipe_down(350)

    def swipe_loading(self):
        self.wait_transition(2)
        self.swipe_up(650)


    def swipe_post_sandwish(self):
        self.wait_transition(2)
        self.click_button_with_id("iv_more")

    def swipe_post_edit(self):
        self.wait_transition(2)
        self.click_button_with_id("menu_edit")

    def swipe_choose_video(self):
        self.click_button_with_id("iv_action_icon")
        self.wait_transition(2)
        self.click_textview_with_text([u"影音","Video"])

    def swipe_edit(self):
        left_x = self.window_size["width"] * 0.06
        right_x = self.window_size["width"] * 0.5
        center_y = self.window_size["height"] * 0.85
        self.driver.swipe(start_x=left_x, start_y=center_y, end_x=right_x, end_y=center_y, duration=500)
        self.wait_transition(1)

    def swipe_edit_back(self):
        left_x = self.window_size["width"] * 0.06
        right_x = self.window_size["width"] * 0.5
        center_y = self.window_size["height"] * 0.9
        self.driver.swipe(start_x=right_x, start_y=center_y, end_x=left_x, end_y=center_y, duration=350)
        self.wait_transition(1)

    def edit_cover(self):
        left_x = self.window_size["width"] * 0.06
        right_x = self.window_size["width"] * 0.5
        center_y = self.window_size["height"] * 0.9
        self.driver.swipe(start_x=right_x, start_y=center_y, end_x=left_x, end_y=center_y, duration=350)
        self.wait_transition(0.5)



    def swipe_posts(self):
        self.wait_transition(2.5)
        try:
            posts_bt = self.wait.until(EC.presence_of_element_located((By.ID,"iv_thumbnail")))
        except :
            posts_bt = self.wait.until(EC.presence_of_element_located((By.ID,"iv_screenshot")))
        finally:
            posts_bt.click()#if first post is iv_thumbnail(viedo) or iv_screenshot (photo) ,to click

        self.wait_transition(1)

    def swipe_tofind(self):
        self.wait_transition(2)
        self.swipe_up(250)

    def swipe_tofind_slow(self):
        self.wait_transition(2)
        self.swipe_up(1000)

    def swipe_like(self):
        self.wait_transition(1)
        self.click_button_with_id("iv_like")
        self.wait_transition(1)


    def swipe_and_send_message(self,text):
        self.click_button_with_id("tv_comments")
        self.wait_transition(1)
        self.send_text_with_id("message_edit_text",text)
        self.wait_transition(1.5)
        self.click_button_with_id("outbox")
        self.wait_transition(1.5)



    def swipe_newsfeed_video(self):
        video_bt = self.wait.until(EC.presence_of_all_elements_located((By.ID,"iv_video")))
        if video_bt is None:
            return False
        video_bt[0].click()
        self.wait_transition(0.5)
        self.click_textview_with_text(u"編輯")
        self.wait_transition(2)

    def swipe_videounit(self):
        self.wait_transition(2)
        self.click_button_with_id("svv_preview")

    def swipe_to_msg(self):
        self.wait_transition(2)
        self.click_button_with_id("tv_comments")

    def swipe_share_posts_to_otherapp(self):
        self.click_button_with_id("menu_share_to_other")
        self.wait_transition(1)

    def swipe_fans_list_photo_image_view(self):
        fansbt = self.wait.until(EC.presence_of_element_located((By.ID,"fans_list_photo_image_view")))
        fansbt.click()
        self.wait_transition(1.5)

    def get_newsfeed_info(self):
        self.swipe_to_newsfeed()
        feedcard = self.wait.until(EC.presence_of_all_elements_located((By.ID,"ll_post_card")))
        if feedcard is None:
            return False
        else:
            return True

    def get_personal_info(self):
        self.swipe_to_aboutme()
        #self.click_button_with_id("tv_about_me_more")
        displayName = self.get_text_with_id("tv_display_name")
        soociiId = self.get_text_with_id("tv_soocii_id")
        # go back to main page

        return displayName, soociiId.split('S.')[1]

    def get_fanslist_info(self):
        self.swipe_to_friendlist()
        self.wait_transition(2)
        fans_video = self.wait.until(EC.presence_of_all_elements_located((By.ID, "fans_list_displayname_text")))
        if fans_video is None:
         return False
        else:
            return True

    def get_idsearch(self,text):
        self.send_text_with_id("search_field",text)
        self.wait_transition(1.5)
        self.click_textview_with_text(text)
        self.wait_transition(1)

    def go_back(self):
        self.press_back_key()
        self.wait_transition(1.5)

    def get_videocard(self):
        videocard=self.wait.until(EC.presence_of_element_located((By.ID,"iv_screenshot")))
        if videocard is None:
            return False
        else:
            return True

    def get_number_with_id(self,ID):
        self.wait_transition(1)
        return self.get_text_with_id(ID)

    def check_num_of_fans_follow(self,num):
        items = self.wait.until(EC.presence_of_all_elements_located((By.ID,"tab_text")))
        for text in items:
            if num in text.text:
                return True
        return False

    def check_share_otherapp_posts(self):
        self.swpie_share_posts()
        self.swipe_share_posts_to_otherapp()
        if self.is_sharing()==True:
            self.press_back_key()
            return True
        else:
            return False


    def check_share_posts(self):
        self.click_textview_with_text("this is share post testing")
        return True

    def check_and_refresh_share_posts(self):
        for x in range(3):
            self.swipe_refresh()
            self.wait_transition(3)



    def check_like_num(self,text):
        check_like_tv = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"android.widget.TextView")))
        for items in check_like_tv:
            if text[0] in items.text:
                return items.text.split(" ")[0]
            elif text[1] in items.text:
                return items.text.split(" ")[0]


    def check_aboutme(self,exdisplayname):
        self.swipe_to_aboutme()
        self.wait_transition(4)
        displayName = self.get_text_with_id("tv_display_name")
        if exdisplayname in displayName:
            return True
        else:
            return False
    def check_support(self): 
        self.swipe_to_support()
        self.wait_transition(5)
        supportname = self.get_text_with_id("tv_display_name")
        #if "Support" in supportname:  can't find "Support" 
        if True:
            self.wait_transition(1)
            self.press_back_key()
            self.press_back_key()
            return True
        else:
            self.press_back_key()
            self.press_back_key()
            return False

       


    def check_suggest(self):
        self.swipe_to_suggest()
        suggestbutton =self.wait.until(EC.presence_of_all_elements_located((By.ID,"facebook_invite")))
        if suggestbutton is None:
            return False
        else:
            return True

    def check_game_tag(self):
        tag =self.wait.until(EC.presence_of_all_elements_located((By.ID,"tag")))
        if tag is None:
            return False
        else:
            return True

    def check_tag_num(self):
        tag =self.wait.until(EC.presence_of_all_elements_located((By.ID,"tag_name")))
        if len(tag) <5:
            return False
        else:
            return True

    def check_result_game_tag(self):
        tag =self.wait.until(EC.presence_of_all_elements_located((By.ID,"iv_thumbnail")))
        if tag is None:
            return False
        else:
            return True

    def check_hashtag(self):

        items = self.wait.until(EC.presence_of_all_elements_located((By.ID,"text")))
        d=[]
        for ii in range(1,3):

            for el in items:
                elname=el.text
                if el.text not in d:
                    d.append(el.text)
                    el.click()

                    self.wait_transition(2.5)
                    try:
                        videonum=self.wait.until(EC.presence_of_all_elements_located((By.ID,"iv_thumbnail")))
                        vtag=self.wait.until(EC.presence_of_all_elements_located((By.ID,"tv_tag")))
                    except:
                        videonum=self.wait.until(EC.presence_of_all_elements_located((By.ID,"iv_screenshot")))
                        vtag=self.wait.until(EC.presence_of_all_elements_located((By.ID,"tv_tag")))

                    if len(videonum)<4:
                        return False
                    else:
                        for al in vtag:
                            if al.text not in elname:
                                return False

                    self.wait_transition(2.5)
                    self.press_back_key()
                    self.wait_transition(2.5)
            self.swipe_hash()
            self.wait_transition(2.5)

            items = self.wait.until(EC.presence_of_all_elements_located((By.ID,"text")))
            if str(d[len(d)-1]) == items[len(items)-1].text:
                return True

    def check_section(self):
        self.click_button_with_id("tv_call_to_action")
        self.wait_transition(2)
        section = self.wait.until(EC.presence_of_all_elements_located((By.ID,"rl_post_card")))
        if section is None:
            return False
        else:
            return True

    def check_search_username(self):
        name =self.wait.until(EC.presence_of_all_elements_located((By.ID,"soocii_id")))
        if name is None:
            return False
        else:
            return True
    def check_northrace(self):
        self.click_textview_with_text(u"北區聯賽")
        tag =self.wait.until(EC.presence_of_all_elements_located((By.ID,"iv_thumbnail")))
        if tag is None:
            return False
        else:
            return True

    def check_zendesk(self):
        self.assertTrue(self.is_FAQ())
        self.assertTrue(self.is_Contact())

    def check_faq(self):
        self.swipe_to_faq()
        self.wait_transition(4)
        self.assertTrue(self.is_faqwebview())
        self.wait_transition(2)
        self.press_back_key()

    def check_contact(self,text):
        self.swipe_to_contact()
        #self.click_button_with_text(u"開始對話")
        self.click_button_with_id("request_list_empty_start_conversation")
        self.send_text_with_text_no_clear(u"留下訊息","test")
        self.wait_transition(1.5)
        self.click_textview_with_id("message_composer_send_btn")
        self.wait_transition(1.5)
        self.press_back_key()

    def check_video_and_photo_icon(self):
        vpicons=self.wait.until(EC.presence_of_all_elements_located((By.ID,"tv_action")))
        keyw=[u"影音","Viedo",u"圖片","Image"]
        for vpicon in vpicons:
            if vpicon.text in keyw:

                return True
        return False

    def check_video_unit(self):
        self.swipe_videounit()
        self.wait_transition(1)
        vc=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"android.view.View")))
        if vc is None:
            return False
        return  True

    def click_choose_album(self):
        self.click_textview_with_text([u"相簿","Photos"])

    def click_alwaysbutton(self):
        self.click_button_with_id("button_always")

    def click_confirm_recommended_celebrity(self):
        # wait for recommended list is loaded
        self.wait_transition(8)

        self.click_button_with_id("add_follow_confirm")
        self.wait_transition(3)

    def click_camera_floatball(self):
        self.wait_transition(7)
        #dp=px*160/dpi
        #px=dp*dpi/160
        center_x = self.window_size["width"]
        if center_x == 720 : self.driver.tap([(45, 650)], 500)
        elif center_x == 1080 : self.driver.tap([(50, 980)], 500)
        else : self.driver.tap([(100, 1300)], 500)

    def click_camera_shot(self):
        self.wait_transition(2)
        center_x=self.window_size["width"]*0.5
        center_y=self.window_size["height"]*0.9
        self.driver.tap([(center_x,center_y)],500)

    def click_next(self):
        self.wait_transition(2)
        center_x=self.window_size["width"]*0.8
        center_y=self.window_size["height"]*0.9
        self.driver.tap([(center_x,center_y)],500)

    def click_open_fab_button(self):
        self.click_button_with_id("fab_live")
        self.wait_transition(2)

    def click_viedo_to_share(self):#today
        self.swipe_newsfeed_video()#click video

        self.click_button_with_id("btn_trim_complete")
        self.wait_transition(1)
        self.click_button_with_id("btn_trim_complete")
        self.wait_transition(1)#click next button x2

        self.send_text_with_id("upload_edittext","video from about me")#posts message
        self.wait_transition(1.5)

        self.click_textview_with_id("tv_share")#click share button
        self.wait_transition(1.5)


    def click_searchid(self,text):
        self.get_idsearch(text)
        self.click_textview_with_text(u"搜尋")
        self.click_button_with_id("display_name")
        self.wait_transition(2)

    def click_video_pause(self):
        self.wait_transition(2)
        self.click_button_with_id("exo_pause")

    def click_accept(self):
        self.wait_transition(2)
        self.click_button_with_id("btn_accept")


    def choice_game(self):
        self.click_textview_with_text(["Snake Off","Snake Off"])
        self.wait_transition(1)

    def setting_live(self):
        self.click_button_with_id("ib_broadcast_icon_camera_switch")
        self.wait_transition(3)
        self.click_button_with_id("btn_go_live")
        self.wait_transition(20)

    def broadcast(self,message):
        self.click_button_with_id("iv_menu_icon_chat")
        self.wait_transition(1)
        self.click_button_with_id("messageEditText")
        self.wait_transition(1)
        self.send_text_with_id("messageEditText", message)
        self.logger.info('sent message: {}'.format(message))
        self.wait_transition(5)
        self.click_button_with_id("sendButton")
        self.wait_transition(2)

    def change_camera(self):
        self.click_button_with_id("iv_menu_icon_camera")
        self.wait_transition(10)

    def stop_live(self):
        self.click_button_with_id("iv_menu_icon_stop")
        self.wait_transition(0.1)
        self.click_button_with_id("iv_menu_icon_stop")
        self.wait_transition(5)

    def go_to_post(self):
        self.click_button_with_id("tv_go")

    def share_live_record(self, upload,x):
        #self.click_button_with_id("tv_go")
        self.wait_transition(1)
        self.click_button_with_id("upload_edittext")
        self.wait_transition(1)
        self.send_text_with_id("upload_edittext", upload+str(x+1))
        self.logger.info('sent upload: {}'.format(upload+str(x+1)))
        self.wait_transition(3)
        self.click_button_with_id("tv_share")
        self.wait_transition(15)

    def back_soocii(self):
        self.click_button_with_id("iv_menu_icon_back")
        self.wait_transition(1)

    def refresh_aboutme(self):
        self.swipe_down(350)
        self.wait_transition(3)

    def check_single_posts(self):
        postview=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"android.view.View")))
        self.wait_transition(0.5)
        if postview is None:
            return False
        return True

    def check_post_title(self,tt):
        #check title
        postmsg=self.wait.until(EC.presence_of_element_located((By.ID,"tv_msg")))
        posttitle=postmsg.text
        if posttitle==tt:
            return True
        else :
            return False
        self.wait_transition(2)

    def check_post(self):
        self.wait_transition(1)
        #click sandwish button
        self.swipe_post_sandwish()
        self.wait_transition(1)
        #click edit button
        self.swipe_post_edit()
        self.wait_transition(1)
        #edit
        self.send_text_with_id("upload_edittext","edit post")
        self.wait_transition(1)
        #click confirm
        self.click_button_with_id("tv_share")
        self.wait_transition(2)
        self.check_post_title("edit post")

    def choose_video(self):
        #choose folder
        photofolder=self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"android.widget.RelativeLayout")))
        try:
            photofolder[0].click()
        except:
            photofolder[3].click()
        self.wait_transition(2)
        #choose video
        if self.isAndroid5():
            try:
                avideo=self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"android.view.View")))
                avideo[0].click()
                self.wait_transition(2)
                self.assertTrue(self.is_edit_video_page())
            except:
                avideo[1].click()
        else:
            try:
                avideo=self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"android.view.ViewGroup")))
                avideo[0].click()
                self.wait_transition(1)
                self.assertTrue(self.is_edit_video_page())
            except:
                avideo[1].click()

        self.wait_transition(2)

    def new_local_video_post(self):
        self.wait_transition(3)
        #add local video
        self.swipe_choose_video()
        self.wait_transition(2)
        try:
            #check choose google album
            self.assertFalse(self.click_choose_album())
        except:
            #if don't have the button
            self.click_alwaysbutton()
        else:
            #if have the button,do not thing
            pass

        self.choose_video()
        #click next*2
        self.click_button_with_id("btn_trim_complete")
        self.wait_transition(1)
        self.click_button_with_id("btn_trim_complete")
        self.wait_transition(2)
        #keyin title
        self.send_text_with_id("upload_edittext","upload video from local")
        self.click_textview_with_id("tv_share")
        self.wait_transition(10)
        self.swipe_refresh()
        #check title
        self.assertTrue(self.check_post_title("upload video from local"))

    def input_send_share_message(self,text):
        self.send_text_with_id("upload_edittext",text)

        self.wait_transition(1.5)
        self.click_textview_with_id("action_share")
        self.wait_transition(2)
        self.press_back_key()
        self.wait_transition(1)

    def click_accept(self):
        self.click_button_with_id("btn_accept")
    def click_share_picture(self):
        self.swipe_picture()

        select_Album_bt = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"android.widget.RelativeLayout")))


        select_Album_bt[1].click()#select album and click
        self.wait_transition(1.5)

        if self.isAndroid5():
            select_picture_bt = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"android.view.View")))
        else:
            select_picture_bt = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"android.view.ViewGroup")))
        #have a bug
        select_picture_bt[0].click()#select picture and click
        self.wait_transition(1.5)

        self.click_textview_with_id("action_next")
        self.wait_transition(1.5)

        self.send_text_with_id("upload_edittext","upload img from local")#posts message
        self.wait_transition(1.5)

        self.click_textview_with_id("tv_share")#click share button
        self.wait_transition(1.5)

    def to_record(self):
        self.press_back_key()
        self.wait_transition(1)
        self.press_back_key()
        self.wait_transition(1)
        self.choice_game()
        self.wait_transition(5)
        self.click_camera_floatball()
        self.wait_transition(1.5)
        start_bt = self.wait.until(EC.presence_of_element_located(By.ID,"iv_menu_icon_record"))
        start_bt.click()
        self.wait_transition(10)
        self.click_camera_floatball()
        stop_bt = self.wait.until(EC.presence_of_element_located(By.ID,"iv_menu_icon_stop"))
        stop_bt.click()
        self.wait_transition(1.5)
        back_bt = self.wait.until(EC.presence_of_element_located(By.ID,"iv_menu_icon_back"))
        back_bt.click()
        self.wait_transition(3.5)

    def edit_live_record(self):
        x = self.window_size["width"] * 0.8
        y = self.window_size["height"] * 0.15
        self.swipe_edit()
        self.swipe_edit_back()
        self.wait_transition(2)
        self.driver.tap([(x,y)],500)
        self.wait_transition(2)
        self.edit_cover()
        self.wait_transition(3)


    def edit_next(self):
        x = self.window_size["width"] * 0.9
        y = self.window_size["height"] * 0.1
        self.driver.tap([(x,y)],500)

    def download_live_record(self):
        self.click_button_with_id("tv_download")
        self.wait_transition(10)
        self.press_home_key()
        self.wait_transition(1)
        self.driver.open_notifications()
        self.wait_transition(1)
        #self.swipe()
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            self.logger.info(u'Check text view: {}'.format(el.text))
            if el.text == "Tap to edit":
                self.logger.info(u'Found text view: {}'.format(el.text))
                self.wait_transition(2)
                self.click_textview_with_text(["Tap to edit","Tap to edit"])
                self.wait_transition(1)
                return
        # Expand Soocii notification
        for el in items:
            if "Soocii" in el.text:
                el.click()
                self.wait_transition(1)
                #Click on "Soocii Logger"
                items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
                for el in items:
                    if el.text == "Tap to edit":
                        el.click()
                        self.wait_transition(1)
                        return
        self.wait_transition(1)

    def chat_live(self,a):
        x = self.window_size["width"] * 0.5
        y = self.window_size["height"] * 0.5
        self.wait_transition(20)
        #self.driver.tap([(x,y)],350)
        self.wait_transition(2)
        self.click_button_with_id("messageEditText")
        self.wait_transition(2)
        self.send_text_with_id("messageEditText", a)
        self.logger.info('sent message: {}'.format(a))
        self.click_button_with_id("sendButton")
        self.wait_transition(1)

    def click_sharelink_button(self):
        self.click_button_with_id("shareButton")
        self.wait_transition(5)
        self.press_back_key()

    def click_viewer_button(self):
        self.wait_transition(5)
        self.click_button_with_id("img_btn_check_viewers")
        self.wait_transition(1)

    def leave_live(self):
        self.press_back_key()
        self.press_back_key()
        self.wait_transition(2)

    def goto_RTMP(self):
        self.swipe_to_newsfeed()
        self.wait_transition(30)
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            self.logger.info(u'Check text view: {}'.format(el.text))
            if el.text == "test stream":
                self.logger.info(u'Found text view: {}'.format(el.text))
                self.wait_transition(2)
                self.click_textview_with_text(["test stream","test stream"])
                self.wait_transition(1)
                return

    def gotochat_with_discovery(self):
        self.swipe_discover()
        x=1
        while x==1:
            items = self.wait.until(EC.presence_of_all_elements_located((By.ID, "tv_streaming_message")))
            for el in items:
                self.logger.info(u'Check text view: {}'.format(el.text))
                if el.text == "test stream":
                    self.logger.info(u'Found text view: {}'.format(el.text))
                    el.click()
                    x=2
                    return

    def open_live_ingame(self):
        self.click_button_with_id("iv_menu_icon_broadcast")
        self.wait_transition(2)
        self.click_accept()
        self.wait_transition(2)
        self.click_button_with_id("btn_friend_broadcast")
        self.wait_transition(2)
        self.click_button_with_id("button1")
        self.wait_transition(2)

    def record_ingame(self):
        self.click_button_with_id("iv_menu_icon_record")
        self.wait_transition(2)
        self.click_button_with_id("button1")

    def screenshot_ingame(self):
        self.click_button_with_id("iv_menu_icon_screenshot")
        self.wait_transition(2)
        self.click_button_with_id("button1")


    def check_viewer_name(self):
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            self.logger.info(u'Check text view: {}'.format(el.text))
            if el.text == "chnnnnnnnb":
                self.logger.info(u'Found text view: {}'.format(el.text))
                self.wait_transition(2)
                return True
        return False

    def edit_infophoto(self):
        self.wait_transition(2)
        self.click_button_with_id("rl_edit")

        self.wait_transition(2)
        self.click_button_with_id("iv_avatar")

        self.wait_transition(2)
       # self.Brosew_photo()
        self.click_textview_with_text([u"選擇照片","Browse photo"])

        self.wait_transition(2)
        photofold = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.RelativeLayout")))
        photofold[0].click()

        self.wait_transition(1)
        if self.isAndroid5():
            photobtn = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.view.View")))
            photobtn[1].click()
        else:
            photobtn = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.view.ViewGroup")))
            photobtn[1].click()
        self.wait_transition(5)
       # self.click_textview_with_id("action_next")
        self.click_textview_with_text([u"下一步","next"])
        self.wait_transition(1)

    def edit_username_and_introduction(self):
        self.wait_transition(2)
        self.send_text_with_id("edit_display_name", "edit display")

        self.wait_transition(2)
        self.send_text_with_id("et_about", "Hello welcome to my broatcast!!!")
        self.wait_transition(2)

        self.click_textview_with_id("menu_personal_info_check")
        self.wait_transition(2)
        self.swipe_refresh()
        self.swipe_refresh()

    def check_text(self, id, text):
        texts = self.wait.until(EC.presence_of_element_located((By.ID, id)))
        texts.text.index(text)

    def friend_select_message_edittext(self, upload,x):
        self.click_button_with_id("friend_select_message_edittext")
        self.wait_transition(1)
        self.send_text_with_id("friend_select_message_edittext", upload+str(x+1))
        self.logger.info('sent upload: {}'.format(upload+str(x+1)))
        self.wait_transition(3)

    def wait_autopost(self):
        self.wait_transition(30)

    def setting_autopost(self):
        self.click_button_with_id("ib_broadcast_auto_post_switch")
        self.wait_transition(3)
        self.click_button_with_id("btn_confirm")
        self.wait_transition(3)

    def check_broadcast(self,x):
        self.swipe_up(500)
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            self.logger.info(u'Check text view: {}'.format(el.text))
            if "autopost" in el.text:
                self.logger.info(u'Found text view: {}'.format(el.text))
                self.wait_transition(2)
                self.swipe_down(500)
                return True
            elif "broadcast" in el.text:
                self.logger.info(u'Found text view: {}'.format(el.text))
                self.wait_transition(2)
                self.swipe_down(500)
                return True
        return False

    def check_search_button(self):
        self.click_button_with_id("iv_search_icon")
        self.wait_transition(2)

    def check_result_tag(self):
        self.click_textview_with_id("tag_name")
        self.wait_transition(5)

    def check_result_tag_share(self):
        self.click_button_with_id("action_share")
        self.wait_transition(3)
        self.press_back_key()
        self.press_back_key()

    def check_search_user_button(self):
        self.click_textview_with_text(u"用戶")
        self.wait_transition(2)
        self.click_textview_with_text("battle")
        self.wait_transition(2)

    def search_name(self,text):
        self.send_text_with_id("search_field",text)
        self.wait_transition(2)
        self.click_textview_with_text(u"尋找")

    def search_batt_game(self):
        self.send_text_with_id("search_field","batt")
        self.wait_transition(1)
        self.click_button_with_id("search_button")
        self.wait_transition(1)

    def click_onboading_step(self):
        self.wait_transition(2)
        center_x = self.window_size["width"]
        if self.isAndroid8():
            self.wait_transition(2)
            self.driver.tap([(420, 540)], 500) 
            self.wait_transition(1)
            self.driver.tap([(420, 540)], 500)
            self.wait_transition(1)
            self.driver.tap([(820, 540)], 500) 
            self.wait_transition(1)
            self.click_button_with_id("post_left_top")
            self.wait_transition(1)
            self.press_back_key()
            self.wait_transition(0.5)
            self.driver.tap([(800, 650)], 500)
            return

        if center_x == 1080:
            self.wait_transition(2)
            self.driver.tap([(400, 650)], 500) 
            self.wait_transition(1)
            self.driver.tap([(400, 650)], 500)
            self.wait_transition(1)
            self.driver.tap([(800, 650)], 500) 
            self.wait_transition(1)
            self.click_button_with_id("post_left_top")
            self.wait_transition(1)
            self.press_back_key()
            self.wait_transition(0.5)
            self.driver.tap([(800, 650)], 500) 
        else:
            self.wait_transition(2)
            self.driver.tap([(250, 400)], 500) 
            self.wait_transition(1)
            self.driver.tap([(250, 400)], 500)
            self.wait_transition(1)
            self.driver.tap([(530, 400)], 500) 
            self.wait_transition(1)
            self.click_button_with_id("post_left_top")
            self.wait_transition(1)
            self.press_back_key()
            self.wait_transition(0.5)
            self.driver.tap([(530, 400)], 500) 

    def login_point(self):
        self.wait_transition(6)
        self.click_textview_with_text(u"確認")
        self.wait_transition(1)
        self.click_button_with_id("icon_profile")

    def check_aboutme_coin(self):
        self.swipe_to_aboutme()
        self.wait_transition(0.5)
        coinObject = self.wait.until(EC.presence_of_element_located((By.ID, "tv_point")))
        self.logger.info(u"金幣入口外的金幣數:"+coinObject.text)
        cointext = self.Tertile(coinObject.text)#裡面數字表示有逗號 38105 outside -> 38,105 inside
        coinObject.click()
        
        self.wait_transition(1)
        if self.__visibility_of_textview(cointext):
            self.press_back_key()
            self.wait_transition(1)
            return True
        else:
            self.press_back_key()
            self.wait_transition(1)
            return False

    def check_aboutme_gift(self):
        try:
            self.swipe_to_aboutme()
            self.wait_transition(0.5)
            giftObject = self.wait.until(EC.presence_of_element_located((By.ID, "tv_gift")))
            giftObject.click()
            self.wait_transition(3)
            self.press_back_key()
            self.wait_transition(0.5)
            return True
        except:
            return False

    def check_aboutme_missions(self):
        try:    
            self.swipe_to_aboutme()
            self.wait_transition(0.5)
            missionsObject = self.wait.until(EC.presence_of_element_located((By.ID, "tv_mission")))
            missionsObject.click()
            self.wait_transition(2)
            self.press_back_key()
            self.wait_transition(0.5)
            return True
        except:
            return False

    def check_menu_ad(self):
        try:      
            self.click_button_with_id("navi_menu")
            self.wait_transition(1)
            self.click_textview_with_text(u"壽司點")
            self.wait_transition(1)
            items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
            point = items[2].text
            self.logger.info("point:"+point)
            self.wait_transition(10)
            self.click_button_with_id("tv_rewarded_button")
            self.wait_transition(9)
            self.press_back_key() #close_button_icon
            self.wait_transition(1)
            self.click_button_with_id("btn_right")
            self.wait_transition(1)
            items = items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
            newpoint = items[2].text
            self.logger.info("newpoint:"+newpoint)
            self.press_back_key()
            if point != newpoint:
                return True
            else:
                raise
        except:
            return False

    def Tertile(self, inputstr):
        strlen = len(inputstr)
        inputstr = inputstr[::-1]
        print(inputstr)
        end = 3
        count = strlen/3
        for i in range(1, count+1):
            inputstr = inputstr[0:end] + "," + inputstr[end:]
            end += 4
        inputstr = inputstr[::-1]
        return inputstr