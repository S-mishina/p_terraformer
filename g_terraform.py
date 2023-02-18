from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os
import datetime
import boto3
import ast
import subprocess
import argparse
import logging

def main(args):
    if not args.provider or not args.resource_id:
        parser.print_help()
        print("\n")
        logging.warning("not provider or not provider resource_id")
        return
    else:
        if args.provider =="datadog":
            logging.info(args.provider)
            logging.info(args.app_key_secret_id)
            logging.info(args.app_key_secret_id)
            logging.info(args.resource)
            datadog_secret(args.api_key_secret_id, args.app_key_secret_id, args.resource_id, args.region, args.resource)


def datadog_secret(api_key, app_key, resource_id, region, resource):
    dt_now = datetime.datetime.now()
    dt_now=dt_now.strftime("%Y-%m-%d-%H-%M")
    datadog_api_key = get_secret(api_key,"api_key", region)
    datadog_app_key = get_secret(app_key,"app_key", region)
    subprocess.run(["terraformer-datadog", "import","datadog","--resources={}".format(resource),"--api-key={}".format(datadog_api_key),"--app-key={}".format(datadog_app_key),"--filter={}={}".format(resource,resource_id)])
    subprocess.run(["mv","generated",str(dt_now)])
    subprocess.run(["open", str(dt_now)])


def get_secret(secret_name, Subscript, region_name):
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e
    secret = get_secret_value_response["SecretString"]
    dic = ast.literal_eval(secret)
    return dic[str(Subscript)]

if __name__ == "__main__":
    load_dotenv()
    if "API_NAME" in os.environ and "APP_NAME" in os.environ:
        pass
    else:
        logging.warning(".env file is not set")
    parser = argparse.ArgumentParser(description="terraformer rapper")
    subparsers = parser.add_subparsers(dest="provider", help="Provider Generation ex) datadog")
    datadog_parser = subparsers.add_parser("datadog", help="Datadog terraform Generation")
    datadog_parser.add_argument("--api_key_secret_id", type=str, default=os.getenv("API_NAME"), help="default app_key :ex) secret manager datadog_app_key name is hogehoge/hogehoge >> input hogehoge/hogehoge")
    datadog_parser.add_argument("--app_key_secret_id", type=str, default=os.getenv("APP_NAME"), help="default api_key :ex) secret manager datadog_api_key name is hogehoge1/hogehoge1 >> input hogehoge1/hogehoge1")
    datadog_parser.add_argument("--region", type=str, default="ap-northeast-1", help="default aws region ap-northeast-1 :ex) secret manager region ap-northeast-1 >> input ap-northeast-1")
    datadog_parser.add_argument("--resource", type=str, default="dashboard", help="default datadog resource dashboard   :ex) datadog resource is monitor >> input monitor")
    datadog_parser.add_argument("--resource_id", type=str, help="datadog resource id :ex) datadog resource id is xxxxx >> input resource id xxxxx")
    args = parser.parse_args()
    main(args)
