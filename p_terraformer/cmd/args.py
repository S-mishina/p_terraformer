import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description="p_terraformer CLI")
    subparsers = parser.add_subparsers(
        dest="provider", help="p_terraformer instructions"
    )

    # DATADOG

    # aws secret manager
    datadog_parser = subparsers.add_parser(
        "datadog", help="Datadog terraform Generation"
    )
    secret_parser = datadog_parser.add_subparsers(dest="subcommand")

    aws_secret_parser = secret_parser.add_parser(
        "aws_secret", help="datadog secret type aws secret type"
    )
    aws_secret_parser.add_argument(
        "-p", "--profile",
        type=str,
        required=True,
        help="aws secret manager profile",
    )
    aws_secret_parser.add_argument(
        "--region",
        type=str,
        default="ap-northeast-1",
        help="(--type aws): default aws region ap-northeast-1 :ex) secret manager region ap-northeast-1 >> input ap-northeast-1",
    )
    aws_secret_parser.add_argument(
        "--resource",
        type=str,
        required=True,
        help="default datadog resource dashboard   :ex) datadog resource is monitor >> input monitor",
    )
    aws_secret_parser.add_argument(
        "--resource_id",
        type=str,
        required=True,
        help="Use only to create a .tf for execution.",
    )
    aws_secret_parser.add_argument('--no-tf', action='store_true',
                    help='Do not generate .tf files')
    aws_secret_parser.add_argument(
        "--terraform_version",
        type=str,
        default="0.13.6",
        help="Use only to create a .tf for execution. default terraform version 0.13.6 ex) terraform version 0.14.11 >> input 0.14.11",
    )
    aws_secret_parser.add_argument(
        "--datadog_provider_version",
        type=str,
        default="3.12.0",
        help="Use only to create a .tf for execution. default terraform datadog provider version 3.12.0 ex) datadog provider version 3.12.0 >> input 3.12.0",
    )

    # default secret
    default_secret_parser = secret_parser.add_parser(
        "default_secret", help="datadog secret type default"
    )
    default_secret_parser.add_argument(
        "--api_key",
        type=str,
        required=True,
        help="default app_key :ex) --type default >>{datadog app_key}",
    )
    default_secret_parser.add_argument(
        "--app_key",
        type=str,
        required=True,
        help="default api_key :ex) --type default >>{datadog api_key}",
    )

    default_secret_parser.add_argument(
        "--resource",
        type=str,
        required=True,
        help="default datadog resource dashboard   :ex) datadog resource is monitor >> input monitor",
    )
    default_secret_parser.add_argument(
        "--resource_id",
        type=str,
        required=True,
        help="Use only to create a .tf for execution.",
    )
    default_secret_parser.add_argument('--no-tf', action='store_true',
                    help='Do not generate .tf files')
    default_secret_parser.add_argument(
        "--terraform_version",
        type=str,
        default="0.13.6",
        help="Use only to create a .tf for execution. default terraform version 0.13.6 ex) terraform version 0.14.11 >> input 0.14.11",
    )
    default_secret_parser.add_argument(
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
        required=True,
        help="default aws resource vpc :ex) datadog resource is vpc >> input vpc",
    )
    aws_parser.add_argument(
        "--filter",
        type=str,
        required=True,
        help="for vpc id vpc---xxxxxxxxxx, enter vpc=vpc-xxxxxxxxxxx",
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
        default="ap-northeast-1",
        help="Use only to create a .tf for execution. default aws region ap-northeast-1 ex) aws region ap-northeast-1 >> input ap-northeast-1",
    )

    #profile
    profile_parser = subparsers.add_parser("profile", help="Settings to use with p_terraformer")
    profile_parser.add_argument(
        "profile_list",
        action='store_true',
        help="Display profile list"
    )


    args = parser.parse_args()
    return args,parser,datadog_parser