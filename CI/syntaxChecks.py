import os
import py_compile
import unittest

class TestSyntax(unittest.TestCase):

    def __init__(self,scriptToCheck):
        super(TestSyntax,self).__init__()
        self.scriptToCheck = scriptToCheck

    def runTest(self):
        # print(self.scriptToCheck)
        try:
            compile(open(self.scriptToCheck, 'r').read(), self.scriptToCheck, 'exec')
            passed = True
        except:
            passed = False
        self.failIf(not passed,"Failed compiling {}".format(self.scriptToCheck))
        if passed == False:
            sys.exit(1)

def suite():
    testsSuite = unittest.TestSuite()
    for root, dirs, filenames in os.walk("../"):
        for file in filenames:
            if file[-3:] == ".py":
                scriptToCheck = root+'/'+file
                testsSuite.addTest(TestSyntax(scriptToCheck))
    return testsSuite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    #test_suite = suite()
    runner.run(suite())