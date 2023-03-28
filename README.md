# L3T12 - Word Vector Similarity
Requirement for HyperionDev SE Bootcamp - L3T12 Task 2

## Introduction
The requirement for this task is to build a system that will tell you what to watch next based on the word
vector similarity of the description of movies.

The file 'movies.txt' contains the movie descriptions where a each line is a description of a separate movie.

## How to run 'next_watch.py'
You can run the python file by following the below steps:
1. Clone this repository onto your machine
1. If you have not already done so, you will need to download Docker Desktop by visiting https://www.docker.com/products/docker-desktop/
1. If you don't already have a Docker Hub account, visit this website and create one: https://hub.docker.com
1. Navigate to the directory which contains the Dockerfile and build a Docker image by running this command in Terminal (Macbooks): "docker build --platform linux/amd64/v8 -t [name of your docker image] ./"
1. Run the program by entering the following into your terminal: "docker run [image name]" NOTE: Afterwards the container will automatically shut down.
