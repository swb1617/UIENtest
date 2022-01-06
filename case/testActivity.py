"""
user:石文斌
time：2022/01/05

"""
import time
import unittest

from appium import webdriver

from config.config import desired_caps
from element.elementActivity import Activity
from element.button import Tap
from common.tool import Tool


class TestActivity(unittest.TestCase):

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

    def test_Calendar(self):  # 日历界面
        try:
            Tap.GetToActivity(self).click()
            time.sleep(1)
            Activity.GetActivityCalendarInfo(self).click()
            time.sleep(2)
            Activity.GetActivityCalendarBack(self).click()
        except:
            self.driver.save_screenshot('CalendarError.png')
            Tool.ReStartApp(self)
            raise

    def test_ActivityShare(self):  # 活动分享
        try:
            Tap.GetToActivity(self).click()
            Activity.GetActivityShareInfo(self).click()
            Tool.AgreeJurisdiction(self)
            time.sleep(1)
            Activity.GetActivityShareSave(self).click()
            Activity.GetActivityShareBack(self).click()
        except:
            self.driver.save_screenshot('ActivityShareError.png')
            Tool.ReStartApp(self)
            raise

    def test_StatisticData(self):  # 数据管理界面
        try:
            Tap.GetToActivity(self).click()
            Activity.GetActivityDataStatisticInfo(self).click()
            time.sleep(1)
            Activity.GetActivityDataStatisticBack(self).click()
        except:
            self.driver.save_screenshot('StatisticDataError.png')
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
            raise


if __name__ == '__main__':
    unittest.main()
