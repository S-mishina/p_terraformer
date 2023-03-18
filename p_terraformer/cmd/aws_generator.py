import logging
import subprocess

from p_terraformer.cmd.terraform_generator import generation_aws
from p_terraformer.utils.helpers import file_handling , terraform_init
from p_terraformer.utils.helpers import generate_filename
from p_terraformer.utils.helpers import file_handling

def aws_cmd(args):
    if not args.no_tf:
        generation_aws(args.terraform_version, args.aws_provider_version, args.aws_region)
    aws_resources_output(args)

def aws_resources_output(args):
    """_summary_
    Code to run terraformer to generate aws resource

    Args:
        filter (str):       aws filter
        resource (str):     aws resource name
    """
    terraform_init()
    try:
        subprocess.run(
            [
                "terraformer",
                "import",
                "aws",
                "--resources={}".format(args.resource),
                "--filter={}".format(args.filter),
                "--regions={}".format(args.aws_region),
                "--profile={}".format(args.aws_profile),
            ], check=True
        )
        dt_now=generate_filename()
        file_handling(dt_now)
    except:
        logging.warning("Execution failed.")
        return