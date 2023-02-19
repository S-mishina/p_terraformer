terraform {
    required_version = "= 0.13.6"
    required_providers {
        datadog = {
            source  = "DataDog/datadog"
            version = "3.12.0"
        }
    }
}
# Import from TF_VAR_xxx environment variables
variable "datadog_api_key" {}
variable "datadog_app_key" {}

provider "datadog" {
    api_key = var.datadog_api_key
    app_key = var.datadog_app_key
}