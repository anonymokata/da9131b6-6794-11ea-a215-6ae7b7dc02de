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
	if hour not in range(13) or len(time_split[0]) > 2:
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