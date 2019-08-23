#!/usr/bin/env python

from requestHandlers import RequestHandlers
	
routes = {
	"GET": {
		"/" : RequestHandlers.getHelloWorld
	}
}