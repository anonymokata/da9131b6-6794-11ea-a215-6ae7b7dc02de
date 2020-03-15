import unittest
import babysitter

class TestBabysitter(unittest.TestCase):

	def test_timeTest(self):
		self.assertEqual(babysitter.timeTest('4:59pm'), False)
		self.assertEqual(babysitter.timeTest('5:00pm'), True)
		self.assertEqual(babysitter.timeTest('12:59am'), True)
		self.assertEqual(babysitter.timeTest('12:33pm'), False)
		self.assertEqual(babysitter.timeTest('4:18am'), False)
		self.assertEqual(babysitter.timeTest('6:4pm',), False)
		self.assertEqual(babysitter.timeTest('7:63am'), False)
		self.assertEqual(babysitter.timeTest('7:22em'), False)
		self.assertEqual(babysitter.timeTest('6:29pm'), True)
		self.assertEqual(babysitter.timeTest('8:38pm'), True)
		self.assertEqual(babysitter.timeTest('6:59pm'), True)
		self.assertEqual(babysitter.timeTest('2:37am'), True)
		self.assertEqual(babysitter.timeTest('12:09pm'), False)
		self.assertEqual(babysitter.timeTest('12:00am'), True)
		self.assertEqual(babysitter.timeTest('4:00pm'), False)
		self.assertEqual(babysitter.timeTest('3:002pm'), False)
		self.assertEqual(babysitter.timeTest('3:76pm'), False)
		self.assertEqual(babysitter.timeTest('1:59om'), False)
		self.assertEqual(babysitter.timeTest('6:28pm'), True)
		self.assertEqual(babysitter.timeTest('7:26pm'), True)

	def test_relativeTimeTest(self):
		self.assertEqual(babysitter.relativetimeTest('5:00pm','4:00am'), True)
		self.assertEqual(babysitter.relativetimeTest('4:00am','5:00pm'), False)
		self.assertEqual(babysitter.relativetimeTest('12:00am','3:33pm'), True)
		self.assertEqual(babysitter.relativetimeTest('11:02pm','12:51am'), True)
		self.assertEqual(babysitter.relativetimeTest('8:09pm','7:26pm'), False)
		self.assertEqual(babysitter.relativetimeTest('5:04pm','5:03pm'), False)
		self.assertEqual(babysitter.relativetimeTest('6:03pm','7:03pm'), True)
		self.assertEqual(babysitter.relativetimeTest('2:46am','12:42am'), False)
		self.assertEqual(babysitter.relativetimeTest('1:23am','2:22am'), True)
		self.assertEqual(babysitter.relativetimeTest('2:22pm','5:10pm'), False)

if __name__ == '__main__':
	unittest.main()