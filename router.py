#!/usr/bin/env python

from requestHandlers import RequestHandlers
	
routes = {
	"GET": {
		"/deviceStatus" : RequestHandlers.deviceStatusGetRequest
	},
	
	"POST": {
		"/deviceStatus" : RequestHandlers.deviceStatusPostRequest
	},
	
	"PUT": {
		"/deviceStatus" : RequestHandlers.deviceStatusPutRequest
	}
}