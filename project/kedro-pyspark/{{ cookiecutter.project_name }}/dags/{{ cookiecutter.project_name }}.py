from airflow import DAG
from datafy_airflow_plugins.datafy_container_plugin.datafy_container_operator import DatafyContainerOperator
from datetime import datetime, timedelta


{% set start_date = cookiecutter.workflow_start_date.split('-') -%}
{% set project_name = cookiecutter.project_name -%}
default_args = {
    "owner": "Datafy",
    "depends_on_past": False,
    "start_date": datetime(year={{ start_date[0] }}, month={{ start_date[1].lstrip("0") }}, day={{ start_date[2].lstrip("0") }}),
    "email": [],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


role = "{{ cookiecutter.project_name }}-{% raw %}{{ macros.env() }}{% endraw %}"

dag = DAG(
    "{{ cookiecutter.project_name }}", default_args=default_args, schedule_interval="{{ cookiecutter.workflow_schedule }}", max_active_runs=1
)

DatafyContainerOperator(
    dag=dag,
    task_id="kedro_run",
    name="kedro_run",
    cmds=["kedro"],
    arguments=["run", "--env", "{% raw %}{{ macros.env() }}{% endraw %}"],
    instance_type="mx_medium",
    service_account_name="spark",
    env_vars = {
        "spark.master": "k8s://https://kubernetes.default:443",
        "spark.driver.cores":  "200m",
        "spark.eventLog.enabled":  "false",
        "spark.executor.cores":  "4",
        "spark.executor.instances":  "3",
        "spark.executor.pyspark.memory": "1G",
        "spark.executorEnv.SPARK_EXECUTOR_MEMORY": "1G",

        "spark.hadoop.hive.imetastoreclient.factory.class":  "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory",
        "spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version": "2",

        "spark.kubernetes.authenticate.driver.serviceAccountName":  "spark",
        "spark.kubernetes.container.image.pullPolicy":  "Always",
        "spark.kubernetes.driver.limit.cores":  "1",
        "spark.kubernetes.executor.limit.cores":  "1",
        "spark.kubernetes.executor.request.cores":  "1",
        "spark.kubernetes.memoryOverheadFactor":  "0.1",
        "spark.kubernetes.pyspark.pythonVersion":  "3",


        "spark.kubernetes.namespace":"{% raw %}{{ macros.env() }}{% endraw %}", 
        "spark.kubernetes.container.image": "{% raw %}{{ {% endraw %} macros.image('{{ cookiecutter.project_name }}'){% raw %} }}{% endraw %}",
        "spark.kubernetes.authenticate.caCertFile": "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt",
        "spark.kubernetes.authenticate.oauthTokenFile": "/var/run/secrets/kubernetes.io/serviceaccount/token",
        "spark.kubernetes.authenticate.driver.serviceAccountName": "spark",
        #TODO figure out this
        #"spark.driver.host","", # DRIVER_POD_HOSTNAME)
        #"spark.driver.port","", # int(DRIVER_POD_PORT))

    }
)