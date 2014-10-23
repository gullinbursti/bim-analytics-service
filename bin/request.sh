#! /bin/bash

curl -v --request POST \
    -H "Content-Type: application/json" \
    -H 'Accept: application/json; indent=4' \
    "http://stats.devint.selfieclubapp.com/selfieclub/" \
    --data '@request.json'

