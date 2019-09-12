#!/usr/bin/env python

import time
import json
import os
import pymongo
from cryptography.fernet import Fernet
from http.server import HTTPServer
from serverRequestHandler import ServerRequestHandler

class SmartHomeServer(HTTPServer):

	__defaultConfig = {
		"defaultHost"        : "localhost",
		"defaultPort"        : 8000,
		"database"           : "mongodb+srv://SmartHomeServer:pw@despaironcluster-lorle.mongodb.net/test?retryWrites=true&w=majority",
		"db_pw_encrypted"    : "gAAAAABdesqmOQQG5tz6ma5zHTCtF8tdhpqjWWKccbAkgxEnlZCBHeDBXOaIek4AlHUwwjM-DmMH3gY1DgFX0Iz7wyYoD9QZNA==",
		"db_pw_key_location" : "pw.key"
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
			with open(self.__config["db_pw_key_location"], "r") as keyFile:
				f = Fernet(keyFile.read())
				keyFile.close()
				password = f.decrypt(self.__config["db_pw_encrypted"].encode())
				databaseUrl = self.__config["database"].replace(":pw@", ":{}@".format(password.decode("utf-8")))
				self.__dbClient = pymongo.MongoClient(databaseUrl)
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