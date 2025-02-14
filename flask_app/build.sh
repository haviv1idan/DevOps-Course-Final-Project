#!/bin/bash

# get version
version=$(cat version.txt)
echo $version 

# build Docker image
docker build -t flask-app:$version .

# tag image with version
docker tag flask-app:$version haviv1idan/dev_sec_ops_course:flask-app-$version

# push image to Docker Hub
docker push haviv1idan/dev_sec_ops_course:flask-app-$version
