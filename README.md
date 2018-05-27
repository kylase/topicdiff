# Topic Model Application

[![Build Status](https://travis-ci.com/kylase/cs-topic-app.svg?token=uVsTSLyLLpWLUJnmWAEA&branch=master)](https://travis-ci.com/kylase/cs-topic-app)

## Instructions

### Windows Powershell

`$env:FLASK_APP = "run.py"`

### *Unix

`export FLASK_APP="run.py"`

## Objective 

The main objective of this web application is to visualise how 2 documents are similar in terms of the topics that they cover using a topic model.

## Technical Design

### Topic Model

The topic model is trained with the [Wikipedia's page dumps](https://dumps.wikimedia.org/enwiki/20180520/) using [gensim's LDA implementation](https://radimrehurek.com/gensim/models/ldamodel.html).

### Web Application

The web application is built with Python. 

[Flask](http://flask.pocoo.org/) is used as the back-end framework to serve the data and logic. 