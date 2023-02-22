"""
This module provides a wrapper for the Terraformer,
allowing users to programmatically interact with Terraformer.
"""
import argparse
import logging
import os

from p_terraformer.cmd.terraform_generator import generation_datadog
from p_terraformer.cmd.terraform_generator import generation_aws
from p_terraformer.cmd.datadog_generator import datadog_resources_output

from p_terraformer.config.cli_conf import getenv


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
    else:
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

def main():
    logging.basicConfig(level=logging.INFO)
    # getenv()
    parser = argparse.ArgumentParser(description="terraformer python rapper")
    subparsers = parser.add_subparsers(
        dest="provider", help="Provider Generation ex) datadog or aws"
    )
    datadog_parser = subparsers.add_parser(
        "datadog", help="Datadog terraform Generation"
    )
    secret_parser = datadog_parser.add_subparsers(dest="subcommand")

    # DATADOG
    secret_parser = secret_parser.add_parser(
        "secret", help="datadog resource generation terraformer secret type"
    )
    secret_parser.add_argument(
        "-t", "--type", help="secret type default or aws", choices=["default", "aws"]
    )
    secret_parser.add_argument(
        "--api_key_secret_id",
        type=str,
        default=os.getenv("API_NAME"),
        help="(--type default or aws): default app_key :ex) --type default >>{datadog app_key} OR --type aws secret manager datadog_app_key name is hogehoge/hogehoge >> input hogehoge/hogehoge",
    )
    secret_parser.add_argument(
        "--app_key_secret_id",
        type=str,
        default=os.getenv("APP_NAME"),
        help="(--type default or aws): default api_key :ex) --type default >>{datadog api_key} OR --type aws secret manager datadog_api_key name is hogehoge1/hogehoge1 >> input hogehoge1/hogehoge1",
    )
    secret_parser.add_argument(
        "--region",
        type=str,
        default="ap-northeast-1",
        help="(--type aws): default aws region ap-northeast-1 :ex) secret manager region ap-northeast-1 >> input ap-northeast-1",
    )
    secret_parser.add_argument(
        "--resource",
        type=str,
        default="dashboard",
        help="default datadog resource dashboard   :ex) datadog resource is monitor >> input monitor",
    )
    secret_parser.add_argument(
        "--resource_id",
        type=str,
        default="dashboard",
        help="Use only to create a .tf for execution.",
    )
    secret_parser.add_argument('--no-tf', action='store_true',
                    help='Do not generate .tf files')
    secret_parser.add_argument(
        "--terraform_version",
        type=str,
        default="0.13.6",
        help="Use only to create a .tf for execution. default terraform version 0.13.6 ex) terraform version 0.14.11 >> input 0.14.11",
    )
    secret_parser.add_argument(
        "--datadog_provider_version",
        type=str,
        default="3.12.0",
        help="Use only to create a .tf for execution. default terraform datadog provider version 3.12.0 ex) datadog provider version 3.12.0 >> input 3.12.0",
    )

    # AWS
    aws_parser = subparsers.add_parser("aws", help="AWS terraform Generation")
    aws_parser.add_argument(
        "--aws_profile",
        type=str,
        default="default",
        help="default aws profile default"
    )
    aws_parser.add_argument(
        "--resource",
        type=str,
        default="dashboard",
        help="default aws resource vpc :ex) datadog resource is vpc >> input vpc",
    )
    aws_parser.add_argument(
        "--resource_id",
        type=str,
        help="datadog resource id :ex) datadog resource id is xxxxx >> input resource id xxxxx",
    )
    aws_parser.add_argument('--no-tf', action='store_true',
                    help='Do not generate .tf files')
    aws_parser.add_argument(
        "--terraform_version",
        type=str,
        default="0.13.6",
        help="Use only to create a .tf for execution. default terraform version 0.13.6 ex) terraform version 0.14.11 >> input 0.14.11",
    )
    aws_parser.add_argument(
        "--aws_provider_version",
        type=str,
        default="3.12.0",
        help="Use only to create a .tf for execution. default terraform aws provider version 4.0 ex) datadog provider version 4.0 >> input 4.0",
    )
    aws_parser.add_argument(
        "--aws_region",
        type=str,
        default="us-east-1",
        help="Use only to create a .tf for execution. default aws region us-east-1 ex) aws region us-east-1 >> input us-east-1",
    )
    args = parser.parse_args()
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