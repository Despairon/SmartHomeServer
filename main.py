#!/usr/bin/env python

import argparse
import time
from http.server import HTTPServer
from smartHomeServer import SmartHomeServer

def parseArguments():
	parser = argparse.ArgumentParser(description="Runs Smart Home Server which serves both devices and client applications via REST API.")
	
	parser.add_argument("--host", type=str, help="Host name to be used by the server. Don\'t specify this argument to use default value (localhost)")
	parser.add_argument("--port", type=int, help="Host port to be used by the server. Don\'t specify this argument to use default value (8000)")

	return parser.parse_args()

def main():
	args = parseArguments()

	if args.host:
		hostName = args.host
	else:
		hostName = "localhost"
	
	if args.port:
		hostPort = args.port
	else:
		hostPort = 8000

	server = HTTPServer((hostName, hostPort), SmartHomeServer)
	
	print("{}: Server {}:{} is UP".format(time.asctime(), hostName, hostPort))
	
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print("Keyboard interrupt received. Closing the server...")
		pass
		
	server.server_close()
	
	print("{}: Server {}:{} is DOWN".format(time.asctime(), hostName, hostPort))
	
	return True

if __name__ == '__main__':
	exit(0 if main() else 1)