#!/bin/bash

# Navigate to the directory containing your repository
cd /home/pablo/tempsbus

# Pull the latest changes from the Git repository
git pull

# Stop and remove the old container if it exists
if [ "$(docker ps -q -f name=tempsbus)" ]; then
    docker stop tempsbus
    docker rm tempsbus
fi

# Build the Docker image
docker build -t tempsbus .

# Run the run.sh script
sh run.sh
