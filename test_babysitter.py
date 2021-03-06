import unittest
import babysitter

class TestBabysitter(unittest.TestCase):

	def test_timeTest(self):
		self.assertEqual(babysitter.timeTest('4:59pm'), False)
		self.assertEqual(babysitter.timeTest('5:00pm'), True)
		self.assertEqual(babysitter.timeTest('12:59am'), True)
		self.assertEqual(babysitter.timeTest('12:33pm'), False)
		self.assertEqual(babysitter.timeTest('4:18am'), False)
		self.assertEqual(babysitter.timeTest('6:4pm'), False)
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
		self.assertEqual(babysitter.timeTest('a'), False)

	def test_timeInMinutes(self):
		self.assertEqual(babysitter.timeInMinutes('4:59pm'), 1019)
		self.assertEqual(babysitter.timeInMinutes('5:00pm'), 1020)
		self.assertEqual(babysitter.timeInMinutes('12:59am'), 59)
		self.assertEqual(babysitter.timeInMinutes('12:33pm'), 753)
		self.assertEqual(babysitter.timeInMinutes('4:18am'), 258)
		self.assertEqual(babysitter.timeInMinutes('6:29pm'), 1109)
		self.assertEqual(babysitter.timeInMinutes('8:38pm'), 1238)
		self.assertEqual(babysitter.timeInMinutes('6:59pm'), 1139)
		self.assertEqual(babysitter.timeInMinutes('2:37am'), 157)
		self.assertEqual(babysitter.timeInMinutes('12:09pm'), 729)
		self.assertEqual(babysitter.timeInMinutes('12:00am'), 0)
		self.assertEqual(babysitter.timeInMinutes('4:00pm'), 960)
		self.assertEqual(babysitter.timeInMinutes('12:00pm'), 720)
		self.assertEqual(babysitter.timeInMinutes('7:26pm'), 1166)

	def test_relativeTimeTest(self):
		self.assertEqual(babysitter.relativeTimeTest('5:00pm','4:00am'), True)
		self.assertEqual(babysitter.relativeTimeTest('4:00am','5:00pm'), False)
		self.assertEqual(babysitter.relativeTimeTest('12:00am','3:33pm'), False)
		self.assertEqual(babysitter.relativeTimeTest('11:02pm','12:51am'), True)
		self.assertEqual(babysitter.relativeTimeTest('8:09pm','7:26pm'), False)
		self.assertEqual(babysitter.relativeTimeTest('5:04pm','5:03pm'), False)
		self.assertEqual(babysitter.relativeTimeTest('6:03pm','7:03pm'), True)
		self.assertEqual(babysitter.relativeTimeTest('2:46am','12:42am'), False)
		self.assertEqual(babysitter.relativeTimeTest('1:23am','2:22am'), True)
		self.assertEqual(babysitter.relativeTimeTest('7:22pm','5:10pm'), False)

	def test_amountPaid(self):
		self.assertEqual(babysitter.amountPaid('5:00pm','4:00am','A'), '$195')
		self.assertEqual(babysitter.amountPaid('5:00pm','4:00am','B'), '$136')
		self.assertEqual(babysitter.amountPaid('5:00pm','4:00am','C'), '$183')
		self.assertEqual(babysitter.amountPaid('11:02pm','12:51am','A'), '$20')
		self.assertEqual(babysitter.amountPaid('11:02pm','12:51am','B'), '$16')
		self.assertEqual(babysitter.amountPaid('11:02pm','12:51am','C'), '$15')
		self.assertEqual(babysitter.amountPaid('6:03pm','7:03pm','A'), '$15')
		self.assertEqual(babysitter.amountPaid('6:03pm','7:03pm','B'), '$12')
		self.assertEqual(babysitter.amountPaid('6:03pm','7:03pm','C'), '$21')
		self.assertEqual(babysitter.amountPaid('1:23am','2:22am','A'), '$0')
		self.assertEqual(babysitter.amountPaid('1:23am','2:22am','B'), '$0')
		self.assertEqual(babysitter.amountPaid('1:23am','2:22am','C'), '$0')
		self.assertEqual(babysitter.amountPaid('1:23am','2:22am','D'), False)

	def test_output(self):
		self.assertEqual(babysitter.output('5:00pm','4:00am','A'), 'Amount Paid: $195')
		self.assertEqual(babysitter.output('5:00pm','4:00am','B'), 'Amount Paid: $136')
		self.assertEqual(babysitter.output('5:00pm','4:00am','C'), 'Amount Paid: $183')
		self.assertEqual(babysitter.output('11:02pm','12:51am','A'), 'Amount Paid: $20')
		self.assertEqual(babysitter.output('11:02pm','12:51am','B'), 'Amount Paid: $16')
		self.assertEqual(babysitter.output('11:02pm','12:51am','C'), 'Amount Paid: $15')
		self.assertEqual(babysitter.output('6:03pm','7:03pm','A'), 'Amount Paid: $15')
		self.assertEqual(babysitter.output('6:03pm','7:03pm','B'), 'Amount Paid: $12')
		self.assertEqual(babysitter.output('6:03pm','7:03pm','C'), 'Amount Paid: $21')
		self.assertEqual(babysitter.output('1:23am','2:22am','A'), 'Amount Paid: $0')
		self.assertEqual(babysitter.output('1:23am','2:22am','B'), 'Amount Paid: $0')
		self.assertEqual(babysitter.output('1:23am','2:22am','C'), 'Amount Paid: $0')
		self.assertEqual(babysitter.output('3:55am','3:55am','C'), 'Amount Paid: $0')
		self.assertEqual(babysitter.output('1:23am','2:22am','D'), False)
		self.assertEqual(babysitter.output('1:23ym','2:22am','A'), False)
		self.assertEqual(babysitter.output('1:23am','23:22am','A'), False)
		self.assertEqual(babysitter.output('2:23am','2:22am','A'), False)
		self.assertEqual(babysitter.output('1:23am','4:22am','B'), False)
		self.assertEqual(babysitter.output('5:23am','6:12am','B'), False)
		self.assertEqual(babysitter.output('0:23am','2:22am','B'), False)
		self.assertEqual(babysitter.output('1:23am','0:22am','C'), False)
		self.assertEqual(babysitter.output('4:00am','6:22am','C'), False)
		self.assertEqual(babysitter.output('5:00pm','5:00am','C'), False)
		self.assertEqual(babysitter.output('4:00am','6:22am',''), False)
		self.assertEqual(babysitter.output('','5:00am','C'), False)
		self.assertEqual(babysitter.output('2am','4:00am','C'), False)

if __name__ == '__main__':
	unittest.main()