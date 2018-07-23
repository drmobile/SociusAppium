#coding=utf-8
import sys
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from base import AppiumBaseHelper

class FacebookHelper(unittest.TestCase, AppiumBaseHelper):
    def __init__(self, driver, platformName, platformVersion):
        AppiumBaseHelper.__init__(self, driver, platformName, platformVersion)

    def login(self, username, password):
        bClickedLogin = False
        bGrantedPermission = False
        bContinue=False

        # wait login transition
        self.wait_transition(4)
        if self.click_button_with_text([u'繼續']) == True:
            bContinue=True

            return True

        if bContinue !=True:    
        # Webview-based
            allEditText = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.EditText")))

            self.logger.info(len(allEditText))

            self.assertTrue(len(allEditText)==2 or 3, 'could not identify facebook two text fields for user name and password')
            self.assertIsNotNone(allEditText)
            # User name field
            el = allEditText[0]
            self.logger.info(u'text of located element: {}'.format(el.text))
            el.clear()
            el.send_keys(username)
            self.driver.hide_keyboard()

            #if self.click_button_with_text([u'登入']) == True:
                #bClickedLogin = True

            # Password field
            el = allEditText[1]
            self.logger.info(u'text of located element: {}'.format(el.text))
            el.send_keys(password)
            self.driver.hide_keyboard()

            self.logger.info('Try to locate facebook login button by text')
            if self.click_button_with_text([u'登入']) == True:
                bClickedLogin = True
            self.assertTrue(bClickedLogin, 'could not identify facebook login button in the page')

            # wait for loading
            self.wait_transition(4)

            #cancel google smart lock
            self.click_button_with_text(u'一律不要')

            # grant facebook permission
            self.logger.info('Try to locate facebook permission button by text')
            if self.click_button_with_text([u'繼續', u'確定']) == True:
                bGrantedPermission = True
            self.assertTrue(bGrantedPermission, 'could not identify facebook grant permission button in the page')

            # wait for loading
            self.wait_transition(1)

        return True

class TwitterHelper(unittest.TestCase, AppiumBaseHelper):
    def __init__(self, driver, platformName, platformVersion):
        AppiumBaseHelper.__init__(self, driver, platformName, platformVersion)

    def login2(self, username, password):
        bClickedLogin = False
        bGrantedPermission = False

        # wait login transition
        self.wait_transition(2)

        # Webview-based
        allEditText = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.EditText")))
        self.assertTrue(len(allEditText)==2, 'could not identify facebook two text fields for user name and password')
        self.assertIsNotNone(allEditText)
        # User name field
        el = allEditText[0]
        self.logger.info(u'text of located element: {}'.format(el.text))
        el.send_keys(username)
        self.driver.hide_keyboard()
        # Password field
        el = allEditText[1]
        self.logger.info(u'text of located element: {}'.format(el.text))
        el.send_keys(password)
        self.driver.hide_keyboard()

        self.logger.info('Try to locate twitter login button by text')
        if self.click_button_with_text([u'授權應用程式','Authorize app']) == True:
            bClickedLogin = True
        self.assertTrue(bClickedLogin, 'could not identify twitter login button in the page')

        # wait for loading
        self.wait_transition(4)
        # wait for loading
        self.wait_transition(1)

        return True



class SysHelper(unittest.TestCase, AppiumBaseHelper):
    def __init__(self, driver, platformName, platformVersion):
        AppiumBaseHelper.__init__(self, driver, platformName, platformVersion)
        self.fb = FacebookHelper(driver, platformName, platformVersion)
        self.twitter=TwitterHelper(driver, platformName, platformVersion)

    def start_soocii(self):
        # The function does not work due to missing android:exported=”true” for the activity
        # self.driver.start_activity('me.soocii.socius.staging', 'me.soocii.socius.core.ui.MainActivity')
        self.press_recent_apps_key()
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            if self.app_name in el.text:
                try:
                    el.click()
                    return self.is_aboutme()#check wheather in the about me
                except:
                    center_x=self.window_size["width"]
                    center_y=self.window_size["height"]                    
                    self.driver.tap([(center_x*0.6,center_y*0.5)],500)#for oppo back to soocii


                return
        raise NoSuchElementException('could not identify soocii in recent apps')

    def start_snake_off(self):
        self.press_recent_apps_key()
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            if "Snake Off" in el.text:
                el.click()
                return
        raise NoSuchElementException('could not identify snake off in recent apps')


    def start_setting_page(self):
        self.driver.start_activity('com.android.settings', 'com.android.settings.Settings')

    # support for sony z3, samsung note5
    def __enable_usage_access_sony_z3(self):
        # Usage access permission
        self.wait_transition(5)
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            self.logger.info(u'text of located element: {}'.format(el.text))
            if self.app_name in el.text:
                # 1st level of setting
                self.wait_transition(4)
                el.click()

                # 2nd level of setting
                switch = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.Switch")))
                self.assertIsNotNone(switch)
                switch.click()

                # Back to Soccii App
                self.press_back_key()
                self.press_back_key()
                self.logger.info('enabled usage access in sony z3, samsung note5')
                return True

    # support for sony z3, asus zenfone2
    def __enable_usage_access_sony_m4(self):
        # Usage access permission
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            self.logger.info(u'text of located element: {}'.format(el.text))
            if self.app_name in el.text:
                # 1st level of setting
                self.wait_transition(4)
                el.click()
                # Confirmation
                if self.click_button_with_text(["OK", u"確定"]) is True:
                    # Back to Soccii App
                    self.press_back_key()
                    self.logger.info('enabled usage access in sony m4')
                    return True
                else:
                    self.click_button_with_text(["Allow",u"允許"])
                    self.wait_transition(1)
                    # Back to Soccii App
                    self.press_back_key()
                    self.wait_transition(1)
                    self.click_textview_with_id("confirm")
                    self.logger.info('enabled usage access in sony m4')
                    return True

                # could not identify alert dialog
                self.logger.info('could not identify confirmation dialog')
                raise NoSuchElementException('could not identify confirmation dialog')

    def enable_usage_access(self):
        # click on confirm "請選擇Soocii，並將可存取使用情形打開"
        self.click_textview_with_id("confirm")
        self.wait_transition(2)

        if self.isAndroid5() == True:
            self.logger.info('try enable usage access in Android 5')
            self.wait_transition(2)
            self.__enable_usage_access_sony_m4()
        else:
            self.logger.info('try enable usage access in Android 6+')
            self.wait_transition(2)
            self.__enable_usage_access_sony_z3()

        # try:
        #     self.logger.info('try enable usage access in sony m4')
        #     self.__enable_usage_access_sony_m4()
        # except:
        #     self.logger.info('caught exception: {}'.format(sys.exc_info()[0]))
        #     try:
        #         self.logger.info('try enable usage access in sony z3, samsung note5')
        #         self.__enable_usage_access_sony_z3()
        #     except:
        #         raise

    def enable_draw_on_top_layer(self):
        # click on confirm "請選擇允許在其他應用程式上層繪製內容，並將其打開"
        # only require for Android6+
        self.wait_transition(3)
        if self.isAndroid5():
            return
        self.click_textview_with_id("confirm")

        # draw on top layer permission
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
        for el in items:
            self.logger.info(u'text of located element: {}'.format(el.text))
            el.click()

        # Back to Soccii App
        self.press_back_key()
        self.logger.info('enabled draw on top layer')
        return True

    def login_facebook_account(self, username, password):
        self.logger.info('username: {}, password: {}'.format(username, password))
        self.fb.login(username, password)

    def login_twitter_account(self, username, password):
        self.logger.info('username: {}, password: {}'.format(username, password))
        self.twitter.login2(username, password)
        
    def login_google_account(self):
        self.wait_transition(1)
        self.click_textview_with_text(["Dr. Booster","Dr. Booster"])
        self.wait_transition(3)
    def Facebook_clear_data_step(self):
        self.wait_transition(2)
        self.click_button_with_text(u"接受並繼續")
        self.click_button_with_text(u"繼續")
        self.click_button_with_text(u"好，我知道了")
        self.wait_transition(5)
