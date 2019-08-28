#!/usr/bin/env python

import argparse
from smartHomeServer import SmartHomeServer

def parseArguments():
	parser = argparse.ArgumentParser(description="Runs Smart Home Server which serves both devices and client applications via REST API.")
	
	parser.add_argument("--host", type=str, help="Host name to be used by the server. Don\'t specify this argument to use default value (localhost)")
	parser.add_argument("--port", type=int, help="Host port to be used by the server. Don\'t specify this argument to use default value (8000)")

	return parser.parse_args()

def main():
	args = parseArguments()

	server = SmartHomeServer(args)
	
	return server.getResult()

if __name__ == '__main__':
	exit(0 if main() else 1)