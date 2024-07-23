# base image
FROM python:3.9 


RUN pip install pandas 


#sys.argv -> printing all the arguments we passed to the script

#specifying the directory
WORKDIR /app

# copying the file from our current working directory to our docker image
COPY pipeline.py pipeline.py

#overwriting the entrypoint

ENTRYPOINT [ "bash" ]