FROM python:3.6-alpine3.7

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

# install chromedriver
RUN apk add chromium chromium-chromedriver 

# set display port to avoid crash
ENV DISPLAY=:99

COPY requirements.txt  fanatic.py ./ 
RUN pip install --upgrade pip &&  pip install -r requirements.txt

ENTRYPOINT ["python3","fanatic.py"]