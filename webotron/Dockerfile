FROM python:3.8.2

MAINTAINER OMBU

WORKDIR /tmp

RUN apt-get -qq update && apt-get install -y build-essential \
    libssl-dev groff \
    && rm -rf /var/lib/apt/lists/*

#COPY requirements.txt .
COPY webotron.py .
#COPY index.html .
COPY kitten_web/* ./kitten_web/
#COPY awsconfig /root/.aws/config

#RUN pip install -r requirements.txt
RUN pip install boto3
RUN pip install click
RUN pip install nltk
RUN pip install numpy
RUN pip install pandas
RUN pip install scipy
RUN pip install sklearn
RUN pip install pickle
RUN pip install re

CMD ["pip", "freeze"]
