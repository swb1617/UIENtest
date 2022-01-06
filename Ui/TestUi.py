"""
user:石文斌
time：2021/12/06

"""
import time
import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from element.button import Tap
from element.elementMe import Me
from element.elementMenu import Menu
from element.elementFriend import Friend
from element.elementFollow import Follow
from element.elementPeople import People
from element.elementMessage import Message
from element.elementData import Data
from element.elementActivity import Activity


class TestUI(unittest.TestCase):

    def setUp(self) -> None:  # 执行方法前准备工作
        self.driver.implicitly_wait(20)  # 稳定元素
        # print("...........开始.............")
        # self.driver.background_app(5)   # 模拟热启动
        # InputMethod.ChangeIme(self)
        time.sleep(3)

    def tearDown(self) -> None:  # 执行方法后工作
        # print("...........结束..............")
        time.sleep(3)
        self.driver.close_app()  # 定义关闭APP方法
        time.sleep(3)
        self.driver.start_activity('com.igpsport.globalapp', 'com.igpsport.globalapp.activity.v3.SplashActivity')
        # 重新启动APP
        time.sleep(3)

    @classmethod
    def setUpClass(cls) -> None:  # 设置手机相关参数
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'test01',
            'appPackage': 'com.igpsport.globalapp',
            'appActivity': 'com.igpsport.globalapp.activity.v3.SplashActivity',
            # 国际版APP
            'noReset': True,
            'newCommandTimeout': 6000,
            # 更换底层驱动
            'automationName': 'UiAutomator2'
            # 'unicodeKeyboard': False,  # 修改手机的输入法
            # 'resetKeyboard': False
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def SwipeDown(self):  # 定义下滑动方法
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.5
        y1, y2 = height * 0.35, height * 0.7
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)

    def SwipeFriendLeft(self):  # 定义下滑动方法
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1, x2 = width * 0.9, width * 0.1
        y1 = y2 = height * 0.35
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)

    def SwipeLittleUp(self):  # 定义上滑动方法
        size = self.driver.get_window_size()  # 获取手机屏幕尺寸
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.7
        y1, y2 = height * 0.89, height * 0.86
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)  # 滑动方法

    def SwipeLittleDown(self):  # 定义切换性别的下滑动方法
        size = self.driver.get_window_size()  # 获取手机屏幕尺寸
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.7
        y1, y2 = height * 0.9, height * 0.95
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)  # 滑动方法

    def GetToast(self, toast_message):
        message = '//*[@text=\'{}\']'.format(toast_message)
        toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(by=By.XPATH, value=message))
        print(toast_element.text)
        assert toast_element.text == toast_message

    def PressEnter(self):  # 定义回车键
        self.driver.press_keycode(66)

    def PressBack(self):  # 定义返回键
        self.driver.keyevent(4)

    def PressMoveEnd(self):  # 定义光标移动文本末尾
        self.driver.keyevent(123)

    def test_MenuMessage(self):  # 主页消息界面
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuMessageInto(self).click()
            Message.GetMessageRead(self).click()
            Message.GetMeaagaeBack(self).click()
        except:
            self.driver.save_screenshot('MenuMessageError.png')
            raise

    def test_MenuGoals(self):  # 主页月骑行目标
        MonthGoals = 777
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuTrainingGoalsInto(self).click()
            Me.GetMeUserGoalsText(self).click()
            Me.GetMeUserGoalsText(self).clear()
            Me.GetMeUserGoalsText(self).send_keys(MonthGoals)
            Me.GetMeUserGoalsSave(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('MenuGoalsError.png')
            raise

    def test_ChangeMapStyle(self):  # 地图样式
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMapStyleInto(self).click()
            Data.GetDataMapStyleMode(self).click()
            Data.GetDataMapStyleSave(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ChangeMapStyleError.png')
            raise

    def test_OpenMapGoals(self):  # 地图距离点
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMapStyleInto(self).click()
            Data.GetDataMapStyleGoals(self).click()
            Data.GetDataMapStyleSave(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('MenuGoalsError.png')
            raise

    def test_SaveMyLine(self):  # 保存为我的线路
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(4)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToSaveMyLine(self).click()
            # self.GetToast("保存成功！")
            time.sleep(3)
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('SaveMyLineError.png')
            raise

    @unittest.skip
    def test_ExportDataFit(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToExportFile(self).click()
            Data.GetDataExportDataFit(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataFitError.png')
            raise

    @unittest.skip
    def test_ExportDataGpx(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToExportFile(self).click()
            Data.GetDataExportDataGpx(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataGpxError.png')
            raise

    @unittest.skip
    def test_ExportDataTcx(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToExportFile(self).click()
            Data.GetDataExportDataTcx(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataTcxError.png')
            raise

    @unittest.skip("删除数据")
    def test_DeleteData(self):  # 删除数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToDeleteData(self).click()
            Data.GetDataDeleteDataOk(self).click()
            time.sleep(3)
        except:
            self.driver.save_screenshot('DeleteDataError.png')
            raise

    def test_ShareWatermarkData(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            # Data.GetDataWatermarkPhotoChangePhoto(self).click()
            # Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            # Data.GetDataWatermarkPhotoSeePhoto(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkPhotoSave(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkDataError.png')
            raise

    def test_ShareWatermarkDataDefault(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(1)
            Data.GetDataWatermarkRestoreDefault(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkDataDefaultError.png')
            raise

    def test_ShareWatermarkDataChoose(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkDataChooseError.png')
            raise

    def test_ShareWatermarkTrack(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            time.sleep(1)
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            # Data.GetDataWatermarkPhotoChangePhoto(self).click()
            # Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            # Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkTrackError.png')
            raise

    def test_ShareWatermarkTrackDefault(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(1)
            Data.GetDataWatermarkRestoreDefault(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkTrackDefaultError.png')
            raise

    def test_ShareWatermarkTrackChoose(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkTrackChooseError.png')
            raise

    def test_ShareWatermarkAlt(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(3)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(1)
            Data.GetDataWatermarkRestoreDefault(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkAltError.png')
            raise

    def test_ShareWatermarkAltDefault(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(3)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(1)
            Data.GetDataWatermarkRestoreDefault(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkAltDefaultError.png')
            raise

    def test_ShareWatermarkAltChoose(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(3)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkAltChooseError.png')
            raise

    def test_Calendar(self):  # 日历界面
        try:
            Tap.GetToActivity(self).click()
            time.sleep(1)
            Activity.GetActivityCalendarInfo(self).click()
            time.sleep(2)
            Activity.GetActivityCalendarBack(self).click()
        except:
            self.driver.save_screenshot('CalendarError.png')
            raise

    def test_ActivityShare(self):  # 活动分享
        try:
            Tap.GetToActivity(self).click()
            Activity.GetActivityShareInfo(self).click()
            time.sleep(1)
            Activity.GetActivityShareSave(self).click()
            Activity.GetActivityShareBack(self).click()
        except:
            self.driver.save_screenshot('ActivityShareError.png')
            raise

    def test_StatisticData(self):  # 数据管理界面
        try:
            Tap.GetToActivity(self).click()
            Activity.GetActivityDataStatisticInfo(self).click()
            time.sleep(1)
            Activity.GetActivityDataStatisticBack(self).click()
        except:
            self.driver.save_screenshot('StatisicDataError.png')
            raise

    def test_PersonalRecords(self):  # 个人记录界面
        try:
            Tap.GetToActivity(self).click()
            Activity.GetActivityPersonalRecordsInfo(self).click()
            Activity.GetActivityPersonalRecordsShare(self).click()
            time.sleep(3)
            Activity.GetActivityPersonalRecordsShareBack(self).click()
            time.sleep(1)
            Activity.GetActivityPersonalRecordsBack(self).click()
        except:
            self.driver.save_screenshot('PersonalRecordsError.png')
            raise

    def test_MeSettingHR(self):  # 设置心率区间
        try:
            Tap.GetToMe(self).click()
            Me.GetMEUserDetailsInfo(self).click()
            Me.GetMeSettingHRInfo(self).click()
            time.sleep(1)
            Me.GetMeSettingHR(self).click()
            Me.GetMeSettingHRBack(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('MeSettingHRError.png')
            raise

    def test_MeSettingPower(self):  # 设置功率区间
        try:
            Tap.GetToMe(self).click()
            Me.GetMEUserDetailsInfo(self).click()
            Me.GetMeSettingPowerInfo(self).click()
            time.sleep(1)
            Me.GetMeSettingPower(self).click()
            Me.GetMeSettingPowerBack(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('MeSettingPowerError.png')
            raise

    def test_AboutUs(self):  # 关于我们页面
        try:
            Tap.GetToMe(self).click()
            Me.GetMeAboutUs(self).click()
            time.sleep(3)
            Me.GetMeAboutUsBack(self).click()
        except:
            self.driver.save_screenshot('AboutUsError.png')
            raise

    def test_FeedBack1(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList1(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack1Error.png')
            raise

    def test_FeedBack2(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList2(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack2Error.png')
            raise

    def test_FeedBack3(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList3(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack3Error.png')
            raise

    def test_FeedBack4(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList4(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack4Error.png')
            raise

    def test_FeedBack5(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList5(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack5Error.png')
            raise

    def test_FeedBack6(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList6(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack6Error.png')
            raise

    def test_FeedBack7(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList7(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack7Error.png')
            raise

    def test_FeedBack8(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList8(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack8Error.png')
            raise

    def test_FeedBack9(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList9(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack9Error.png')
            raise

    def test_FeedBackA(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionLista(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBackAError.png')
            raise

    def test_FeedBackB(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionListb(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTitle(self).click()
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBackBError.png')
            raise

    def test_ActivityChangeGoals(self):  # 日历界面骑行目标
        try:
            MonthlyGoals = 520
            Tap.GetToActivity(self).click()
            Activity.GetActivityCalendarInfo(self).click()
            Activity.GetActivityCalendarGoalsEdit(self).click()
            Activity.GetActivityCalendarGoalsEditText(self).click()
            Activity.GetActivityCalendarGoalsEditText(self).clear()
            Activity.GetActivityCalendarGoalsEditText(self).send_keys(MonthlyGoals)
            Activity.GetActivityCalendarGoalsEditSave(self).click()
            Activity.GetActivityCalendarBack(self).click()
        except:
            self.driver.save_screenshot('ActivityChangeGoalsError.png')
            raise

    def test_MenuChangeGoals(self):  # 主页修改骑行目标
        try:
            MonthlyGoals = 888
            Tap.GetToHome(self).click()
            Menu.GetMenuTrainingGoalsInto(self).click()
            Me.GetMeUserGoalsText(self).click()
            Me.GetMeUserGoalsText(self).clear()
            Me.GetMeUserGoalsText(self).send_keys(MonthlyGoals)  # id定位
            Me.GetMeUserGoalsSave(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('MenuChangeGoalsError.png')
            raise

    def test_MeChangeGoals(self):  # 我的界面修改骑行目标
        try:
            MonthlyGoals = 666
            Tap.GetToMe(self).click()
            Me.GetMEUserDetailsInfo(self).click()
            Me.GetMeUserGoalsEdit(self).click()
            Me.GetMeUserGoalsText(self).click()
            Me.GetMeUserGoalsText(self).clear()
            Me.GetMeUserGoalsText(self).send_keys(MonthlyGoals)  # id定位
            Me.GetMeUserGoalsSave(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('MeChangeGoalsError.png')
            raise

    @unittest.skip
    def test_SexChange(self):  # 性别设置
        try:
            Tap.GetToMe(self).click()
            Me.GetMEUserDetailsInfo(self).click()
            UserSex = Me.GetMeUserSex(self).text
            if UserSex == '男':
                Me.GetMeUserSexInfo(self).click()
                time.sleep(1)
                self.SwipeLittleUp()
                Me.GetMeUserSexSave(self).click()
                Me.GetMeUserDetailsBack(self).click()
                Tap.GetToMe(self).click()
                Me.GetMEUserDetailsInfo(self).click()
                Sex = Me.GetMeUserSex(self).text
                Me.GetMeUserDetailsBack(self).click()
                self.assertNotEqual(Sex, UserSex)
            else:
                Me.GetMeUserSexInfo(self).click()
                self.SwipeLittleDown()
                Me.GetMeUserSexSave(self).click()
                Me.GetMeUserDetailsBack(self).click()
                Tap.GetToMe(self).click()
                Me.GetMEUserDetailsInfo(self).click()
                Sex = Me.GetMeUserSex(self).text
                Me.GetMeUserDetailsBack(self).click()
                self.assertNotEqual(Sex, UserSex)
        except:
            self.driver.save_screenshot('SexChangeError.png')
            raise

    @unittest.skip
    def test_LanguageChange(self):  # 切换语言
        try:
            Tap.GetToMe(self).click()
            Me.GetMeAccountSettingInfo(self).click()
            time.sleep(3)
            Me.GetMeLanguageSetting(self).click()
            time.sleep(2)
            self.SwipeLittleUp()
            time.sleep(2)
            Me.GetMeLanguageSettingSave(self).click()
            time.sleep(1)
            OldLanguage = Me.GetMeLanguageMessage(self).text
            Me.GetMeAccountSettingSave(self).click()
            time.sleep(1)
            Tap.GetToMe(self).click()
            Me.GetMeAccountSettingInfo(self).click()
            time.sleep(3)
            NewLanguage = Me.GetMeLanguageMessage(self).text
            time.sleep(2)
            Me.GetMeAccountSettingBack(self).click()
            self.assertEqual(OldLanguage, NewLanguage)
        except:
            self.driver.save_screenshot('LanguageChangeError.png')
            raise

    def test_MeNotification(self):  # 消息设置界面
        try:
            Tap.GetToMe(self).click()
            Me.GetMeNotification(self).click()
            time.sleep(3)
            Me.GetMeNotificationBack(self).click()
        except:
            self.driver.save_screenshot('MeNotificationError.png')
            raise

    def test_AccumulatedMileageConsistency(self):  # 累计里程一致性
        try:
            Tap.GetToActivity(self).click()
            time.sleep(3)
            ActivityDistance = Activity.GetActivityTotalDistance(self).text
            Activity.GetActivityDataStatisticInfo(self).click()
            time.sleep(3)
            Activity.GetActivityDataStatisticAll(self).click()
            time.sleep(3)
            ActivityDistances = Activity.GetActivityDataStatisticAllDistances(self).text
            Activity.GetActivityDataStatisticBack(self).click()
            self.assertEqual(ActivityDistance, ActivityDistances)
        except:
            self.driver.save_screenshot('AccumulatedMileageConsistencyError.png')
            raise

    def test_CumulativeTimesConsistency(self):  # 累计时间一致性
        try:
            Tap.GetToActivity(self).click()
            ActivityFrequency = Activity.GetActivityTotalFrequency(self).text
            Activity.GetActivityDataStatisticInfo(self).click()
            Activity.GetActivityDataStatisticAll(self).click()
            time.sleep(3)
            ActivityFrequencys = Activity.GetActivityDataStatisticAllFrequency(self).text
            Activity.GetActivityDataStatisticBack(self).click()
            self.assertEqual(ActivityFrequencys, ActivityFrequency)
        except:
            self.driver.save_screenshot('CumulativeTimesConsistencyError.png')
            raise

    def test_AverageVelocityConsistency(self):  # 平均速度一致性
        try:
            Tap.GetToActivity(self).click()
            ActivityAverageVelocity = Activity.GetActivityTotalAverageVelocity(self).text
            Activity.GetActivityDataStatisticInfo(self).click()
            Activity.GetActivityDataStatisticAll(self).click()
            time.sleep(2)
            ActivityAverageVelocitys = Activity.GetActivityDataStatisticAllAverageVelocity(self).text
            Activity.GetActivityDataStatisticBack(self).click()
            self.assertIn(ActivityAverageVelocity, ActivityAverageVelocitys)
        except:
            self.driver.save_screenshot('AverageVelocityConsistencyError.png')
            raise

    @unittest.skip("需含有当月骑行记录！")
    def test_MonthlyCyclingTimes(self):  # 月度骑行次数一致性
        try:
            Tap.GetToActivity(self).click()
            ActivityMonthFrequency = Activity.GetActivityMonthFrequency(self).text
            Activity.GetActivityDataStatisticInfo(self).click()
            time.sleep(1)
            Activity.GetActivityDataStatisticMonth(self).click()
            time.sleep(2)
            ActivityDataStatisicMonthFrequency = Activity.GetActivityDataStatisticMonthFrequency(self).text
            Activity.GetActivityDataStatisticBack(self).click()
            self.assertEqual(ActivityDataStatisicMonthFrequency, ActivityMonthFrequency)
        except:
            self.driver.save_screenshot('MonthlyCyclingTimesError.png')
            raise

    def test_ResetPassword(self):  # 修改密码
        try:
            OldPassword = 123456
            NewPassword = 123456
            Tap.GetToMe(self).click()
            Me.GetMeAccountSettingInfo(self).click()
            Me.GetMeResetPasswordInfo(self).click()  # 1207崩溃
            Me.GetMeOldPasswordText(self).click()
            Me.GetMeOldPasswordText(self).send_keys(OldPassword)
            Me.GetMeNemPasswordText(self).click()
            Me.GetMeNemPasswordText(self).send_keys(NewPassword)
            Me.GetMeAgainNemPasswordText(self).click()
            Me.GetMeAgainNemPasswordText(self).send_keys(NewPassword)
            Me.GetMeConfirmPassword(self).click()
            time.sleep(3)
            Me.GetMeAccountSettingBack(self).click()
        except:
            self.driver.save_screenshot('ResetPasswordError.png')
            raise

    # @unittest.skip
    def test_FollowFriend(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFriendInto(self).click()
            time.sleep(5)
            FriendName = Friend.GetFriendFirstPeopleName(self).text
            print(FriendName)
            FriendDistance = Friend.GetFriendFirstPeopleDistance(self).text
            Friend.GetFriendFirstPeopleFollow(self).click()
            Menu.GetMenuFriendBack(self).click()
            Tap.GetToMe(self).click()
            FollowNumber = Me.GetFollowNumber(self).text
            self.assertEqual(1, int(FollowNumber))
            Follow.GetFollowInfo(self).click()
            time.sleep(2)
            FollowName = Follow.GetFollowFirstPeopleName(self).text
            FollowDistance = Follow.GetFollowFirstPeopleDistance(self).text
            FollowId = Follow.GetFollowFirstPeopleId(self).text
            self.assertEqual(FriendName, FollowName)
            self.assertIn(FriendDistance, FollowDistance)
            Follow.GetFollowFirstPeopleInfo(self).click()
            time.sleep(2)
            PeopleId = People.GetPeopleId(self).text
            PeopleName = People.GetPeopleName(self).text
            self.assertEqual(FollowId, PeopleId)
            self.assertEqual(FollowName, PeopleName)
            People.GetPeopleFollowed(self).click()
            People.GetPeopleBack(self).click()
            time.sleep(1)
            Follow.GetFollowBack(self).click()
        except:
            self.driver.save_screenshot('FollowFriendError.png')
            raise

    def test_FollowSeekFriend(self):
        FriendID = 148788
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFriendInto(self).click()
            time.sleep(5)
            Friend.GetFriendSeekFriendId(self).click()
            Friend.GetFriendSeekText(self).click()
            Friend.GetFriendSeekText(self).send_keys(FriendID)
            time.sleep(1)
            self.PressEnter()
            time.sleep(1)
            Friend.GetFriendSeekFriendFollow(self).click()
            self.PressBack()
            time.sleep(1)
            Menu.GetMenuFriendBack(self).click()
            Tap.GetToMe(self).click()
            FollowNumber = Me.GetFollowNumber(self).text
            self.assertEqual(1, int(FollowNumber))
            Follow.GetFollowInfo(self).click()
            time.sleep(2)
            FollowName = Follow.GetFollowFirstPeopleName(self).text
            FollowId = Follow.GetFollowFirstPeopleId(self).text
            Follow.GetFollowFirstPeopleInfo(self).click()
            time.sleep(2)
            PeopleId = People.GetPeopleId(self).text
            PeopleName = People.GetPeopleName(self).text
            self.assertEqual(FollowId, PeopleId)
            self.assertEqual(FollowName, PeopleName)
            People.GetPeopleFollowed(self).click()
            People.GetPeopleBack(self).click()
            time.sleep(1)
            Follow.GetFollowBack(self).click()
        except:
            self.driver.save_screenshot('FollowSeekFriendError.png')
            raise

    def test_FollowSeekNotFollowFriend(self):
        FriendID = 148788
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFriendInto(self).click()
            time.sleep(5)
            Friend.GetFriendSeekFriendId(self).click()
            Friend.GetFriendSeekText(self).click()
            Friend.GetFriendSeekText(self).send_keys(148788)
            time.sleep(1)
            self.PressEnter()
            time.sleep(1)
            Friend.GetFriendSeekFriendFollow(self).click()
            time.sleep(1)
            self.PressBack()
            time.sleep(1)
            Friend.GetFriendSeekFriendId(self).click()
            Friend.GetFriendSeekText(self).click()
            Friend.GetFriendSeekText(self).send_keys(FriendID)
            time.sleep(1)
            self.PressEnter()
            time.sleep(1)
            Friend.GetFriendSeekFriendFollow(self).click()
            self.PressBack()
            time.sleep(1)
            Menu.GetMenuFriendBack(self).click()
            Tap.GetToMe(self).click()
            FollowNumber = Me.GetFollowNumber(self).text
            self.assertEqual(0, int(FollowNumber))
        except:
            self.driver.save_screenshot('FollowSeekNotFollowFriendError.png')
            raise

    def test_RecommendFriend(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFriendInto(self).click()
            time.sleep(5)
            FirstPeopleName = Friend.GetFriendFirstPeopleName(self).text
            SecondPeopleName = Friend.GetFriendSecondPeopleName(self).text
            ThirdPeopleName = Friend.GetFriendThirdPeopleName(self).text
            self.SwipeFriendLeft()
            self.SwipeFriendLeft()
            FourthPeopleName = Friend.GetFriendFourthPeopleName(self).text
            FifthPeopleName = Friend.GetFriendFifthPeopleName(self).text
            SixthPeopleName = Friend.GetFriendSixthPeopleName(self).text
            if FirstPeopleName != SecondPeopleName != ThirdPeopleName != FourthPeopleName != FifthPeopleName != \
                    SixthPeopleName:
                Menu.GetMenuFriendBack(self).click()
        except:
            self.driver.save_screenshot('RecommendFriendError.png')
            raise

    def test_SendToFriend(self):
        FriendID = 148788
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFriendInto(self).click()
            time.sleep(5)
            Friend.GetFriendSeekFriendId(self).click()
            Friend.GetFriendSeekText(self).click()
            Friend.GetFriendSeekText(self).send_keys(FriendID)
            time.sleep(1)
            self.PressEnter()
            time.sleep(1)
            Friend.GetFriendSeekFriendFollow(self).click()
            self.PressBack()
            time.sleep(1)
            Menu.GetMenuFriendBack(self).click()
            Tap.GetToMe(self).click()
            FollowNumber = Me.GetFollowNumber(self).text
            self.assertEqual(1, int(FollowNumber))
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToSendFriend(self).click()
            Data.GetDataSendToFriend(self).click()
            time.sleep(3)
            Data.GetDataSendMessageBack(self).click()
            Data.GetDataBack(self).click()
            Tap.GetToMe(self).click()
            FollowNumber = Me.GetFollowNumber(self).text
            self.assertEqual(1, int(FollowNumber))
            Follow.GetFollowInfo(self).click()
            time.sleep(2)
            FollowName = Follow.GetFollowFirstPeopleName(self).text
            FollowId = Follow.GetFollowFirstPeopleId(self).text
            Follow.GetFollowFirstPeopleInfo(self).click()
            time.sleep(2)
            PeopleId = People.GetPeopleId(self).text
            PeopleName = People.GetPeopleName(self).text
            self.assertEqual(FollowId, PeopleId)
            self.assertEqual(FollowName, PeopleName)
            People.GetPeopleFollowed(self).click()
            People.GetPeopleBack(self).click()
            time.sleep(1)
            Follow.GetFollowBack(self).click()
        except:
            self.driver.save_screenshot('SendToFriendError.png')
            raise

    def test_NoFriendSendToFriend(self):
        try:
            Tap.GetToMe(self).click()
            FollowNumber = Me.GetFollowNumber(self).text
            self.assertEqual(0, int(FollowNumber))
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToSendFriend(self).click()
            Data.GetDataMenuToSendFriendAddFriend(self).click()
            Friend.GetFriendUnderFirstPeopleFollowed(self).click()
            Menu.GetMenuFriendBack(self).click()
            Data.GetDataSendToFriend(self).click()
            time.sleep(3)
            Data.GetDataSendMessageBack(self).click()
            time.sleep(1)
            Data.GetDataBack(self).click()
            Tap.GetToMe(self).click()
            FollowedNumber = Me.GetFollowNumber(self).text
            self.assertEqual(1, int(FollowedNumber))
            Follow.GetFollowInfo(self).click()
            time.sleep(2)
            FollowName = Follow.GetFollowFirstPeopleName(self).text
            FollowId = Follow.GetFollowFirstPeopleId(self).text
            Follow.GetFollowFirstPeopleInfo(self).click()
            time.sleep(2)
            PeopleId = People.GetPeopleId(self).text
            PeopleName = People.GetPeopleName(self).text
            self.assertEqual(FollowId, PeopleId)
            self.assertEqual(FollowName, PeopleName)
            People.GetPeopleFollowed(self).click()
            People.GetPeopleBack(self).click()
            time.sleep(1)
            Follow.GetFollowBack(self).click()
        except:
            self.driver.save_screenshot('NoFriendSendToFriendError.png')
            raise

    def test_RefreshFriends(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFriendInto(self).click()
            time.sleep(3)
            FirstPeopleName = Friend.GetFriendUnderFirstPeopleName(self).text
            SecondPeopleName = Friend.GetFriendUnderSecondPeopleName(self).text
            Friend.GetFriendUnderPeopleChanged(self).click()
            ReFirstPeopleName = Friend.GetFriendUnderFirstPeopleName(self).text
            ReSecondPeopleName = Friend.GetFriendUnderSecondPeopleName(self).text
            self.assertNotEqual(FirstPeopleName, ReFirstPeopleName)
            self.assertNotEqual(SecondPeopleName, ReSecondPeopleName)
            Menu.GetMenuFriendBack(self).click()
        except:
            self.driver.save_screenshot('RefreshFriendsError.png')
            raise


if __name__ == '__main__':
    unittest.main()
