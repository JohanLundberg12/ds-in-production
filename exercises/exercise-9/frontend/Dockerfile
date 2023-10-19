# start by pulling the python image
FROM python:3.8-alpine
RUN mkdir /frontend
# COPY is preferred over ADD: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#:~:text=COPY%20only%20supports%20the%20basic,image%2C%20as%20in%20ADD%20rootfs.
COPY . /frontend
WORKDIR /frontend

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["view.py" ]