#!/bin/bash
# Only status code
curl -sLIw '%{http_code}' "$1" -o /dev/null
