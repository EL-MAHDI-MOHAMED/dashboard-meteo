# Apache Spark with Docker

This project provides a simple setup to run an Apache Spark cluster using Docker Compose with the official `apache/spark` image.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1.  Start the cluster:
    ```bash
    docker-compose up -d
    ```

2.  Access the Spark Master Web UI:
    Open [http://localhost:8080](http://localhost:8080) in your browser.

3.  Submit jobs (Example):
    ```bash
    docker exec -it spark-master /opt/spark/bin/spark-submit \
      --master spark://spark-master:7077 \
      --class org.apache.spark.examples.SparkPi \
      /opt/spark/examples/jars/spark-examples_2.12-3.5.0.jar 10
    ```
    *Note: Adjust the jar path version if necessary matching the image version.*

4.  Stop the cluster:
    ```bash
    docker-compose down
    ```

## Services

-   **Spark Master**: Exposed on port 8080 (Web UI) and 7077 (Master URL).
-   **Spark Worker**: Connects to the master.
