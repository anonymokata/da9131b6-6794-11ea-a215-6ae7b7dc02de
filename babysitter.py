def output(startTime,endTime,family):
	if (timeTest(startTime) and timeTest(endTime) and relativeTimeTest(startTime,endTime)) == False:
		return False
	else:
		amount_paid = amountPaid(startTime,endTime,family)
		if amount_paid == False:
			return False
		return ('Amount Paid: ' + amount_paid)

def timeTest(time): #returns True when time is between 5pm and 4am; otherwise False
	in_minutes = timeInMinutes(time)
	if in_minutes is not False:
		if in_minutes >= 17*60 or in_minutes <= 4*60:
			return True
		else:
			return False
	else:
		return False

def relativeTimeTest(startTime,endTime): #returns False if endTime is prior to startTime
	start_time_minutes = timeInMinutes(startTime)
	end_time_minutes = timeInMinutes(endTime)
	if start_time_minutes <= 4*60:
		start_time_minutes += 24*60
	if end_time_minutes <= 4*60:
		end_time_minutes += 24*60
	if end_time_minutes >= start_time_minutes:
		return True
	else:
		return False

def timeInMinutes(time): #returns given time in minutes; returns False if input is incorrectly formatted
	time_split = time.split(':')
	hour = int(time_split[0])
	if hour not in range(1,13) or len(time_split[0]) > 2:
		return False 
	minute = int(time_split[1][0:-2])
	if minute not in range(60) or len(time_split[1][0:-2]) != 2:
		return False 
	if time_split[1][-2:] == 'pm' and hour != 12:
		hour += 12
	elif time_split[1][-2:] != 'am' and hour != 12:
		return False
	if hour == 12 and time_split[1][-2:] == 'am':
		hour = 0
	return (hour*60 + minute)

def amountPaid(startTime,endTime,family): #returns amount paid as string; only paid for full hours
	start_time_minutes = timeInMinutes(startTime)
	end_time_minutes = timeInMinutes(endTime)
	if start_time_minutes <= 4*60:
		start_time_minutes += 24*60
	if end_time_minutes <= 4*60:
		end_time_minutes += 24*60
	hours_worked = (end_time_minutes - start_time_minutes) // 60
	amount_paid = 0
	if family == 'A':
		while start_time_minutes < 22*60:
			if hours_worked >= 1:
				start_time_minutes += 60
				hours_worked -= 1
				amount_paid += 15
			else:
				return '$' + str(amount_paid)
		while hours_worked >= 1:
			hours_worked -= 1
			amount_paid += 20
		return '$' + str(amount_paid)
	elif family == 'B':
		while start_time_minutes < 21*60:
			if hours_worked >= 1:
				start_time_minutes += 60
				hours_worked -= 1
				amount_paid += 12
			else:
				return '$' + str(amount_paid)
		while start_time_minutes <= 23*60:
			if hours_worked >= 1:
				start_time_minutes += 60
				hours_worked -= 1
				amount_paid += 8
			else:
				return '$' + str(amount_paid)
		while hours_worked >= 1:
			hours_worked -= 1
			amount_paid += 16
		return '$' + str(amount_paid)
	elif family == 'C':
		while start_time_minutes < 20*60:
			if hours_worked >= 1:
				start_time_minutes += 60
				hours_worked -= 1
				amount_paid += 21
			else:
				return '$' + str(amount_paid)
		while hours_worked >= 1:
			hours_worked -= 1
			amount_paid += 15
		return '$' + str(amount_paid)
	else:
		return False