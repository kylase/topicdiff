# TopicDiff Visualisation Application

[![Build Status](https://travis-ci.com/kylase/cs-topic-app.svg?token=uVsTSLyLLpWLUJnmWAEA&branch=master)](https://travis-ci.com/kylase/cs-topic-app)

## Instructions

### Windows Powershell

`$env:FLASK_APP = "run.py"`

For development: `$env:FLASK_ENV = "development"`

### Linux/macOS

`export FLASK_APP="run.py"`

For development: `export FLASK_APP="development"`

## Objective 

The main objective of this web application is to visualise how 2 documents are similar in terms of the topics that they cover using a topic model.

## Technical Design

### Topic Model

The topic model is trained with the [Wikipedia's page dumps](https://dumps.wikimedia.org/enwiki/20180520/) using [gensim's LDA implementation](https://radimrehurek.com/gensim/models/ldamodel.html).

### Web Application

The web application is built with Python. 

[Flask](http://flask.pocoo.org/) is used as the back-end framework to handle the processing logic and to serve the data.

[jQuery](https://jquery.com/), [d3](https://d3js.org/), [Bootstrap](https://getbootstrap.com/) are used for the front-end design.

## API

**POST** `/api/documents/compare`

### Parameters

- `content` (*string*): 1 or more `content` is needed to show the topic cloud
- `model` (*string*): Only `wikipedia` is the valid value
- `threshold` (*float): Topics with score below the threshold will not be shown