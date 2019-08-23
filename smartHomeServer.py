#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler
from router import routes

class SmartHomeServer(BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.handleRequest()
		
	def do_POST(self):
		self.handleRequest()
		
	def do_PUT(self):
		self.handleRequest()
		
	def do_DELETE(self):
		self.handleRequest()
		
	def do_HEAD(self):
		self.handleRequest()
		
	def handleRequest(self):
		print("Requested {} on: {}".format(self.command, self.path))
		
		if self.command in routes:
			if self.path in routes[self.command]:
				routes[self.command][self.path](self) # TODO: add arguments as a parameter
			else:
				self.sendError(404, "404: request {} {} not found.".format(self.command, self.path))
		else:
			self.sendError(404, "404: request {} {} not found.".format(self.command, self.path))
	
	def sendError(self, status, message):
		self.send_response(status)
		self.send_header('Content-type', "text/plain")
		self.end_headers()
		self.wfile.write(bytes("Hello World", "UTF-8"))