import unittest
import babysitter

class TestBabysitter(unittest.TestCase):

	def test_startTest(self):
		self.assertEqual(babysitter.startTest('4:59pm'), False)
		self.assertEqual(babysitter.startTest('5:00pm'), True)
		self.assertEqual(babysitter.startTest('12:59am'), True)
		self.assertEqual(babysitter.startTest('12:33pm'), False)
		self.assertEqual(babysitter.startTest('4:18am'), False)
		self.assertEqual(babysitter.startTest('6:4pm'), False)