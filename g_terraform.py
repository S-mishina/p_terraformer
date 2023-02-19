"""
This module provides a wrapper for the Terraformer,
allowing users to programmatically interact with Terraformer.
"""
from pathlib import Path
import argparse
import ast
import datetime
import logging
import os
import subprocess

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv


def main(args):
    """_summary_

    Args:
        args (Array): Getting Command Arguments
    """
    if not args.provider == "" or args.resource_id == "":
        parser.print_help()
        print("\n")
        logging.warning("not provider or not provider resource_id")
        return
    else:
        if args.provider == "datadog":
            logging.info(args.provider)
            logging.info(args.app_key_secret_id)
            logging.info(args.app_key_secret_id)
            logging.info(args.resource)
            logging.info(args.type)
            datadog_resources_output(
                args.provider,
                args.type,
                args.api_key_secret_id,
                args.app_key_secret_id,
                args.resource_id,
                args.region,
                args.resource,
            )
        else:
            logging.info(args.profile)
            logging.info(args.resource)
            logging.info(args.resource_id)

def file_handling(dt_now):
    generated_dir = Path("generated")
    generated_dir.rename(dt_now)


def datadog_resources_output(
    provider, secret_type, api_key, app_key, resource_id, region, resource
):
    """_summary_

    Args:
        provider (str): terraformer generated provider
        secret_type (str): secret type ex) aws secret manager or default
        api_key (str): --type default or aws): default api_key :ex) --type default >>{datadog api_key} OR --type aws secret manager datadog_app_key name is hogehoge/hogehoge >> input hogehoge/hogehoge
        app_key (str): --type default or aws): default app_key :ex) --type default >>{datadog app_key} OR --type aws secret manager datadog_app_key name is hogehoge/hogehoge >> input hogehoge/hogehoge
        resource_id (str): datadog resource id
        resource str): datadog resource
        region (str): aws secret manager region
    """
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime("%Y-%m-%d-%H-%M")
    if secret_type == "default":
        pass
    else:
        api_key = aws_secret_get(api_key, "api_key", region)
        app_key = aws_secret_get(app_key, "app_key", region)
    try:
        subprocess.run(
            [
                "terraformer-datadog",
                "import",
                "{}".format(provider),
                "--resources={}".format(resource),
                "--api-key={}".format(api_key),
                "--app-key={}".format(app_key),
                "--filter={}={}".format(resource, resource_id),
            ], check=True
        )
    except subprocess.CalledProcessError:
        logging.warning("")
    file_handling(dt_now)

def aws_resources_output(resource_id, resource):
    """_summary_

    Args:
        resource_id (str):  aws resource id
        resource (str):     aws resource name
    """
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime("%Y-%m-%d-%H-%M")
    try:
        subprocess.run(
            [
                "terraformer-datadog",
                "import",
                "datadog",
                "--resources={}".format(resource),
                "--filter={}={}".format(resource, resource_id),
            ], check=True
        )
    except subprocess.CalledProcessError:
        logging.warning("")
    file_handling(dt_now)


def aws_secret_get(secret_name, secret_value, region_name):
    """_summary_

    Args:
        secret_name (str): secret manager secret name ex) hogehoge/hogehoge
        secret_value(str): secret manager secret key ex) api-key
        region_name (str): secret manager region

    """
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager", region_name=region_name)
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name)
    except ClientError as e:
        raise e
    secret = get_secret_value_response["SecretString"]
    dic = ast.literal_eval(secret)
    return dic[str(secret_value)]


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    if "API_NAME" in os.environ and "APP_NAME" in os.environ:
        pass
    else:
        logging.warning(".env file is not set")
        logging.warning(
            "When generating Terraform resources in datadog, \n if secret --type aws is selected, the .env File is not set, so --api_key_secret_id and --app_key_secret_id must be set manually.\n"
        )

    parser = argparse.ArgumentParser(description="terraformer python rapper")
    subparsers = parser.add_subparsers(
        dest="provider", help="Provider Generation ex) datadog or aws"
    )
    datadog_parser = subparsers.add_parser(
        "datadog", help="Datadog terraform Generation"
    )
    secret_parser = datadog_parser.add_subparsers(dest="subcommand")

    # DATADOG
    secret_parser = secret_parser.add_parser(
        "secret", help="datadog resource generation terraformer secret type"
    )
    secret_parser.add_argument(
        "-t", "--type", help="secret type default or aws", choices=["default", "aws"]
    )
    secret_parser.add_argument(
        "--api_key_secret_id",
        type=str,
        default=os.getenv("API_NAME"),
        help="(--type default or aws): default app_key :ex) --type default >>{datadog app_key} OR --type aws secret manager datadog_app_key name is hogehoge/hogehoge >> input hogehoge/hogehoge",
    )
    secret_parser.add_argument(
        "--app_key_secret_id",
        type=str,
        default=os.getenv("APP_NAME"),
        help="(--type default or aws): default api_key :ex) --type default >>{datadog api_key} OR --type aws secret manager datadog_api_key name is hogehoge1/hogehoge1 >> input hogehoge1/hogehoge1",
    )
    secret_parser.add_argument(
        "--region",
        type=str,
        default="ap-northeast-1",
        help="(--type aws): default aws region ap-northeast-1 :ex) secret manager region ap-northeast-1 >> input ap-northeast-1",
    )
    secret_parser.add_argument(
        "--resource",
        type=str,
        default="dashboard",
        help="default datadog resource dashboard   :ex) datadog resource is monitor >> input monitor",
    )
    secret_parser.add_argument(
        "--resource_id",
        type=str,
        help="datadog resource id :ex) datadog resource id is xxxxx >> input resource id xxxxx",
    )

    # AWS
    aws_parser = subparsers.add_parser("aws", help="AWS terraform Generation")
    aws_parser.add_argument(
        "--profile", type=str, default="default", help="default aws profile default"
    )
    aws_parser.add_argument(
        "--resource",
        type=str,
        default="dashboard",
        help="default aws resource vpc :ex) datadog resource is vpc >> input vpc",
    )
    aws_parser.add_argument(
        "--resource_id",
        type=str,
        help="datadog resource id :ex) datadog resource id is xxxxx >> input resource id xxxxx",
    )
    args = parser.parse_args()
    main(args)
