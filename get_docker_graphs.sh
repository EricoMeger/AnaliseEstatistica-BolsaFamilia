#!/bin/bash

docker build -t projeto_estatistica .
docker run --name get_images -t projeto_estatistica

docker cp get_images:/app/images ./images