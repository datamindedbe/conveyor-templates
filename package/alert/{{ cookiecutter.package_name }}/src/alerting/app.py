import argparse
import json
import logging
import sys


class Config:
    def __init__(
        self,
        date: str,
        state: str,
        task: str,
        dag: str,
        env: str,
        start_date: str,
        try_number: int,
    ) -> None:
        self.date = date
        self.state = state
        self.task = task
        self.dag = dag
        self.env = env
        self.start_date = start_date
        self.try_number = try_number


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description="Building alert hook")
    parser.add_argument(
        "--state",
        help="state of the task triggering the alert",
        default="failed",
        dest="state",
    )
    parser.add_argument(
        "--task", help="the task triggering the alert", dest="task", required=True
    )
    parser.add_argument(
        "--dag",
        help="the dag of which the task triggering the alert is part",
        required=True,
        dest="dag",
    )
    parser.add_argument(
        "--env",
        help="the environment in which the task triggering the alert is running",
        required=True,
        dest="env",
    )
    parser.add_argument(
        "--execution-date",
        help="execution date",
        required=True,
        dest="execution_date",
    )
    parser.add_argument(
        "--start-date",
        help="start time of the task that failed",
        required=True,
        dest="start_date",
    )
    parser.add_argument(
        "--try-number",
        type=int,
        help="The amount of times the failed task has been retried",
        default=-1,
        dest="try_number",
    )
    args = parser.parse_args()
    return Config(
        date=args.execution_date,
        state=args.state,
        task=args.task,
        dag=args.dag,
        env=args.env,
        start_date=args.start_date,
        try_number=args.try_number,
    )


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    config = parse_args()

    logging.info(f"Triggering some complex alert using: {json.dumps(config.__dict__)}")
