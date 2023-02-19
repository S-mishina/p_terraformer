import logging
import subprocess

from utils.helpers import generate_filename
from utils.helpers import file_handling

from config.cli_conf import aws_secret_get

def datadog_resources_output(
    provider, secret_type, api_key, app_key, resource_id, region, resource
):
    """_summary_

    Args:
        provider (_type_): _description_
        secret_type (_type_): _description_
        api_key (_type_): _description_
        app_key (_type_): _description_
        resource_id (_type_): _description_
        region (_type_): _description_
        resource (_type_): _description_
    """
    if secret_type == "default":
        pass
    else:
        api_key = aws_secret_get(api_key, "api_key", region)
        app_key = aws_secret_get(app_key, "app_key", region)
    try:
        subprocess.run(
            [
                "terraformer",
                "import",
                "{}".format(provider),
                "--resources={}".format(resource),
                "--api-key={}".format(api_key),
                "--app-key={}".format(app_key),
                "--filter={}={}".format(resource, resource_id),
            ],
            check=True,
        )
    except subprocess.CalledProcessError:
        logging.warning("")
    dt_now = generate_filename()
    file_handling(dt_now)
