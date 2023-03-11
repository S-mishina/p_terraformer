import logging
import subprocess
from p_terraformer.utils.helpers import generate_filename
from p_terraformer.utils.helpers import file_handling
from p_terraformer.cmd.terraform_generator import *
from p_terraformer.config.cli_conf import *

def datadog_cmd(args):
    # Whether to generate .tf files
    if not args.no_tf:
        generation_datadog(args.terraform_version, args.datadog_provider_version)
    datadog_resources_output(args)

def datadog_resources_output(args):
    # TODO: Write summary
    """_summary_
    This program generates terraform code for datadog using terraformer
    Args:
        args (array): argument
    """
    if args.subcommand == "default_secret":
        api_key = args.api_key
        app_key = args.app_key
    else:
        data=profile_check()
        if data!=None:
            result = [d for d in data["profile"] if d['name'] == args.profile]
        else:
            result=None
        if not result:
            logging.info("""
            The profile does not exist.
            sample Command: > p_terraformer profile <profile name>
                        """)
            return
        else:
            api_key = aws_secret_get(result[0]["api_key"], "api_key", args.region)
            app_key = aws_secret_get(result[0]["app_key"], "app_key", args.region)
    try:
        subprocess.run(
            [
                "terraformer",
                "import",
                "{}".format(args.provider),
                "--resources={}".format(args.resource),
                "--api-key={}".format(api_key),
                "--app-key={}".format(app_key),
                "--filter={}={}".format(args.resource, args.resource_id),
            ],
            check=True,
        )
    except subprocess.CalledProcessError:
        logging.warning("Execution failed.")
    dt_now = generate_filename()
    file_handling(dt_now)
