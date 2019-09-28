#!/usr/bin/env python

import time
import json
import os
import pymongo
from cryptography.fernet import Fernet
from http.server import HTTPServer
from serverRequestHandler import ServerRequestHandler
from bson.objectid import ObjectId

class SmartHomeServer(HTTPServer):

	__defaultConfig = {
		"defaultHost"        : "localhost",
		"defaultPort"        : 8000,
		"database"           : "mongodb+srv://SmartHomeServer:pw@despaironcluster-lorle.mongodb.net/test?retryWrites=true&w=majority",
		"db_pw_encrypted"    : "gAAAAABdj2Q4iLK0EGjP0uAzeA-lPA7-hqA86rPqFVhhU7fTiXcHAkSardTXA62MQLhc8iWlSlgx-hO8UylPtOTYmBvo_ruRr9FCvXMJ_U4NZsRsgR6gypQ=",
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
				self.__devicesDb = self.__dbClient.devicesDatabase
				self.__devicesCollection = self.__devicesDb.devicesCollection
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
		
	def getDeviceInfo(self, deviceId):
		result = True
		deviceInfo = None
		
		if self.__devicesCollection:
			deviceInfo = self.__devicesCollection.find_one({"_id": ObjectId(deviceId)})
			if not deviceInfo:
				result = False
		else:
			result = False
			
		return result, deviceInfo
		
	def getAllDeviceInfos(self):
		result = True
		deviceInfos = None
		
		if self.__devicesCollection:
			if self.__devicesCollection.find_one():
				deviceInfos = self.__devicesCollection.find()
			if not deviceInfos:
				result = False
		else:
			result = False
		
		return result, deviceInfos
		
	def addDevice(self, deviceDesc):
		result = True
		deviceId = None
		deviceInfoFromDb = None
		
		for param in deviceDesc:
			if param["name"] == "device_ID":
				deviceId = param["currentValue"]
				break
		else:
			result = False
			
		if result and deviceId:
			try:
				# TODO: use mac address to look up the device
				deviceInfoFromDb = self.__devicesCollection.find_one({"_id": ObjectId(deviceId)})
			except Exception:
				pass
			
			if deviceInfoFromDb:
				opResult = self.__devicesCollection.replace_one({"_id": ObjectId(deviceId)}, {"deviceDesc": deviceDesc}, upsert=False)
				# TODO: find out why doesn't work.
				#if not opResult["matched_сount"] or not opResult["modified_count"]:
				#	result = False
			else:
				deviceId = self.__devicesCollection.insert_one({"deviceDesc": deviceDesc}).inserted_id
		else:
			result = False
			
		return result, deviceId