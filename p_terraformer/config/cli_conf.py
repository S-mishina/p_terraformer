import ast
import boto3
from botocore.exceptions import ClientError
import os
import yaml

def profile_check():
    p_terraformer_config_folder = os.getenv("HOME")+"/.p_terraformer"
    p_terraformer_config_path=p_terraformer_config_folder+"/config.yaml"
    if not os.path.exists(p_terraformer_config_path):
        os.makedirs(p_terraformer_config_folder, exist_ok=True)
        init_yml = {'profile': []}
        with open(p_terraformer_config_path, 'w') as file:
            yaml.dump(init_yml, file, sort_keys=False)
    with open(p_terraformer_config_path, "r") as f:
        data = yaml.safe_load(f)
    return data

def aws_secret_get(secret_name, secret_value, region_name):
    """_summary_
    Retrieve data from aws secret manager
    Args:
        secret_name (str): secret manager secret name ex) hogehoge/hogehoge
        secret_value(str): secret manager secret key ex) api-key
        region_name (str): secret manager region

    """
    session = boto3.session.Session()
    if os.environ.get("TESTING_FLAG") == "True":
        client = session.client(service_name="secretsmanager", region_name=region_name, endpoint_url="http://localhost:4566")
    else:
        client = session.client(service_name="secretsmanager", region_name=region_name)
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name)
    except ClientError as e:
        raise e
    secret = get_secret_value_response["SecretString"]
    dic = ast.literal_eval(secret)
    return dic[str(secret_value)]
