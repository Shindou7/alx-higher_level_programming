#!/bin/bash
# Post Request  cURL a JSON file
curl -sLX POST -H 'Content-Type: application/json' -d @"$2" "$1"
