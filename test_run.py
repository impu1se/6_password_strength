import unittest
import test_pass

test_pass_suite = unittest.TestSuite()
test_pass_suite.addTest(unittest.makeSuite(test_pass.FileTests))
test_pass_suite.addTest(unittest.makeSuite(test_pass.PasswordTests))
print('count of tests: ' + str(test_pass_suite.countTestCases()) + '\n')

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_pass_suite)