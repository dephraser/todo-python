import unittest

suite = unittest.TestSuite()

from unit import taskTest
suite.addTest(taskTest.suite())

from unit import listTest
suite.addTest(listTest.suite())

unittest.TextTestRunner(verbosity=2).run(suite)
