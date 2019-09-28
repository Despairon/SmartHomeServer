#!/bin/sh
JSON="{
	\"eventName\": \"deviceOnline\",
	
	\"parameters\": [
		{
			\"name\":         \"device_ID\",
			\"type\":         \"TEXTBOX\",
			\"currentValue\": \"5d8f88455dc9e7c78707adfd\",
			\"values\":       [\"100500200300\"],
			\"readOnly\":     true
		},
		{
			\"name\":         \"device_MAC_Address\",
			\"type\":         \"TEXTBOX\",
			\"currentValue\": \"4C-CC-6A-29-E0-B7\",
			\"values\":       [\"4C-CC-6A-29-E0-B7\"],
			\"readOnly\":     true
		},
		{
			\"name\":         \"device_Name\",
			\"type\":         \"TEXTBOX\",
			\"currentValue\": \"TestSmartHomeDevice\",
			\"values\":       [\"TestSmartHomeDevice\"],
			\"readOnly\":     true
		},
		{
			\"name\":         \"device_Status\",
			\"type\":         \"TEXTBOX\",
			\"currentValue\": \"Online\",
			\"values\":       [\"Online\", \"Offline\"],
			\"readOnly\":     true
		}
	]
}"

echo curl --request PUT --header "Accept: application/json" --header "Content-type: application/json" --header "Content-Length: ${#JSON}" --data "$JSON" 176.36.209.154:8000/deviceStatus
curl --request PUT --header "Accept: application/json" --header "Content-type: application/json" --header "Content-Length: ${#JSON}" --data "$JSON" 176.36.209.154:8000/deviceStatus