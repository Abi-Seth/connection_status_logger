import socket

def ping():
	try:
		socket.setdefaulttimeout(5)

		session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		host = "8.8.8.8"
		port = 53

		server_address = (host, port)
		session.connect(server_address)

	except OSError as error:
		return False

	else:
		session.close()
		return True
