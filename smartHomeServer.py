#!/usr/bin/env python

import time
import json
import os
import pymongo
from http.server import HTTPServer
from serverRequestHandler import ServerRequestHandler

class SmartHomeServer(HTTPServer):

	__defaultConfig = {
		"defaultHost"  : "localhost",
		"defaultPort"  : 8000,
		"database"     : "mongodb+srv://SmartHomeServer:pw@despaironcluster-lorle.mongodb.net/test?retryWrites=true&w=majority"
	}

	def __init__(self, args):
		self.__result = True
		self.__config = self.__class__.__defaultConfig
		
		if os.path.exists("config"):
			with open("config", "r") as configFile:
				try:
					self.__config = json.load(configFile)
				except Exception:
					self.__config = self.__class__.__defaultConfig
					pass
		else:
			with open("config", "w") as configFile:
				json.dump(self.__class__.__defaultConfig, configFile)
		
		hostName = args.host if args.host else self.__config["defaultHost"]		
		hostPort = args.port if args.port else self.__config["defaultPort"]

		super().__init__((hostName, hostPort), ServerRequestHandler)
		
		try:
			self.__dbClient = pymongo.MongoClient(self.__config["database"])
		except Exception as e:
			print("Error connecting to the database: {}".format(e))
			self.__result = False
		
		if self.__result:
			print("{}: Server {}:{} is UP".format(time.asctime(), hostName, hostPort))
			
			try:
				super().serve_forever()
			except KeyboardInterrupt:
				print("Keyboard interrupt received. Closing the server...")
				self.__result = False
				pass
				
			self.__dbClient.close()
			super().server_close()
			
			print("{}: Server {}:{} is DOWN".format(time.asctime(), hostName, hostPort))
	
	def getResult(self):
		return self.__result