import datetime
from connect import ping
from sync_network_logs import FILE

def first_check():

	if ping():
		live = "\nCONNECTION ACQUIRED\n"
		print(live)
		connection_acquired_time = datetime.datetime.now()
		acquiring_message = "connection acquired at: " + \
			str(connection_acquired_time).split(".")[0]
		print(acquiring_message)

		with open(FILE, "a") as file:
			file.write(live)
			file.write(acquiring_message)

		return True

	else:
		not_live = "\nCONNECTION NOT ACQUIRED\n"
		print(not_live)

		with open(FILE, "a") as file:
			file.write(not_live)
		return False

