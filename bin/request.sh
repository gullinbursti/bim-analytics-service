#! /bin/bash

curl -v --request POST \
    -H "Content-Type: application/json" \
    -H 'Accept: application/json; indent=4' \
    "http://127.0.0.1:8000/selfieclub/" \
    --data '@request.json'

