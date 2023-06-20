#set the base image
FROM python:3

# File Author / Maintainer
MAINTAINER rrmolinet@gmail.com


# add project files to the usr/src/app folder
ADD . /home/app

# set directoty where CMD will execute

WORKDIR /home/app

COPY requirements.txt ./

# Get pip to download and install requirements:
RUN pip install --no-cache-dir --trusted-host nexus.netcons.com.cu \
                                             -i https://nexus.netcons.com.cu/repository/pypi/simple -r requirements.txt

# Expose ports
EXPOSE 8000

# default command to execute
CMD exec gunicorn Aicros.wsgi:application --bind 0.0.0.0:8000 --workers 3