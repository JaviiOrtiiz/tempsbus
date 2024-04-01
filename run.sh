#!/bin/bash
docker run -d -v /home/pablo/tempsbus:/app --restart always tempsbus --name tempsbus
