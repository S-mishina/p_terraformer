import logging
import subprocess

from utils.helpers import generate_filename
from utils.helpers import file_handling

def aws_resources_output(resource,resource_id):
    """_summary_

    Args:
        resource_id (str):  aws resource id
        resource (str):     aws resource name
    """
    try:
        subprocess.run(
            [
                "terraformer",
                "import",
                "datadog",
                "--resources={}".format(resource),
                "--filter={}={}".format(resource, resource_id),
            ], check=True
        )
    except subprocess.CalledProcessError:
        logging.warning("")
    dt_now=generate_filename()
    file_handling(dt_now)