"""
This module provides a wrapper for the Terraformer,
allowing users to programmatically interact with Terraformer.
"""

import logging


from p_terraformer.cmd import *
from p_terraformer.cmd.terraform_generator import *
from p_terraformer.cmd.datadog_generator import *
from p_terraformer.cmd.args import *

from p_terraformer.config.cli_conf import *


def cli(args):
    """_summary_

    Args:
        args (Array): Getting Command Arguments
    """
    if args.provider == "datadog":
        logging.info(
            "provider:{0},app_key_secret_id:{1},app_key_secret_id:{2},resource:{3},resource id:{4}".format(
                args.provider,
                args.api_key_secret_id,
                args.app_key_secret_id,
                args.resource,
                args.resource_id,
            )
        )
        # Whether to generate .tf files
        if args.no_tf:
            pass
        else:
            generation_datadog(args.terraform_version, args.datadog_provider_version)
        datadog_resources_output(
            args.provider,
            args.type,
            args.api_key_secret_id,
            args.app_key_secret_id,
            args.resource_id,
            args.region,
            args.resource,
        )
    elif args.provider == "aws":
        # Whether to generate .tf files
        logging.info(
            "aws profile:{0},aws resource:{1},aws resource id{2}".format(
                args.aws_profile, args.resource, args.resource_id
            )
        )
        if args.no_tf:
            pass
        else:
            generation_aws(args.terraform_version, args.aws_provider_version,args.aws_region)
    else:
        if args.provider=="profile" and args.subcommand==None:
            pass
        elif args.provider=="profile" and args.profile_list:
            pass


def main():
    logging.basicConfig(level=logging.INFO)
    make_config_yaml()
    args,parser,secret_parser=parse_args()
    if args.provider==None:
        parser.print_help()
        return
    if args.provider=="datadog" and args.subcommand==None:
        secret_parser.print_help()
        return
    else:
        cli(args)


if __name__ == "__main__":
    main()