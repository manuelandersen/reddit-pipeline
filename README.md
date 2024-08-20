# Reddit ELT Pipeline 

This is a repo to implement an ETL pipeline for Reddit data using Airflow and AWS cloud services.

## Overview

What the pipelines does:

- Extract Reddit data trough their API.
- Load the data to an S3 bucket.
- Perform some transformations to the data using AWS Glue.

## Installation

1)  Clone the repository

``` bash
git clone https://github.com/manuelandersen/reddit-pipeline.git
```

2)  Create a virtual environment (optional but recommended):

``` bash
python3 -m venv venv
source venv/bin/activate
```

3)  Install the dependencies:

``` bash
pip install -r requirements.txt
```

4) Rename the configuration file:

``` bash
 mv config/config.conf.example config/config.conf
``` 
> [!WARNING]  
> Make sure to put the credentials you need in the new config.conf file.

5) Build and run the Docker container:

``` bash
docker compose up -d --build
``` 

6) Open Airflow web UI:

In your browser go to `http://localhost:8080`, you will see the DAG's and then you can run them.