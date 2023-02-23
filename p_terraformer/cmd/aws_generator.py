import logging
import subprocess

from p_terraformer.utils.helpers import generate_filename
from p_terraformer.utils.helpers import file_handling

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
        # TODO: include an error phrase
        logging.warning("")
    dt_now=generate_filename()
    file_handling(dt_now)