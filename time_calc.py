import datetime

def calculate_time(start, stop):

	# calculating unavailability
	# time and converting it in seconds
	difference = stop - start
	seconds = float(str(difference.total_seconds()))
	return str(datetime.timedelta(seconds=seconds)).split(".")[0]
