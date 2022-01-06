"""
user:石文斌
time：2022/01/05

"""
import time
import unittest

from appium import webdriver

from config.config import desired_caps
from element.elementLogin import Login
from common.tool import Tool


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:  # 执行方法前准备工作
        self.parme = {"port": 4723}
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % str(self.parme['port']), desired_caps)
        Tool.InstallApp(self)
        Tool.StartApp(self)
        self.driver.implicitly_wait(20)  # 稳定元素

    def tearDown(self) -> None:  # 执行方法后工作
        # print("...........结束..............")
        time.sleep(3)

    def test_LoginApp(self):
        UserName = '1503593264@qq.com'
        Password = '123456'
        Login.GetLoginConsentToLaw(self).click()
        time.sleep(2)
        Login.GetLoginLoginInfo(self).click()
        time.sleep(3)
        Login.GetLoginUsernameEdit(self).click()
        Login.GetLoginUsernameEdit(self).send_keys(UserName)
        time.sleep(1)
        Login.GetLoginUserPassword(self).click()
        Login.GetLoginUserPassword(self).send_keys(Password)
        time.sleep(1)
        Login.GetLoginUserLogin(self).click()
        time.sleep(5)
        Message = Login.GetLoginUserLoginMessage(self).text
        if Message:
            time.sleep(3)
            Login.GetLoginUserLoginMessageAgree(self).click()
            time.sleep(1)
            Tool.AgreeJurisdiction(self)

