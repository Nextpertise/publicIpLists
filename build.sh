#!/bin/bash
docker build -t registry.nextpertise.tools/nextpertise/public-ip-lists:latest .
docker rm -f public-ip-lists; sleep 1; docker run -p 5000:5000 --name public-ip-lists -d registry.nextpertise.tools/nextpertise/public-ip-lists
