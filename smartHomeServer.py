#!/usr/bin/env python

import time
from http.server import HTTPServer
from serverRequestHandler import ServerRequestHandler

class SmartHomeServer(HTTPServer):

	def __init__(self, args):
		self.__result = True
		
		if args.host:
			hostName = args.host
		else:
			hostName = "localhost"
		
		if args.port:
			hostPort = args.port
		else:
			hostPort = 8000

		super().__init__((hostName, hostPort), ServerRequestHandler)
		
		print("{}: Server {}:{} is UP".format(time.asctime(), hostName, hostPort))
		
		try:
			super().serve_forever()
		except KeyboardInterrupt:
			print("Keyboard interrupt received. Closing the server...")
			self.__result = False
			pass
			
		super().server_close()
		
		print("{}: Server {}:{} is DOWN".format(time.asctime(), hostName, hostPort))
	
	def getResult(self):
		return self.__result