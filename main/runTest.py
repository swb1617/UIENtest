# 导包
import unittest

from unittestreport import TestRunner
# from Ui.TestUi import TestUI
from case.testMe import TestMe
from case.testFriend import TestFriend
from case.testActivity import TestActivity
from case.testMenu import TestMenu
from case.testData import TestData
from case.testLogin import TestLogin


# 构建测试集
def suite():

    # 创建一个测试套件
    suites = unittest.TestSuite()
    # 将测试用例加载到测试套件中
    loader = unittest.TestLoader()  # 创建一个用例加载对象
    # suites.addTest(loader.loadTestsFromTestCase(TestUI))
    suites.addTest(loader.loadTestsFromTestCase(TestLogin))
    suites.addTest(loader.loadTestsFromTestCase(TestMe))
    suites.addTest(loader.loadTestsFromTestCase(TestFriend))
    suites.addTest(loader.loadTestsFromTestCase(TestActivity))
    suites.addTest(loader.loadTestsFromTestCase(TestMenu))
    suites.addTest(loader.loadTestsFromTestCase(TestData))
    return suites


if __name__ == '__main__':
    report = TestRunner(suite())
    report.run()
