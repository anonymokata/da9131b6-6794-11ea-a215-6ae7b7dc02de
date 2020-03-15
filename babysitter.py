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