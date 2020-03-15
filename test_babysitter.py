import unittest
import babysitter

case_1 = ['4:59pm','6:59pm','A']
case_2 = ['5:00pm','2:37am','A']
case_3 = ['12:59am','12:09pm','B']
case_4 = ['12:33pm','12:00am','B']
case_5 = ['4:18am','4:00pm','C']
case_6 = ['6:4pm','3:002pm','C']
case_7 = ['7:63am','3:76pm','D']
case_8 = ['7:22em','1:59om','1']
case_9 = ['6:29pm','6:28pm','A']
case_10 = ['8:38pm','7:26pm','A']

class TestBabysitter(unittest.TestCase):

	def test_startTest(self):
		self.assertEqual(babysitter.startTest(case_1[0]), False)
		self.assertEqual(babysitter.startTest(case_2[0]), True)
		self.assertEqual(babysitter.startTest(case_3[0]), True)
		self.assertEqual(babysitter.startTest(case_4[0]), False)
		self.assertEqual(babysitter.startTest(case_5[0]), False)
		self.assertEqual(babysitter.startTest(case_6[0]), False)
		self.assertEqual(babysitter.startTest(case_7[0]), False)
		self.assertEqual(babysitter.startTest(case_8[0]), False)
		self.assertEqual(babysitter.startTest(case_9[0]), True)
		self.assertEqual(babysitter.startTest(case_10[0]), True)

	def test_endTest(self):
		self.assertEqual(babysitter.endTest(case_1[1]), True)
		self.assertEqual(babysitter.endTest(case_2[1]), True)
		self.assertEqual(babysitter.endTest(case_3[1]), False)
		self.assertEqual(babysitter.endTest(case_4[1]), True)
		self.assertEqual(babysitter.endTest(case_5[1]), True)
		self.assertEqual(babysitter.endTest(case_6[1]), False)
		self.assertEqual(babysitter.endTest(case_7[1]), False)
		self.assertEqual(babysitter.endTest(case_8[1]), False)
		self.assertEqual(babysitter.endTest(case_9[1]), True)
		self.assertEqual(babysitter.endTest(case_10[1]), True)



if __name__ == '__main__':
	unittest.main()