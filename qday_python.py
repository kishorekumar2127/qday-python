# Function to calculate - Day of the Quarter
import calender 

def qday(date):
	date = pd.to_datetime(date)
	day = date.dayofyear
	year = date.year
	is_leap_year = calendar.isleap(year)
	if(not is_leap_year):
		if day <= 90:
			return day
		elif day > 90 and day <= 181:
			return (day-90)
		elif day > 181 and day <= 273:
			return (day-181)
		elif day > 273 and day <= 365:
			return (day-273)
		else:
			return None
	else:
		if(day <= 91):
			return day
		elif(day > 91 and day <= 182):
			return (day-91)
		elif(day > 182 and day <= 274):
			return (day-182)
		elif(day > 274 and day <= 366):
			return (day-274)
		else:
			return None