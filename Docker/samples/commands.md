# Commands

## Run with port mapping
docker run -p 5000:5000 python-webapp

docker run -p 8080:8080 go-webapp

docker run -p 3030:3030 rust-webapp

docker run -p 8080:8080 cpp-webapp

## Run with environment variables
docker run -p 5000:5000 -e ENVIRONMENT=staging python-webapp

## Run in detached mode
docker run -d -p 5000:5000 --name my-app python-webapp