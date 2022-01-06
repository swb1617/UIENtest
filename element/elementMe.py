from selenium.webdriver.common.by import By

from common.packageparse import get_apkname
from config.config import apk_path


class Me:
    def GetMeUserName(self):
        MeUserName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.TextView[1]")
        return MeUserName

    def GetMeUserId(self):
        MeUserId = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.view.ViewGroup[ "
                                                               "1]/android.widget.ScrollView["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.TextView[2]")
        return MeUserId

    def GetFollowNumber(self):
        FollowNumber = self.driver.find_element(by=By.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout["
                                                      "1]/android.widget.LinearLayout/android.widget.FrameLayout"
                                                      "/android.view.ViewGroup/android.widget.ScrollView/android"
                                                      ".widget.LinearLayout/android.widget.LinearLayout["
                                                      "1]/android.widget.RelativeLayout/android.widget.LinearLayout"
                                                      "/android.widget.LinearLayout[2]/android.widget.LinearLayout["
                                                      "1]/android.widget.TextView[2]")
        return FollowNumber

    def GetMEUserDetailsInfo(self):
        MeUserDetailsInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.view.ViewGroup["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return MeUserDetailsInfo

    def GetMeUserSex(self):
        MeUserSex = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.RelativeLayout["
                                                                "3]/android.widget.LinearLayout["
                                                                "1]/android.widget.TextView[1]")
        return MeUserSex

    def GetMeUserSexInfo(self):
        MeUserSexInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.ScrollView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout[3]")
        return MeUserSexInfo

    def GetMeUserSexSave(self):
        MeUserSexSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.Button[2]")
        return MeUserSexSave

    def GetMeSettingHRInfo(self):
        MeSettingHRInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.ScrollView["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout[8]")
        return MeSettingHRInfo

    def GetMeSettingHR(self):
        MeSettingHR = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "2]/android.widget.RelativeLayout["
                                                                  "2]/android.widget.Button[1]")
        return MeSettingHR

    def GetMeSettingHRBack(self):
        MeSettingHRBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout["
                                                                      "1]/android.widget.LinearLayout[1]")
        return MeSettingHRBack

    def GetMeSettingPowerInfo(self):
        MeSettingPowerInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.ScrollView["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout[9]")
        return MeSettingPowerInfo

    def GetMeSettingPower(self):
        MeSettingPower = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.RelativeLayout["
                                                                     "2]/android.widget.Button[1]")
        return MeSettingPower

    def GetMeSettingPowerBack(self):
        MeSettingPowerBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return MeSettingPowerBack

    def GetMeAccountSettingInfo(self):
        MeAccountSettingInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.view.ViewGroup["
                                                                           "1]/android.widget.ScrollView["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "3]/android.widget.RelativeLayout[2]")
        return MeAccountSettingInfo

    def GetMeLanguageMessage(self):
        MeLanguageMessage = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.TextView[2]")
        return MeLanguageMessage

    def GetMeRidingRankInfo(self):
        MeRidingRankInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "3]/android.widget.RelativeLayout[4]")
        return MeRidingRankInfo

    def GetMeRidingRankBack(self):
        MeRidingRankBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout[1]")
        return MeRidingRankBack

    def GetMeAfterSaleServiceInfo(self):
        MeAfterSaleServiceInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.view.ViewGroup["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "3]/android.widget.RelativeLayout[5]")
        return MeAfterSaleServiceInfo

    def GetMeNotification(self):
        MeNotification = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.view.ViewGroup["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "3]/android.widget.RelativeLayout[6]")
        return MeNotification

    def GetMeAboutUs(self):
        MeAboutUs = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "3]/android.widget.RelativeLayout[8]")
        return MeAboutUs

    def GetMeUserDetailsBack(self):
        MeUserDetailsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return MeUserDetailsBack

    def GetMeUserGoalsEdit(self):
        MeUserGoalsEdit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.ScrollView["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout[10]")
        return MeUserGoalsEdit

    def GetMeUserGoalsText(self):
        MeUserGoalsText = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id/et_goal")
        return MeUserGoalsText

    def GetMeUserGoalsSave(self):
        MeUserGoalsSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.RelativeLayout["
                                                                      "1]/android.widget.Button[1]")
        return MeUserGoalsSave

    def GetMeAboutUsBack(self):
        MeAboutUsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.ImageView[1]")
        return MeAboutUsBack

    def GetMeNotificationBack(self):
        MeNotificationBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return MeNotificationBack

    def GetMeAfterSaleServiceBack(self):
        MeAfterSaleServiceBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return MeAfterSaleServiceBack

    def GetMeAfterSaleServiceFeedBack(self):
        MeAfterSaleServiceFeedBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "1]/android.widget.RelativeLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.RelativeLayout[5]")
        return MeAfterSaleServiceFeedBack

    def GetMeFeedBackQuestionType(self):
        MeFeedBackQuestionType = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.TextView[2]")
        return MeFeedBackQuestionType

    def GetMeFeedBackQuestionList1(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[1]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList2(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[2]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList3(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[3]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList4(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[4]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList5(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[5]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList6(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[6]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList7(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[7]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList8(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[8]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList9(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[9]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionLista(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[10]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionListb(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[11]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionText(self):
        MeFeedBackQuestionText = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id/etProblem")
        return MeFeedBackQuestionText

    def GetMeFeedBackPictureAdd(self):
        MeFeddbackPictureAdd = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.ScrollView["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/androidx.recyclerview.widget"
                                                                           ".RecyclerView["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.ImageView[1]")
        return MeFeddbackPictureAdd

    def GetMeFeedBackPictureChoose(self):
        MeFeedBackPictureChoose = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.RelativeLayout["
                                                                              "1]/androidx.recyclerview.widget"
                                                                              ".RecyclerView["
                                                                              "1]/android.widget.RelativeLayout["
                                                                              "2]/android.widget.TextView[1]")
        return MeFeedBackPictureChoose

    def GetMeFeedBackPictureSave(self):
        MeFeedBackPictureSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.RelativeLayout["
                                                                            "1]/android.widget.RelativeLayout["
                                                                            "2]/android.widget.TextView[3]")
        return MeFeedBackPictureSave

    def GetMeFeedBackTLEText(self):
        MeFeedBackTLEText = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.EditText[2]")
        return MeFeedBackTLEText

    def GetMeFeedBackTitle(self):
        MeFeedBackTitle = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android"
                                                                      ".widget.LinearLayout/android.widget"
                                                                      ".FrameLayout/android.widget.LinearLayout"
                                                                      "/android.widget.FrameLayout/android.widget"
                                                                      ".LinearLayout/android.widget.RelativeLayout"
                                                                      "/android.widget.TextView")
        return MeFeedBackTitle

    def GetMeFeedBackSubmit(self):
        MeFeedBackSubmit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.Button[1]")
        return MeFeedBackSubmit

    def GetMeAccountSettingBack(self):
        MeAccountSettingBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return MeAccountSettingBack

    def GetMeAccountSettingSave(self):
        MeAccountSettingSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout[1]")
        return MeAccountSettingSave

    def GetMeLanguageSetting(self):
        MeLanguageSetting = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout[1]")
        return MeLanguageSetting

    def GetMeLanguageSettingSave(self):
        MeLanguageSettingSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.RelativeLayout["
                                                                            "1]/android.widget.Button[2]")
        return MeLanguageSettingSave

    def GetMeResetPasswordInfo(self):
        MeResetPasswordInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.RelativeLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.RelativeLayout[2]")
        return MeResetPasswordInfo

    def GetMeOldPasswordText(self):
        MeOldPasswordText = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id"
                                                                     "/edt_pwd_old_update_password")
        return MeOldPasswordText

    def GetMeNemPasswordText(self):
        MeNemPasswordText = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id"
                                                                     "/edt_pwd_new_update_password")
        return MeNemPasswordText

    def GetMeAgainNemPasswordText(self):
        MeAgainNemPasswordText = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id"
                                                                          "/edt_pwd_new2_update_password")
        return MeAgainNemPasswordText

    def GetMeConfirmPassword(self):
        MeConfirmPassword = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.Button[1]")
        return MeConfirmPassword

    def GetMeRankTitle(self):
        MeRankTitle = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
        return MeRankTitle

    def GetMeMyEquipmentInfo(self):
        MeMyEquipmentInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout[3]")
        return MeMyEquipmentInfo

    def GetMeMyEquipmentBack(self):
        MeMyEquipmentBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[1]")
        return MeMyEquipmentBack

    def GetMeMyEquipmentFirstAddBike(self):
        MeMyEquipmentFirstAddBike = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.Button")
        return MeMyEquipmentFirstAddBike

    def GetMeMyEquipmentNoAddBikeMessage(self):
        MeMyEquipmentNoAddBikeMessage = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]")
        return MeMyEquipmentNoAddBikeMessage

    def GetMeMyEquipmentAddBike(self):
        MeMyEquipmentAddBike = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[3]")
        return MeMyEquipmentAddBike

    def GetMeMyEquipmentAddBikeNameInfo(self):
        MeMyEquipmentAddBikeNameInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]")
        return MeMyEquipmentAddBikeNameInfo

    def GetMeMyEquipmentAddBikeBack(self):
        MeMyEquipmentAddBikeBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button")
        return MeMyEquipmentAddBikeBack

    def GetMeMyEquipmentAddBikeNameEdit(self):
        MeMyEquipmentAddBikeNameEdit = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.EditText")
        return MeMyEquipmentAddBikeNameEdit

    def GetMeMyEquipmentAddBikeNameEditSave(self):
        MeMyEquipmentAddBikeNameEditSave = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        return MeMyEquipmentAddBikeNameEditSave

    def GetMeMyEquipmentAddBikeWeightInfo(self):
        MeMyEquipmentAddBikeWeightInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]")
        return MeMyEquipmentAddBikeWeightInfo

    def GetMeMyEquipmentAddBikeWeightSave(self):
        MeMyEquipmentAddBikeWeightSave = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View[3]")
        return MeMyEquipmentAddBikeWeightSave

    def GetMeMyEquipmentAddBikeWheelDiameterInfo(self):
        MeMyEquipmentAddBikeWheelDiameterInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[4]")
        return MeMyEquipmentAddBikeWheelDiameterInfo

    def GetMeMyEquipmentAddBikeWheelDiameter935mm(self):
        MeMyEquipmentAddBikeWheelDiameter935mm = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View[2]")
        return MeMyEquipmentAddBikeWheelDiameter935mm

    def GetMeMyEquipmentAddBikeWheelDiameterDiy(self):
        MeMyEquipmentAddBikeWheelDiameterDiy = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View[1]")
        return MeMyEquipmentAddBikeWheelDiameterDiy

    def GetMeMyEquipmentAddBikeWheelDiameterDiyEdit(self):
        MeMyEquipmentAddBikeWheelDiameterDiyEdit = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.EditText")
        return MeMyEquipmentAddBikeWheelDiameterDiyEdit

    def GetMeMyEquipmentAddBikeWheelDiameterDiySave(self):
        MeMyEquipmentAddBikeWheelDiameterDiySave = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        return MeMyEquipmentAddBikeWheelDiameterDiySave

    def GetMeMyEquipmentAddBikeWheelDiameterBack(self):
        MeMyEquipmentAddBikeWheelDiameterBack = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[1]")
        return MeMyEquipmentAddBikeWheelDiameterBack

    def GetMeMyEquipmentAddBikeFarthestDistanceInfo(self):
        MeMyEquipmentAddBikeFarthestDistanceInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[6]")
        return MeMyEquipmentAddBikeFarthestDistanceInfo

    def GetMeMyEquipmentAddBikeFarthestDistanceEdit(self):
        MeMyEquipmentAddBikeFarthestDistanceEdit = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.EditText")
        return MeMyEquipmentAddBikeFarthestDistanceEdit

    def GetMeMyEquipmentAddBikeFarthestDistanceSave(self):
        MeMyEquipmentAddBikeFarthestDistanceSave = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        return MeMyEquipmentAddBikeFarthestDistanceSave

    def GetMeMyEquipmentAddBikeSaveOrRetire(self):
        MeMyEquipmentAddBikeSave = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.widget.Button")
        return MeMyEquipmentAddBikeSave

    def GetMeMyEquipmentOpenOrClose(self):
        MeMyEquipmentOpenOrClose = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.widget.Switch")
        return MeMyEquipmentOpenOrClose

    def GetMeMyEquipmentName(self):
        GetMeMyEquipmentName = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]")
        return GetMeMyEquipmentName

    def GetMeMyEquipmentDate(self):
        MeMyEquipmentDate = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]")
        return MeMyEquipmentDate

    def GetMeMyEquipmentFarthestDistance(self):
        MeMyEquipmentFarthestDistance = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[5]")
        return MeMyEquipmentFarthestDistance

    def GetMeMyEquipmentWheelDiameter(self):
        MeMyEquipmentWheelDiameter = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[9]")
        return MeMyEquipmentWheelDiameter

    def GetMeMyEquipmentWeight(self):
        MeMyEquipmentWeight = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[12]")
        return MeMyEquipmentWeight

    def GetMeMyEquipmentEditInfo(self):
        MeMyEquipmentEditInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[7]")
        return MeMyEquipmentEditInfo

    def GetMeMyEquipmentRetireTap(self):
        MeMyEquipmentRetireTap = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]")
        return MeMyEquipmentRetireTap

    def GetMeMyEquipmentRetireName(self):
        MeMyEquipmentRetireName = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]")
        return MeMyEquipmentRetireName

    def GetMeMyEquipmentRetireMenuInfo(self):
        MeMyEquipmentRetireMenuInfo = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[3]")
        return MeMyEquipmentRetireMenuInfo

    def GetMeMyEquipmentRetireMenuToComeback(self):
        MeMyEquipmentRetireMenuToComeback = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]")
        return MeMyEquipmentRetireMenuToComeback

    def GetMeMyEquipmentRetireMenuToDelete(self):
        MeMyEquipmentRetireMenuToDelete = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]")
        return MeMyEquipmentRetireMenuToDelete

    def GetMeMyEquipmentNumberOfAssociatedActivities(self):
        MeMyEquipmentNumberOfAssociatedActivities = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[3]")
        return MeMyEquipmentNumberOfAssociatedActivities










