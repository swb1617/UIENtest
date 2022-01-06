from selenium.webdriver.common.by import By


class Message:
    def GetMeaagaeBack(self):  # 消息页返回按钮
        MessageBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.widget.LinearLayout[1]")
        return MessageBack

    def GetMessageRead(self):  # 信息已读按钮
        MessageRead = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.widget.RelativeLayout[1]")
        return MessageRead
