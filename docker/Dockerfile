FROM buildo/docker-python2.7-scikit-learn
COPY app.py .
# COPY package.json .

RUN apt-get update
#RUN apt-get purge python-requests -y
RUN apt-get purge python-pip -y
RUN apt-get install wget -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
#RUN apt-get install python-requests python-pip
RUN pip install -U flask
RUN pip install -U python-swiftclient
RUN pip install -U python-keystoneclient
RUN pip install -U pymongo
RUN sudo apt-get install python-pandas -y
EXPOSE  5000
ENV FLASK_APP=app.py
CMD ["python", "app.py"]
