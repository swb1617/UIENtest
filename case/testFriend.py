"""
user:石文斌
time：2022/01/05

"""
import time
import unittest

from appium import webdriver

from config.config import desired_caps
from element.elementMe import Me
from element.button import Tap
from element.elementMenu import Menu
from element.elementFriend import Friend
from element.elementFollow import Follow
from element.elementPeople import People
from common.tool import Tool


class TestFriend(unittest.TestCase):

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

    def NumberOfFriendsAsserted(self, Number):  # 断言好友数量
        FollowNumber = Me.GetFollowNumber(self).text
        self.assertEqual(Number, int(FollowNumber))

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
            self.NumberOfFriendsAsserted(1)
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
            Tool.ReStartApp(self)
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
            Tool.PressEnter(self)
            time.sleep(1)
            Friend.GetFriendSeekFriendFollow(self).click()
            Tool.PressBack(self)
            time.sleep(1)
            Menu.GetMenuFriendBack(self).click()
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
            self.driver.save_screenshot('FollowSeekFriendError.png')
            Tool.ReStartApp(self)
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
            Tool.PressEnter(self)
            time.sleep(1)
            Friend.GetFriendSeekFriendFollow(self).click()
            time.sleep(1)
            Tool.PressBack(self)
            time.sleep(1)
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
        except:
            self.driver.save_screenshot('FollowSeekNotFollowFriendError.png')
            Tool.ReStartApp(self)
            raise

    def test_RecommendFriend(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFriendInto(self).click()
            time.sleep(5)
            FirstPeopleName = Friend.GetFriendFirstPeopleName(self).text
            SecondPeopleName = Friend.GetFriendSecondPeopleName(self).text
            ThirdPeopleName = Friend.GetFriendThirdPeopleName(self).text
            Tool.SwipeFriendLeft(self)
            Tool.SwipeFriendLeft(self)
            FourthPeopleName = Friend.GetFriendFourthPeopleName(self).text
            FifthPeopleName = Friend.GetFriendFifthPeopleName(self).text
            SixthPeopleName = Friend.GetFriendSixthPeopleName(self).text
            if FirstPeopleName != SecondPeopleName != ThirdPeopleName != FourthPeopleName != FifthPeopleName != \
                    SixthPeopleName:
                Menu.GetMenuFriendBack(self).click()
        except:
            self.driver.save_screenshot('RecommendFriendError.png')
            Tool.ReStartApp(self)
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
            Tool.ReStartApp(self)
            raise


if __name__ == '__main__':
    unittest.main()
