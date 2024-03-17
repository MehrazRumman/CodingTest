# Explanation video 
link : https://drive.google.com/file/d/1zyF_W-sX21V0qKeyKXc-Tvc5hSTWCuLZ/view?usp=sharing

# Setting up Airflow Docker Environment

This guide will walk you through setting up an Airflow Docker environment using virtualenv and Docker.

## Prerequisites

- [Python](https://www.python.org/downloads/) installed on your system
- [Docker](https://docs.docker.com/get-docker/) installed on your system

## Installation

1. **Create a Virtual Environment**: 
    ```bash
    python3 -m venv airflow_env
    ```

2. **Activate the Virtual Environment**:
    - On linux:
        ```bash
        source airflow_env/bin/activate
        ```
    

3. **Install Dependencies from `requirements.txt`**:
    ```bash
    pip install -r requirements.txt
    ```

## Setting up Airflow Docker Environment

4. **Pull the Airflow Docker Image**:
    ```bash
    docker pull apache/airflow:latest
    ```

5. **Start Airflow Container**:
    ```bash
    docker run -d -p 8080:8080 --name airflow_container apache/airflow:latest
    ```

6. **Initialize Airflow Database**:
    ```bash
    docker exec -it airflow_container airflow initdb
    ```

## Running Airflow

7. **Start Airflow Webserver**:
    ```bash
    docker exec -it airflow_container airflow webserver
    ```

8. **Start Airflow Scheduler**:
    ```bash
    docker exec -it airflow_container airflow scheduler
    ```

9. **Access Airflow UI**:
    - Open your web browser and go to [http://localhost:8080](http://localhost:8080)

10. **Login Credentials**:
    - Username: `admin`
    - Password: `admin`

11. **Creating and Running DAGs**:
    - Use Airflow UI to create and manage your DAGs.

# Airflow DAGs for Website Scraping

This repository contains Airflow DAGs for scraping data from various websites using Python scripts.

## Directory Structure

The `dags` directory contains the following Python scripts for scraping different types of data from websites:

1. **scrape_country.py**: Python script for scraping country details.
2. **scrape_hockey.py**: Python script for scraping hockey data.
3. **scrape_bikroy.py**: Python script for scraping job listings from Bikroy.

## DAGs Configuration

The following Airflow DAGs are configured to execute the scraping scripts:

1. **dag1**:
    - This DAG executes `scrape_country.py` and `scrape_hockey.py` scripts to scrape country details and hockey data.
    - It is responsible for scraping general information.

2. **dag2**:
    - This DAG executes `scrape_bikroy.py` script to scrape job listings from Bikroy.
    - It is dedicated to scraping job-related data.
  

# Here is some screen shots  
![alt text](https://github.com/mehrazrumman/CodingTest/blob/main/image/mong1.png?raw=true)
![alt text](https://github.com/mehrazrumman/CodingTest/blob/main/image/mong2.png?raw=true)
![alt text](https://github.com/mehrazrumman/CodingTest/blob/main/image/mongo3.png?raw=true)
![alt text](https://github.com/mehrazrumman/CodingTest/blob/main/image/csv1.png?raw=true)
![alt text](https://github.com/mehrazrumman/CodingTest/blob/main/image/csv2.png?raw=true)
![alt text](https://github.com/mehrazrumman/CodingTest/blob/main/image/csv3.png?raw=true)
