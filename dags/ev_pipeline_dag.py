from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocSubmitJobOperator,
    DataprocDeleteClusterOperator,
)

from datetime import datetime

# ---------------- CONFIGURATION -----------------
PROJECT_ID = "boxwood-axon-470816-b1"
REGION = "US"
CLUSTER_NAME = "ev-dataproc-cluster"
BUCKET_NAME = "ev-market-data"
PYSPARK_FILE = f"gs://{BUCKET_NAME}/scripts/etl_ev.py"

# ---------------- DAG DEFINITION ----------------
default_args = {"start_date": datetime(2025, 1, 1)}


with DAG(
    "ev_dataproc_simple",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
) as dag:

    create_cluster = DataprocCreateClusterOperator(
        task_id="create_cluster",
        project_id=PROJECT_ID,
        region=REGION,
        cluster_name=CLUSTER_NAME,
        cluster_config={
            "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-2"},
            "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-2"},
        },
    )

    submit_job = DataprocSubmitJobOperator(
        task_id="run_pyspark",
        project_id=PROJECT_ID,
        region=REGION,
        job={
            "placement": {"cluster_name": CLUSTER_NAME},
            "pyspark_job": {"main_python_file_uri": PYSPARK_FILE},
        },
    )

    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_cluster",
        project_id=PROJECT_ID,
        region=REGION,
        cluster_name=CLUSTER_NAME,
        trigger_rule="all_done",
    )

    create_cluster >> submit_job >> delete_cluster