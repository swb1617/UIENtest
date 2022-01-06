"""
user:石文斌
time：2022/01/05

"""
import time
import unittest

from appium import webdriver

from config.config import desired_caps
from element.button import Tap
from element.elementMenu import Menu
from element.elementMessage import Message
from element.elementMe import Me
from element.elementTraining import Training
from common.tool import Tool


class TestMenu(unittest.TestCase):

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

    def test_MenuMessage(self):  # 主页消息界面
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuMessageInto(self).click()
            Message.GetMessageRead(self).click()
            Message.GetMeaagaeBack(self).click()
        except:
            self.driver.save_screenshot('MenuMessageError.png')
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
            raise

    def test_MenuFirstTraining(self):
        try:
            Tap.GetToHome(self).click()
            Tool.SwipeUp(self)
            MenuFirstTraining = Menu.GetMenuFirstTrainingName(self).text
            self.assertTrue(MenuFirstTraining)
        except:
            self.driver.save_screenshot('MenuFirstTrainingError.png')
            Tool.ReStartApp(self)
            raise

    def test_ToRecommendTraining(self):
        try:
            Tap.GetToHome(self).click()
            Tool.SwipeUp(self)
            Menu.GetMenuMoreTraining(self).click()
            Training.GetTrainingRecommendTrainingTap(self).click()
            Training.GetTrainingRecommendFirstTrainingName(self).click()
            time.sleep(2)
            Training.GetTrainingDetailsBack(self).click()
            TrainingName = Training.GetTrainingRecommendFirstTrainingName(self).text
            print(TrainingName)
            Menu.GetMenuMoreTrainingBack(self).click()
        except:
            self.driver.save_screenshot('ToRecommendTrainingError.png')
            Tool.ReStartApp(self)
            raise

    def test_MenuToMoreTraining(self):
        try:
            Tap.GetToHome(self).click()
            Tool.SwipeUp(self)
            Menu.GetMenuMoreTraining(self).click()
            TrainingName = Training.GetTrainingRecommendFirstTrainingName(self).text
            print(TrainingName)
            Menu.GetMenuMoreTrainingBack(self).click()
        except:
            self.driver.save_screenshot('MenuToMoreTrainingError.png')
            Tool.ReStartApp(self)
            raise

    def test_MenuToTrainingDetails(self):
        try:
            Tap.GetToHome(self).click()
            Tool.SwipeUp(self)
            Menu.GetMenuMoreTraining(self).click()
            Training.GetTrainingDiyTrainingTap(self).click()
            Training.GetTrainingAddTraining(self).click()
            Training.GetTrainingAddStep(self).click()
            Training.GetTrainingAddStep(self).click()
            Training.GetTrainingAddRepeat(self).click()
            Training.GetTrainingAddSave(self).click()
            time.sleep(3)
            Training.GetTrainingDetailsBack(self).click()
            Menu.GetMenuMoreTrainingBack(self).click()
        except:
            self.driver.save_screenshot('MenuToTrainingDetails.png')
            Tool.ReStartApp(self)
            raise


if __name__ == '__main__':
    unittest.main()
