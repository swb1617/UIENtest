from selenium.webdriver.common.by import By


class Friend:
    def GetFriendFirstPeopleName(self):
        FriendFirstPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[2]")
        return FriendFirstPeopleName

    def GetFriendFirstPeopleDistance(self):
        FriendFirstPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[4]")
        return FriendFirstPeopleDistance

    def GetFriendFirstPeopleFollow(self):
        FriendFirstPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[6]/android.widget.Button")
        return FriendFirstPeopleFollow

    def GetFriendSecondPeopleName(self):
        FriendSecondPeopleName = self.driver.find_element(by=By.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[2]")
        return FriendSecondPeopleName

    def GetFriendSecondPeopleDistance(self):
        FriendSecondPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[4]")
        return FriendSecondPeopleDistance

    def GetFriendSecondPeopleFollow(self):
        FriendSecondPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[6]/android.widget.Button")
        return FriendSecondPeopleFollow

    def GetFriendThirdPeopleName(self):
        FriendThirdPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[2]")
        return FriendThirdPeopleName

    def GetFriendThirdPeopleDistance(self):
        FriendThirdPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[4]")
        return FriendThirdPeopleDistance

    def GetFriendThirdPeopleFollow(self):
        FriendThirdPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[6]/android.widget.Button")
        return FriendThirdPeopleFollow

    def GetFriendFourthPeopleName(self):
        FriendFourthPeopleName = self.driver.find_element(by=By.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[2]")
        return FriendFourthPeopleName

    def GetFriendFourthPeopleDistance(self):
        FriendFourthPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[4]")
        return FriendFourthPeopleDistance

    def GetFriendFourthPeopleFollow(self):
        FriendFourthPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[6]/android.widget.Button")
        return FriendFourthPeopleFollow

    def GetFriendFifthPeopleName(self):
        FriendFifthPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[2]")
        return FriendFifthPeopleName

    def GetFriendFifthPeopleDistance(self):
        FriendFifthPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[4]")
        return FriendFifthPeopleDistance

    def GetFriendFifthPeopleFollow(self):
        FriendFifthPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[6]/android.widget.Button")
        return FriendFifthPeopleFollow

    def GetFriendSixthPeopleName(self):
        FriendSixthPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[2]")
        return FriendSixthPeopleName

    def GetFriendSixthPeopleDistance(self):
        FriendSixthPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[4]")
        return FriendSixthPeopleDistance

    def GetFriendSixthPeopleFollow(self):
        FriendSixthPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[6]/android.widget.Button")
        return FriendSixthPeopleFollow

    def GetFriendSeekFriendId(self):
        FriendSeekFriendId = self.driver.find_element(by=By.XPATH,
                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]")
        return FriendSeekFriendId

    def GetFriendSeekText(self):
        FriendSeektext = self.driver.find_element(by=By.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
        return FriendSeektext

    def GetFriendSeekFriendFollow(self):
        FriendSeekFriendFollow = self.driver.find_element(by=By.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[6]/android.widget.Button")
        return FriendSeekFriendFollow

    def GetFriendUnderFirstPeopleName(self):
        FriendUnderFirstPeopleName = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[2]")
        return FriendUnderFirstPeopleName

    def GetFriendUnderFirstPeopleDistance(self):
        FriendUnderFristPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[4]")
        return FriendUnderFristPeopleDistance

    def GetFriendUnderFirstPeopleFollowed(self):
        FriendUnderFirstPeopleFollowed = self.driver.find_element(by=By.XPATH,
                                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[6]/android.widget.Button")
        return FriendUnderFirstPeopleFollowed

    def GetFriendUnderSecondPeopleName(self):
        FriendUnderSecondPeopleName = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[8]")
        return FriendUnderSecondPeopleName

    def GetFriendUnderSecondPeopleDistance(self):
        FriendUnderSecondPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[10]")
        return FriendUnderSecondPeopleDistance

    def GetFriendUnderSecondPeopleFollowed(self):
        FriendUnderSecondPeopleFollowed = self.driver.find_element(by=By.XPATH,
                                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[12]/android.widget.Button")
        return FriendUnderSecondPeopleFollowed

    def GetFriendUnderPeopleChanged(self):
        FriendUnderPeopleChanged = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[7]/android.widget.Button")
        return FriendUnderPeopleChanged