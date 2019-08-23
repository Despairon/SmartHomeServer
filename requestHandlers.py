#!/usr/bin/env python

class RequestHandlers:

	def getHelloWorld(server):
		print("Hello world is hit!")
		server.send_response(200)
		server.send_header('Content-type', "text/plain")
		server.end_headers()
		server.wfile.write(bytes("Hello World", "UTF-8"))