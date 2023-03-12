def generation_aws(terraform_ver, provider_ver, region):
    """_summary_
    Program to generate .tf for aws provider.
    Args:
        terraform_ver (_type_): _description_
        provider_ver (_type_): _description_
        region (_type_): _description_
    """

    template = """terraform {{
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
}}""".format(
        terraform_ver, provider_ver, region
    )
    with open("main.tf", "w") as f:
        f.write(template)


def generation_datadog(terraform_ver, provider_ver):
    """_summary_
    Program to generate .tf for datadog provider.
    Args:
        terraform_ver (_type_): _description_
        provider_ver (_type_): _description_
    """
    template = """terraform {{
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
}}""".format(
        terraform_ver, provider_ver
    )
    with open("main.tf", "w") as f:
        f.write(template)

