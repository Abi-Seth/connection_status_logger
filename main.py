import datetime
import time
from internet_checker import first_check
from connect import ping
from time_calc import calculate_time
from sync_network_logs import FILE

def main():

	monitor_start_time = datetime.datetime.now()
	monitoring_date_time = "monitoring started at: " + \
		str(monitor_start_time).split(".")[0]

	if first_check():
		print(monitoring_date_time)

	else:
		while True:
			if not ping():
				time.sleep(1)
			else:
				first_check()
				print(monitoring_date_time)
				break

	with open(FILE, "a") as file:
		file.write("\n")
		file.write(monitoring_date_time + "\n")

	while True:
		if ping():
			time.sleep(5)

		else:
			down_time = datetime.datetime.now()
			fail_msg = "disconnected at: " + str(down_time).split(".")[0]
			print(fail_msg)

			with open(FILE, "a") as file:
				file.write(fail_msg + "\n")

			while not ping():
				time.sleep(1)

			up_time = datetime.datetime.now()

			uptime_message = "connected again: " + str(up_time).split(".")[0]

			down_time = calculate_time(down_time, up_time)
			unavailablity_time = "connection was unavailable for: " + down_time

			print(uptime_message)
			print(unavailablity_time)

			with open(FILE, "a") as file:
				file.write(uptime_message + "\n")
				file.write(unavailablity_time + "\n")

main()
