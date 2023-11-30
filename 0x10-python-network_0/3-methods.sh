#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP
curl -sI "$1" | grep "Allow:" | cut -d" " -f2-
