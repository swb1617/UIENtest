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

    def GetActivityTotalDistance(self):  # ????????????????????????
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

    def GetActivityCalendarInfo(self):  # ????????????????????????
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

    def GetActivityShareInfo(self):  # ????????????????????????
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

    def GetActivityDataStatisticInfo(self):  # ??????????????????????????????
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

    def GetActivityDataStatisticBack(self):  # ??????????????????????????????
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

    def GetActivityPersonalRecordsInfo(self):  # ??????????????????????????????
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

    def GetActivityCalendarBack(self):  # ??????????????????
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

    def GetActivityCalendarGoalsEdit(self):  # ???????????????????????????
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

    def GetActivityCalendarGoalsEditText(self):  # ?????????????????????
        ActivityCalendarGoalsEditText = self.driver.find_element(by=By.ID, value=get_apkname(apk_path)+":id/et_goal")
        return ActivityCalendarGoalsEditText

    def GetActivityCalendarGoalsEditSave(self):  # ??????????????????
        ActivityCalendarGoalsEditSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                    "1]/android.widget.FrameLayout["
                                                                                    "1]/android.widget.FrameLayout["
                                                                                    "1]/android.widget.RelativeLayout["
                                                                                    "1]/android.widget.Button[1]")
        return ActivityCalendarGoalsEditSave

    def GetActivityShareBack(self):  # ????????????????????????
        ActivityShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return ActivityShareBack

    def GetActivityShareSave(self):  # ????????????????????????
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

    def GetActivityPersonalRecordsBack(self):  # ??????????????????
        ActivityPersonalRecordsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.RelativeLayout["
                                                                                  "1]/android.widget.LinearLayout[1]")
        return ActivityPersonalRecordsBack

    def GetActivityPersonalRecordsShare(self):  # ??????????????????
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

    def GetActivityPersonalRecordsShareBack(self):  # ????????????????????????
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
