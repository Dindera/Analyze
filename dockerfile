# syntax=docker/dockerfile:1
# FROM python:3.7
# WORKDIR C:/Users/chide/OneDrive/Documents/Research Project/Analyze
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# COPY requirements.txt requirements.txt
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN /usr/local/bin/python -m pip install pyspark
# RUN pip install -r requirements.txt
# EXPOSE 5000
# COPY . .
# CMD ["flask", "run"]