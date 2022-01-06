"""
user:石文斌
time：2022/01/05

"""
import time
import unittest

from appium import webdriver

from element.button import Tap
from element.elementMe import Me
from common.tool import Tool
from config.config import desired_caps


class TestMe(unittest.TestCase):

    def setUp(self) -> None:  # 执行方法前准备工作
        self.driver.implicitly_wait(20)  # 稳定元素

    def tearDown(self) -> None:  # 执行方法后工作
        # print("...........结束..............")
        time.sleep(3)

    @classmethod
    def setUpClass(cls) -> None:
        cls.parme = {"port": 4723}
        cls.driver = webdriver.Remote('http://localhost:%s/wd/hub' % str(cls.parme['port']), desired_caps)
        Tool.StartApp(cls)

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
            time.sleep(2)
            Tool.AgreeJurisdiction(self)
            time.sleep(2)
            Tool.AgreeJurisdiction(self)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(3)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack1Error.png')
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
                Tool.SwipeLittleUp(self)
                Me.GetMeUserSexSave(self).click()
                Me.GetMeUserDetailsBack(self).click()
                Tap.GetToMe(self).click()
                Me.GetMEUserDetailsInfo(self).click()
                Sex = Me.GetMeUserSex(self).text
                Me.GetMeUserDetailsBack(self).click()
                self.assertNotEqual(Sex, UserSex)
            else:
                Me.GetMeUserSexInfo(self).click()
                Tool.SwipeLittleDown(self)
                Me.GetMeUserSexSave(self).click()
                Me.GetMeUserDetailsBack(self).click()
                Tap.GetToMe(self).click()
                Me.GetMEUserDetailsInfo(self).click()
                Sex = Me.GetMeUserSex(self).text
                Me.GetMeUserDetailsBack(self).click()
                self.assertNotEqual(Sex, UserSex)
        except:
            self.driver.save_screenshot('SexChangeError.png')
            Tool.ReStartApp(self)
            raise

    @unittest.skip
    def test_LanguageChange(self):  # 切换语言
        try:
            Tap.GetToMe(self).click()
            Me.GetMeAccountSettingInfo(self).click()
            time.sleep(3)
            Me.GetMeLanguageSetting(self).click()
            time.sleep(2)
            Tool.SwipeLittleUp(self)
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
            Tool.ReStartApp(self)
            raise

    def test_MeNotification(self):  # 消息设置界面
        try:
            Tap.GetToMe(self).click()
            Me.GetMeNotification(self).click()
            time.sleep(3)
            Me.GetMeNotificationBack(self).click()
        except:
            self.driver.save_screenshot('MeNotificationError.png')
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
            raise

    def test_RankInfo(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMeRidingRankInfo(self).click()
            time.sleep(3)
            Me.GetMeRidingRankBack(self).click()
        except:
            self.driver.save_screenshot('RankInfoError.png')
            Tool.ReStartApp(self)
            raise

    def test_RankDetails(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMeRidingRankInfo(self).click()
            time.sleep(3)
            RankTitle = Me.GetMeRankTitle(self).text
            self.assertTrue(RankTitle)
            Me.GetMeRidingRankBack(self).click()
        except:
            self.driver.save_screenshot('RankDetailsError.png')
            Tool.ReStartApp(self)
            raise

    def test_MyEquipmentInfo(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMeMyEquipmentInfo(self).click()
            time.sleep(3)
            Me.GetMeMyEquipmentBack(self).click()
        except:
            self.driver.save_screenshot('MyEquipmentInfoError.png')
            Tool.ReStartApp(self)
            raise

    def test_MyEquipmentAddInfo(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMeMyEquipmentInfo(self).click()
            NoBikeMessage0 = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            # print(NoBikeMessage0)
            self.assertTrue(NoBikeMessage0)
            Me.GetMeMyEquipmentAddBike(self).click()
            time.sleep(2)
            Me.GetMeMyEquipmentAddBikeBack(self).click()
            time.sleep(2)
            NoBikeMessage0 = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            print(NoBikeMessage0)
            Me.GetMeMyEquipmentFirstAddBike(self).click()
            time.sleep(2)
            Me.GetMeMyEquipmentAddBikeBack(self).click()
            time.sleep(2)
            NoBikeMessage1 = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            print(NoBikeMessage1)
            self.assertEqual(NoBikeMessage1, NoBikeMessage0)
            time.sleep(2)
            Me.GetMeMyEquipmentBack(self).click()
        except:
            self.driver.save_screenshot('MyEquipmentAddInfoError.png')
            Tool.ReStartApp(self)
            raise

    def test_MyEquipmentAddBike1(self):
        try:
            MyEquipmentName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeMyEquipmentInfo(self).click()
            NoBikeMessage = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            print(NoBikeMessage)
            self.assertTrue(NoBikeMessage)
            Me.GetMeMyEquipmentFirstAddBike(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameInfo(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameEdit(self).click()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).send_keys(MyEquipmentName)
            Me.GetMeMyEquipmentAddBikeNameEditSave(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceInfo(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).send_keys(666)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceSave(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            Name = Me.GetMeMyEquipmentName(self).text
            self.assertEqual(MyEquipmentName, Name)
            Me.GetMeMyEquipmentEditInfo(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            time.sleep(3)
            Me.GetMeMyEquipmentBack(self).click()
        except:
            self.driver.save_screenshot('MyEquipmentAddBike1Error.png')
            Tool.ReStartApp(self)
            raise

    def test_MyEquipmentRetireBike(self):
        try:
            MyEquipmentName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeMyEquipmentInfo(self).click()
            NoBikeMessage = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            print(NoBikeMessage)
            self.assertTrue(NoBikeMessage)
            Me.GetMeMyEquipmentFirstAddBike(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameInfo(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameEdit(self).click()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).send_keys(MyEquipmentName)
            Me.GetMeMyEquipmentAddBikeNameEditSave(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceInfo(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).send_keys(666)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceSave(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            Name = Me.GetMeMyEquipmentName(self).text
            self.assertEqual(MyEquipmentName, Name)
            Me.GetMeMyEquipmentBack(self).click()
            Tap.GetToMe(self).click()
            Me.GetMeMyEquipmentInfo(self).click()
            Me.GetMeMyEquipmentAddBike(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameInfo(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameEdit(self).click()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).send_keys(MyEquipmentName)
            Me.GetMeMyEquipmentAddBikeNameEditSave(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceInfo(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).send_keys(666)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceSave(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            Name = Me.GetMeMyEquipmentName(self).text
            self.assertEqual(MyEquipmentName, Name)
            for i in range(0, 2):
                Me.GetMeMyEquipmentEditInfo(self).click()
                time.sleep(1)
                Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
                time.sleep(2)
            time.sleep(3)
            NoBikeMessage = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            print(NoBikeMessage)
            self.assertTrue(NoBikeMessage)
            Me.GetMeMyEquipmentBack(self).click()
        except:
            self.driver.save_screenshot('MyEquipmentRetireBikeError.png')
            Tool.ReStartApp(self)
            raise

    def test_MyEquipmentAddBike2(self):
        try:
            MyEquipmentName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeMyEquipmentInfo(self).click()
            NoBikeMessage = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            print(NoBikeMessage)
            self.assertTrue(NoBikeMessage)
            Me.GetMeMyEquipmentAddBike(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameInfo(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameEdit(self).click()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).send_keys(MyEquipmentName)
            Me.GetMeMyEquipmentAddBikeNameEditSave(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceInfo(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).send_keys(666)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceSave(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            Name = Me.GetMeMyEquipmentName(self).text
            self.assertEqual(MyEquipmentName, Name)
            Me.GetMeMyEquipmentEditInfo(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            time.sleep(3)
            Me.GetMeMyEquipmentBack(self).click()
        except:
            self.driver.save_screenshot('MyEquipmentAddBike2Error.png')
            Tool.ReStartApp(self)
            raise

    def test_MyEquipmentCloseBike(self):
        try:
            MyEquipmentName = 'Close'
            Tap.GetToMe(self).click()
            Me.GetMeMyEquipmentInfo(self).click()
            NoBikeMessage = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            print(NoBikeMessage)
            self.assertTrue(NoBikeMessage)
            Me.GetMeMyEquipmentAddBike(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameInfo(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameEdit(self).click()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).send_keys(MyEquipmentName)
            Me.GetMeMyEquipmentAddBikeNameEditSave(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceInfo(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).send_keys(666)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceSave(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            Name = Me.GetMeMyEquipmentName(self).text
            self.assertEqual(MyEquipmentName, Name)
            Me.GetMeMyEquipmentOpenOrClose(self).click()
            time.sleep(3)
            Me.GetMeMyEquipmentOpenOrClose(self).click()
            time.sleep(3)
            Me.GetMeMyEquipmentEditInfo(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            time.sleep(3)
            Me.GetMeMyEquipmentBack(self).click()
        except:
            self.driver.save_screenshot('MyEquipmentCloseBikeError.png')
            Tool.ReStartApp(self)
            raise

    def test_MyEquipmentOpenBike(self):
        try:
            MyEquipmentName = 'Open'
            Tap.GetToMe(self).click()
            Me.GetMeMyEquipmentInfo(self).click()
            NoBikeMessage = Me.GetMeMyEquipmentNoAddBikeMessage(self).text
            print(NoBikeMessage)
            self.assertTrue(NoBikeMessage)
            Me.GetMeMyEquipmentAddBike(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameInfo(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeNameEdit(self).click()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeNameEdit(self).send_keys(MyEquipmentName)
            Me.GetMeMyEquipmentAddBikeNameEditSave(self).click()
            time.sleep(1)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceInfo(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).click()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).clear()
            Me.GetMeMyEquipmentAddBikeFarthestDistanceEdit(self).send_keys(666)
            Me.GetMeMyEquipmentAddBikeFarthestDistanceSave(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            Name = Me.GetMeMyEquipmentName(self).text
            self.assertEqual(MyEquipmentName, Name)
            Me.GetMeMyEquipmentOpenOrClose(self).click()
            time.sleep(3)
            Me.GetMeMyEquipmentEditInfo(self).click()
            Me.GetMeMyEquipmentAddBikeSaveOrRetire(self).click()
            time.sleep(3)
            Me.GetMeMyEquipmentBack(self).click()
        except:
            self.driver.save_screenshot('MyEquipmentOpemBikeError.png')
            Tool.ReStartApp(self)
            raise


if __name__ == '__main__':
    unittest.main()
