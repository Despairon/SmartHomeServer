#!/bin/sh

echo curl 176.36.209.154:8000/deviceStatus?id=$1
curl 176.36.209.154:8000/deviceStatus?id=$1