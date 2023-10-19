# start by pulling the python image
FROM python:3.8-alpine
RUN mkdir /backend_z
COPY . /backend_z
WORKDIR /backend_z

COPY requirements.txt requirements.txt
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["chars.py" ]