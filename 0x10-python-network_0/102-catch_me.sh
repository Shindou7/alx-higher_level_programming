#!/bin/bash
# Post Request Catch me if you can!
curl -sLX PUT -d 'user_id=98' -H 'Origin:School' "0.0.0.0:5000/catch_me"
