"""
user:石文斌
time：2022/01/05

"""

import time
import unittest

from appium import webdriver

from config.config import desired_caps
from element.elementData import Data
from element.button import Tap
from element.elementMenu import Menu
from element.elementFriend import Friend
from element.elementFollow import Follow
from element.elementPeople import People
from element.elementMe import Me
from common.tool import Tool


class TestData(unittest.TestCase):

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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
            raise

    @unittest.skip
    def test_ExportDataFit(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToExportFile(self).click()
            Tool.AgreeJurisdiction(self)
            Data.GetDataExportDataFit(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataFitError.png')
            Tool.ReStartApp(self)
            raise

    @unittest.skip
    def test_ExportDataGpx(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Tool.AgreeJurisdiction(self)
            Data.GetDataMenuToExportFile(self).click()
            Data.GetDataExportDataGpx(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataGpxError.png')
            Tool.ReStartApp(self)
            raise

    @unittest.skip
    def test_ExportDataTcx(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Tool.AgreeJurisdiction(self)
            Data.GetDataMenuToExportFile(self).click()
            Data.GetDataExportDataTcx(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataTcxError.png')
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
            raise

    def test_ShareWatermarkData(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            Tool.AgreeJurisdiction(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.PressEnter(self)
            time.sleep(1)
            Friend.GetFriendSeekFriendFollow(self).click()
            Tool.PressBack(self)
            time.sleep(1)
            Menu.GetMenuFriendBack(self).click()
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
            raise


if __name__ == '__main__':
    unittest.main()
