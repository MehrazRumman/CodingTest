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
    - On macOS/Linux:
        ```bash
        source airflow_env/bin/activate
        ```
    - On Windows:
        ```bash
        .\airflow_env\Scripts\activate
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

## Additional Resources

- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
