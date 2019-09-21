#!/usr/bin/env python

class RestApiHandlers:

	def deviceStatusGetRequest(reqHandler, server, params, body):
		result = True
		deviceInfo = None
		
		if "id" in params:
			result, deviceInfo = server.getDeviceInfo(params.id)
			
			if not result:
				reqHandler.sendError(404, "NO device with id: {}, or the collection is empty".format(params.id))
		else:
			result, deviceInfo = server.getAllDeviceInfos()
			
			if not result:
				reqHandler.sendError(404, "Devices collection is empty".format(params.id))
		
		if result:
			bodyData = json.dumps(deviceInfo).encode("UTF-8")
			
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
		# TODO: process PUT requests here...
		print("Device status PUT requested for device with id: {}".format(params["id"]))
		print("Body:" + body)