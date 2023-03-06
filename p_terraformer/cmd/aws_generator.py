import logging
import subprocess

from p_terraformer.cmd.terraform_generator import generation_aws

from p_terraformer.utils.helpers import generate_filename
from p_terraformer.utils.helpers import file_handling

def aws_cmd(args):
    if not args.no_tf:
        generation_aws(args.terraform_ver, args.provider_ver, args.region)
    aws_resources_output(args.terraform_version, args.aws_provider_version,args.aws_region)

def aws_resources_output(args):
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
                "aws",
                "--resources={}".format(args.resource),
                "--filter={}={}".format(args.resource, args.resource_id),
            ], check=True
        )
    except subprocess.CalledProcessError:
        logging.warning("Execution failed.")
    dt_now=generate_filename()
    file_handling(dt_now)