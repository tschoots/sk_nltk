FROM ubuntu:17.10

RUN apt-get update -y && apt-get install -y python3 python3-pip 

#python3-numpy  python3-nltk

RUN pip3 install --upgrade pip \
    && pip3 install -U nltk -U numpy -U matplotlib -U networkx \
    && python3 -m nltk.downloader all
