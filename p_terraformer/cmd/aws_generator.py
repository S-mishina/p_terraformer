import logging
import subprocess

from p_terraformer.utils.helpers import generate_filename
from p_terraformer.utils.helpers import file_handling

def datadog_cmd(args):
    if not args.no_tf:
        aws_resources_output(args.terraform_version, args.aws_provider_version,args.aws_region)

def aws_resources_output(resource,resource_id):
    # TODO: Write summary
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