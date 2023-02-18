import argparse
import subprocess

def main(args):
    if not (args.provider):
        parser.print_help()
        return
    if args.provider == "aws":
        generation_aws(args.terraform_version, args.provider_version, args.region)
    elif args.provider == "datadog":
        generation_datadog(args.terraform_version, args.provider_version)
    subprocess.run(["terraform","init"])
def generation_aws(terraform_ver, provider_ver, region):
    template = '''terraform {{
    required_version = "= {0}"
    required_providers {{
        aws = {{
            source  = "hashicorp/aws"
            version = "~> {1}"
        }}
    }}
}}
# Configure the AWS Provider
provider "aws" {{
    region = "{2}"
}}'''.format(terraform_ver, provider_ver, region)
    with open('output.tf', 'w') as f:
        f.write(template)

def generation_datadog(terraform_ver, provider_ver):
    template = '''terraform {{
    required_version = "= {0}"
    required_providers {{
        datadog = {{
            source  = "DataDog/datadog"
            version = "{1}"
        }}
    }}
}}
# Import from TF_VAR_xxx environment variables
variable "datadog_api_key" {{}}
variable "datadog_app_key" {{}}

provider "datadog" {{
    api_key = var.datadog_api_key
    app_key = var.datadog_app_key
}}'''.format(terraform_ver, provider_ver)
    with open('output.tf', 'w') as f:
        f.write(template)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='terraform generation template')
    subparsers = parser.add_subparsers(dest='provider', help='Provider Generation ex) aws, datadog')
    aws_parser = subparsers.add_parser('aws', help='AWS Provider')
    aws_parser.add_argument('-r','--region', type=str, default='us-east-1', help='default region us-east-1  ex) aws region us-east-1 >> input us-east-1')
    aws_parser.add_argument('-p','--provider_version', type=str, default='4.0', help='default version 4.0 :: ex) aws provider version 4.0 >> input 4.0')
    aws_parser.add_argument('-t','--terraform_version', type=str, default='0.14.11', help='default version 0.14.11 :: ex) terraform version 0.14.11 >> input 0.14.11')
    datadog_parser = subparsers.add_parser('datadog', help='Datadog Provider')
    datadog_parser.add_argument('-ｐ','--provider_version', type=str, default='3.12.0', help='default version 3.12.0 :: ex) datadog provider version 3.12.0 >> input 3.12.0')
    datadog_parser.add_argument('-t','--terraform_version', type=str, default='0.14.11', help='default version 0.14.11 :: ex) terraform version 0.14.11 >> input 0.14.11')
    args = parser.parse_args()
    main(args)
