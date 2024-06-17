#!/bin/bash
docker run -d -v /home/orangepi/tempsbus:/app --restart always --memory=50m --name tempsbus -p 5000:5000 tempsbus
