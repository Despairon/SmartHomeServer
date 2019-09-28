#!/usr/bin/env python

import json
from bson.json_util import dumps

class RestApiHandlers:

	def deviceStatusGetRequest(reqHandler, server, params, body):
		result = True
		deviceInfo = None
		
		if "id" in params:
			print(params["id"][0])
			result, deviceInfo = server.getDeviceInfo(params["id"][0])
			
			if not result:
				reqHandler.sendError(404, "NO device with id: {}, or the collection is empty".format(params["id"]))
		else:
			result, deviceInfo = server.getAllDeviceInfos()
			
			if not result:
				reqHandler.sendError(404, "Devices collection is empty")
		
		if result:
			bodyData = dumps(deviceInfo)

			reqHandler.send_response(200)
			reqHandler.send_header('Accept', "application/json")
			reqHandler.send_header('Content-type', "application/json")
			reqHandler.send_header('Content-Length', len(bodyData))
			reqHandler.end_headers()
			reqHandler.wfile.write(bytes(bodyData, "UTF-8"))
		
	def deviceStatusPostRequest(reqHandler, server, params, body):
		# TODO: process POST requests here...
		print("Device status POST requested for device with id: {}".format(params["id"]))
		print("Body:" + body)
		
	def deviceStatusPutRequest(reqHandler, server, params, body):
		bodyJson = json.loads(body)
		
		if bodyJson["eventName"] == "deviceOnline":
			result, deviceId = server.addDevice(bodyJson["parameters"])
			
			if result:
				respData = {
					"eventName": "deviceOnlineResponse",
					"responseData" : "{\"deviceId\": " + str(deviceId) + "}"
				}
				
				respJson = json.dumps(respData)
				
				reqHandler.send_response(200)
				reqHandler.send_header('Accept', "application/json")
				reqHandler.send_header('Content-type', "application/json")
				reqHandler.send_header('Content-Length', len(respJson))
				reqHandler.end_headers()
				reqHandler.wfile.write(bytes(respJson, "UTF-8"))
			else:
				reqHandler.sendError(500, "Error adding the device.")