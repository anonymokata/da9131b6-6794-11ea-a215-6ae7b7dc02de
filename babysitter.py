def timeTest(time):
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
	as_minutes = hour*60 + minute
	if as_minutes >= 17*60 or as_minutes <= 4*60:
		return True
	else:
		return False

def relativeTimeTest(startTime,endTime): #assumes times given between 5pm and 4am
	startTime_split = startTime.split(':')
	start_hour = int(startTime_split[0])
	start_minute = int(startTime_split[1][0:-2])
	endTime_split = endTime.split(':')
	end_hour = int(endTime_split[0])
	end_minute = int(endTime_split[1][0:-2])
	if startTime_split[1][-2:] == 'pm' and start_hour != 12:
		start_hour += 12
	if start_hour == 12 and startTime_split[1][-2:] == 'am':
		start_hour = 0
	if endTime_split[1][-2:] == 'pm' and end_hour != 12:
		end_hour += 12
	if end_hour == 12 and endTime_split[1][-2:] == 'am':
		end_hour = 0
	startTime_as_minutes = start_hour*60 + start_minute
	endTime_as_minutes = end_hour*60 + end_minute
	if startTime_as_minutes <= 4*60:
		startTime_as_minutes += 24*60
	if endTime_as_minutes <= 4*60:
		endTime_as_minutes += 24*60
	if endTime_as_minutes >= startTime_as_minutes:
		return True
	else:
		return False