#!/usr/bin/env python

class RestApiHandlers:

	def getHelloWorld(server, params, body):
		print("Hello world is hit!")
		server.send_response(200)
		server.send_header('Content-type', "text/plain")
		server.end_headers()
		server.wfile.write(bytes("Hello World!", "UTF-8"))

	def deviceStatusGetRequest(server, params, body):
		if "id" in params:
			print("Device status GET requested for device with id: {}".format(params["id"]))
		else:
			print("Device status GET requested for all devices")
		
		print("Body:" + body)
		
	def deviceStatusPostRequest(server, params, body):
		print("Device status POST requested for device with id: {}".format(params["id"]))
		print("Body:" + body)
		
	def deviceStatusPutRequest(server, params, body):
		print("Device status PUT requested for device with id: {}".format(params["id"]))
		print("Body:" + body)