import logging
import requests
from typing import Optional

from {{ cookiecutter.module_name }}.jobs import entrypoint


@entrypoint("sample")
def run(env: str, date: str):
    """Main ETL script definition.

    :return: None
    """
    # execute ETL pipeline
    data = extract_data()
    logging.info("Downloaded the weather info, now loading it")
    if data is None:
        logging.error("Received no weather data")
    load_data(data, env)


def extract_data() -> Optional[str]:
    """
    Gets the data from the open weather map api and returns the result.
    :return: The weather data
    """
    return requests.get(
        "https://samples.openweathermap.org/data/2.5/weather?q=Leuven&appid=b6907d289e10d714a6e88b30761fae22"
    )


def load_data(data: str, env: str):
    """Writes the data on s3

    :param data: The string to write
    :param env: The environment
    :return: None
    """
    print(data)
    # Uncomment the following block to write to s3
    # s3 = boto3.resource("s3")
    # s3_object = s3.Object("DEFAULT_S3", f"raw/weather/ds={config.date}/weather.json")
    # s3_object.put(Body=r.text)
