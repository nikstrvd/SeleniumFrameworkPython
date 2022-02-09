# 1. Import the files
import unittest
from Tests.test_LoginDemo import LoginPageDemoTest


# 2. Create the object of the class using unitTest
lp = unittest.TestLoader().loadTestsFromTestCase(LoginPageDemoTest)


# 3. Create TestSuite
regressionTest = unittest.TestSuite([lp])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

# Note : All the methods in test files should define in proper run order
