import unittest
import babysitter

case_1 = ['4:59pm','4:59pm','A']
case_2 = ['5:00pm','4:59pm','A']
case_3 = ['12:59am','4:59pm','B']
case_4 = ['12:33pm','4:59pm','B']
case_5 = ['4:18am','4:59pm','C']
case_6 = ['6:4pm','4:59pm','C']
case_7 = ['7:63am','4:59pm','D']
case_8 = ['7:22em','4:59om','1']

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



if __name__ == '__main__':
	unittest.main()