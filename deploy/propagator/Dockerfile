FROM python:3.9.6-slim-buster

RUN python -m pip install loguru \
     requests


# Copying requirements of a project
WORKDIR /app/src
# Copying actuall application
#COPY ./service_propagator /app/src/
#COPY ./service_propagator /app/src/service_propagator
#COPY ./service_propagator /app/src/service_propagator
COPY . /app/src/

#CMD ["/start-propagator"]
CMD ["/usr/local/bin/python", "-m", "service_propagator"]
#CMD ["/usr/local/bin/python", "-m", "fastapi_cybercare"]
#CMD ["/root/.local/bin/poetry", "run" ,"python", "-m", "fastapi_cybercare"]
