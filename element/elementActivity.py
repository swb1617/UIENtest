from selenium.webdriver.common.by import By

from common.packageparse import get_apkname
from config.config import apk_path


class Activity:
    def GetActivityTotalFrequency(self):
        ActivityTotalFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "2]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.TextView[1]")
        return ActivityTotalFrequency

    def GetActivityTotalDuration(self):
        ActivityTotalDuration = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "2]/android.widget.LinearLayout["
                                                                            "2]/android.widget.LinearLayout["
                                                                            "1]/android.widget.TextView[1]")
        return ActivityTotalDuration

    def GetActivityTotalAverageVelocity(self):
        ActivityTotalAverageVelocity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "2]/android.widget.LinearLayout["
                                                                                   "3]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.TextView[1]")
        return ActivityTotalAverageVelocity

    def GetActivityMonthFrequency(self):
        ActivityMonthFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "2]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.TextView[3]")
        return ActivityMonthFrequency

    def GetActivityTotalDistance(self):  # 活动界面总计里程
        ActivityTotalDistance = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.TextView[1]")
        return ActivityTotalDistance

    def GetActivityCalendarInfo(self):  # 活动界面日历入口
        ActivityCalendarInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return ActivityCalendarInfo

    def GetActivityShareInfo(self):  # 活动界面分享入口
        ActivityShareInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[2]")
        return ActivityShareInfo

    def GetActivityDataStatisticInfo(self):  # 活动界面数据管理入口
        ActivityDataStatisticInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "3]/android.widget.LinearLayout[1]")
        return ActivityDataStatisticInfo

    def GetActivityDataStatisticBack(self):  # 活动界面数据管理入口
        ActivityDataStatisticBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.RelativeLayout["
                                                                                "1]/android.widget.LinearLayout[1]")
        return ActivityDataStatisticBack

    def GetActivityDataStatisticWeek(self):
        ActivityDataStatisticWeek = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.ScrollView["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.Button[1]")
        return ActivityDataStatisticWeek

    def GetActivityDataStatisticMonth(self):
        ActivityDataStatisticMonth = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.ScrollView["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "2]/android.widget.Button[1]")
        return ActivityDataStatisticMonth

    def GetActivityDataStatisticYear(self):
        ActivityDataStatisticYear = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.ScrollView["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "3]/android.widget.Button[1]")
        return ActivityDataStatisticYear

    def GetActivityDataStatisticAll(self):
        ActivityDataStatisticAll = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.ScrollView["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "4]/android.widget.Button[1]")
        return ActivityDataStatisticAll

    def GetActivityDataStatisticAllDistances(self):
        ActivityDataStatisticAllDistances = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget"
                                                                                        ".FrameLayout["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget"
                                                                                        ".FrameLayout["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget.ScrollView["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "3]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget.TextView[1]")
        return ActivityDataStatisticAllDistances

    def GetActivityDataStatisticAllFrequency(self):
        ActivityDataStatisticAllFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget"
                                                                                        ".FrameLayout["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget"
                                                                                        ".FrameLayout["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget.ScrollView["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "3]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "2]/android.widget"
                                                                                        ".LinearLayout["
                                                                                        "1]/android.widget.TextView[2]")
        return ActivityDataStatisticAllFrequency

    def GetActivityDataStatisticAllDuration(self):
        ActivityDataStatisticAllDuration = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.ScrollView["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "3]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "2]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "2]/android.widget.TextView[2]")
        return ActivityDataStatisticAllDuration

    def GetActivityDataStatisticAllAverageVelocity(self):
        ActivityDataStatisticAllAverageVelocity = self.driver.find_element(by=By.XPATH, value="//android.widget"
                                                                                              ".FrameLayout["
                                                                                              "1]/android.widget"
                                                                                              ".LinearLayout["
                                                                                              "1]/android.widget"
                                                                                              ".FrameLayout["
                                                                                              "1]/android.widget"
                                                                                              ".LinearLayout["
                                                                                              "1]/android.widget"
                                                                                              ".FrameLayout["
                                                                                              "1]/android.widget"
                                                                                              ".LinearLayout["
                                                                                              "1]/android.widget"
                                                                                              ".ScrollView["
                                                                                              "1]/android.widget"
                                                                                              ".LinearLayout["
                                                                                              "1]/android.widget"
                                                                                              ".LinearLayout["
                                                                                              "3]/android.widget"
                                                                                              ".LinearLayout["
                                                                                              "2]/android.widget"
                                                                                              ".LinearLayout["
                                                                                              "3]/android.widget"
                                                                                              ".LinearLayout["
                                                                                              "1]/android.widget"
                                                                                              ".TextView[1]")
        return ActivityDataStatisticAllAverageVelocity

    def GetActivityDataStatisticMonthFrequency(self):
        ActivityDataStatisticMonthFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget"
                                                                                          ".FrameLayout["
                                                                                          "1]/android.widget"
                                                                                          ".LinearLayout["
                                                                                          "1]/android.widget"
                                                                                          ".FrameLayout["
                                                                                          "1]/android.widget"
                                                                                          ".LinearLayout["
                                                                                          "1]/android.widget"
                                                                                          ".FrameLayout["
                                                                                          "1]/android.widget"
                                                                                          ".LinearLayout["
                                                                                          "1]/android.widget"
                                                                                          ".ScrollView["
                                                                                          "1]/android.widget"
                                                                                          ".LinearLayout["
                                                                                          "1]/android.widget"
                                                                                          ".LinearLayout["
                                                                                          "3]/android.widget"
                                                                                          ".LinearLayout["
                                                                                          "2]/android.widget"
                                                                                          ".LinearLayout["
                                                                                          "1]/android.widget.TextView["
                                                                                          "2]")
        return ActivityDataStatisticMonthFrequency

    def GetActivityPersonalRecordsInfo(self):  # 活动界面个人记录入口
        ActivityPersonalRecordsInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "3]/android.widget.LinearLayout[2]")
        return ActivityPersonalRecordsInfo

    def GetActivityCalendarBack(self):  # 日历界面返回
        ActivityCalendarBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return ActivityCalendarBack

    def GetActivityCalendarGoalsEdit(self):  # 编辑月骑行目标按钮
        ActivityCalendarGoalsEdit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.RelativeLayout["
                                                                                "1]/android.widget.RelativeLayout["
                                                                                "1]/android.widget.RelativeLayout[1]")
        return ActivityCalendarGoalsEdit

    def GetActivityCalendarGoalsEditText(self):  # 骑行目标输入框
        ActivityCalendarGoalsEditText = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id/et_goal")
        return ActivityCalendarGoalsEditText

    def GetActivityCalendarGoalsEditSave(self):  # 骑行目标保存
        ActivityCalendarGoalsEditSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                    "1]/android.widget.FrameLayout["
                                                                                    "1]/android.widget.FrameLayout["
                                                                                    "1]/android.widget.RelativeLayout["
                                                                                    "1]/android.widget.Button[1]")
        return ActivityCalendarGoalsEditSave

    def GetActivityShareBack(self):  # 活动界面分享返回
        ActivityShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return ActivityShareBack

    def GetActivityShareSave(self):  # 活动界面分享保存
        ActivityShareSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return ActivityShareSave

    def GetActivityPersonalRecordsBack(self):  # 个人纪录返回
        ActivityPersonalRecordsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.RelativeLayout["
                                                                                  "1]/android.widget.LinearLayout[1]")
        return ActivityPersonalRecordsBack

    def GetActivityPersonalRecordsShare(self):  # 个人记录分享
        ActivityPersonalRecordsShare = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.RelativeLayout["
                                                                                   "1]/android.widget.RelativeLayout["
                                                                                   "1]")
        return ActivityPersonalRecordsShare

    def GetActivityPersonalRecordsShareBack(self):  # 个人记录分享返回
        ActivityPersonalRecordsShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".RelativeLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout[1]")
        return ActivityPersonalRecordsShareBack
