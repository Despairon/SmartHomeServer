#!/usr/bin/env python

from restApiHandlers import RestApiHandlers
	
routes = {
	"GET": {
		"/deviceStatus" : RestApiHandlers.deviceStatusGetRequest
	},
	
	"POST": {
		"/deviceStatus" : RestApiHandlers.deviceStatusPostRequest
	},
	
	"PUT": {
		"/deviceStatus" : RestApiHandlers.deviceStatusPutRequest
	}
}