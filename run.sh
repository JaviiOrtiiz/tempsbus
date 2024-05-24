#!/bin/bash
docker run -d -v /home/pablo/tempsbus:/app --restart always --name tempsbus -p 5000:5000 tempsbus --memory=50m
