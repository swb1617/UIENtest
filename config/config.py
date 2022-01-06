
apk_path = "/Users/shiwenbin/Downloads/app-global-debug.apk"

desired_caps = {
        'platformName': 'Android',
        'platformVersion': '9',
        'deviceName': 'test01',
        # 国际版APP
        'noReset': False,
        'newCommandTimeout': 6000,
        # 更换底层驱动
        'automationName': 'UiAutomator2',
        'autoGrantPermissions': True
        # 'unicodeKeyboard': False,  # 修改手机的输入法
        # 'resetKeyboard': False
}