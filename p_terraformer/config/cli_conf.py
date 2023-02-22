import os
import logging
import ast
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv


def getenv():
    """_summary_
    """
    load_dotenv()
    if "API_NAME" in os.environ and "APP_NAME" in os.environ:
        pass
    else:
        logging.warning(".env file is not set")
        logging.warning(
            "When generating Terraform resources in datadog, \n if secret --type aws is selected, the .env File is not set, so --api_key_secret_id and --app_key_secret_id must be set manually.\n"
        )

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