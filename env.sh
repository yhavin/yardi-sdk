#!/bin/bash

ENV_FILE=".env"

if [ -f "$ENV_FILE" ]; then
    echo "$ENV_FILE" already exists.
    exit 0
fi

echo "Creating $ENV_FILE..."

cat <<EOL >$ENV_FILE
WSDL_URL=https://webservicepath?WSDL
USERNAME=username
PASSWORD=password
SERVER_NAME=servername
DATABASE=database
PLATFORM=platform
INTERFACE_ENTITY=interfaceentitity
INTERFACE_LICENSE=interfacelicense
EOL

echo "$ENV_FILE" successfully created.