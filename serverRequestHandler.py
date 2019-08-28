#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler
from router import routes
from urllib.parse import urlparse, parse_qs

class ServerRequestHandler(BaseHTTPRequestHandler):
	
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
		pathWithoutParams = self.path.split("?")[0]
		
		print("Requested {} on: {}".format(self.command, pathWithoutParams))
		
		if self.command in routes:
			if pathWithoutParams in routes[self.command]:
				contentType = self.headers.get('content-type')
				
				if contentType == "application/json":
					bodyLength = int(self.headers.get('content-length'))
					body = self.rfile.read(bodyLength).decode("UTF-8")
				else:
					body = ""
				
				params = parse_qs(urlparse(self.path).query)
				
				routes[self.command][pathWithoutParams](self.server, params, body)
			else:
				self.sendError(404, "404: request {} {} not found.".format(self.command, self.path))
		else:
			self.sendError(404, "404: request {} {} not found.".format(self.command, self.path))
	
	def sendError(self, status, message):
		self.send_response(status)
		self.send_header('Content-type', "text/plain")
		self.end_headers()
		self.wfile.write(bytes(message, "UTF-8"))