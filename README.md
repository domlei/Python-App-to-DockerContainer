Simple webscraping code containerized in a docker container.

Tag of the image:
dockdomas/ind_task2:latest

First steps:
Creating a docker file in the same directory as the python code.
Specifying that packages from requirements.txt file should be included.
In Pycharm - quite easy to obtain requirements: Tools -> Sync Python Requirements...

In the Python code I'm using a convenient website made for practicing webscraping: https://www.scrapethissite.com/pages/simple/

# Commands used in the command line terminal for the project environment:

Building a docker image including my specified commands in dockerfile and project environment. Additionally, giving the image a name "app1" for clarity purposes in case other images are present: <br/>

docker build -t app1 . 

Checking if the created image is present and if there are more images: <br/>

docker image list

Running the container named "my-running-app" and the image within it to produce the code result: <br/>

docker run --name my-running-app app1

# Commands used in command line for pushing the Docker image to a container registry:

Tagging the local image with the remote repository name and tag: <br/>

docker tag app1 dockdomas/ind_task2

Pushing the local image to the repository: <br/>

docker push dockdomas/ind_task2

