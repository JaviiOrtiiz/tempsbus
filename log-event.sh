#!/bin/bash

# Load variables from .env file
if [ -f .env ]; then
    source .env
fi

# Check if API_KEY is set as an environment variable
if [ -z "$API_KEY" ]; then
    echo "API_KEY is not set. Please set it in the .env file."
    exit 1
fi

# Check if a message is provided as argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <message>"
    exit 1
fi

# Assign the message provided as argument to a variable
message="$1"

# Define the message data including the variable message
data="[{\"message\": \"$message\", \"entity.guid\": \"MzYyMDI1NHxJTkZSQXxOQXwtNDgwMzUyMjQ5NDY4MzQxNzg2Mg\"}]"

# Perform the curl request with the provided data and API_KEY
curl --request POST \
    --data-raw "$data" \
    --url "https://log-api.eu.newrelic.com/log/v1?Api-Key=$API_KEY"
