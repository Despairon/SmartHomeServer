#!/usr/bin/env python

class RestApiHandlers:

	def deviceStatusGetRequest(server, params, body):
		# TODO: process GET requests here...
		if "id" in params:
			print("Device status GET requested for device with id: {}".format(params["id"]))
		else:
			print("Device status GET requested for all devices")

		print("Body:" + body)
		
	def deviceStatusPostRequest(server, params, body):
		# TODO: process POST requests here...
		print("Device status POST requested for device with id: {}".format(params["id"]))
		print("Body:" + body)
		
	def deviceStatusPutRequest(server, params, body):
		# TODO: process PUT requests here...
		print("Device status PUT requested for device with id: {}".format(params["id"]))
		print("Body:" + body)