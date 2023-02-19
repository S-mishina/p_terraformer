"""
This module provides a wrapper for the Terraformer,
allowing users to programmatically interact with Terraformer.
"""
import os
import argparse
import logging

from command.datadog_generator import datadog_resources_output


def main(args):
    """_summary_

    Args:
        args (Array): Getting Command Arguments
    """
    if not args.provider == "" or args.resource_id == "":
        parser.print_help()
        print("\n")
        logging.warning("not provider or not provider resource_id")
        return
    else:
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
            logging.info(args.profile)
            logging.info(args.resource)
            logging.info(args.resource_id)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
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
        help="datadog resource id :ex) datadog resource id is xxxxx >> input resource id xxxxx",
    )

    # AWS
    aws_parser = subparsers.add_parser("aws", help="AWS terraform Generation")
    aws_parser.add_argument(
        "--profile", type=str, default="default", help="default aws profile default"
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
    args = parser.parse_args()
    main(args)
