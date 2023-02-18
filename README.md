# terrafomrmer-python-wrapper
A python wrapper for Terraformer.

## Files to be prepared

```:directory structure
├── README.md
├── .env << this
├── g_terraform.py
└── template_tf.py
```

```:.env
# .env
API_NAME={api_secret__id}
APP_NAME={app_secret__id}
```

## How to execute each command

### Usage

* template_tf.py

```:help
usage: template_tf.py [-h] {aws,datadog} ...

terraform generation template

positional arguments:
  {aws,datadog}  Provider Generation ex) aws, datadog
    aws          AWS Provider
    datadog      Datadog Provider

options:
  -h, --help     show this help message and exit

usage: template_tf.py datadog [-h] [-ｐ PROVIDER_VERSION] [-t TERRAFORM_VERSION]

options:
  -h, --help            show this help message and exit
  -ｐ PROVIDER_VERSION, --provider_version PROVIDER_VERSION
                        default version 3.12.0 :: ex) datadog provider version 3.12.0 >> input 3.12.0
  -t TERRAFORM_VERSION, --terraform_version TERRAFORM_VERSION
                        default version 0.14.11 :: ex) terraform version 0.14.11 >> input 0.14.11
```

* g_terraform.py

```:help
usage: datadog_dashboard.py [-h] {datadog} ...

terraformer rapper

positional arguments:
  {datadog}   Provider Generation ex) datadog
    datadog   Datadog terraform Generation

options:
  -h, --help  show this help message and exit

usage: g_terraform.py datadog [-h] [--api_key_secret_id API_KEY_SECRET_ID]
                              [--app_key_secret_id APP_KEY_SECRET_ID]
                              [--region REGION] [--resource RESOURCE]
                              [--resource_id RESOURCE_ID]

options:
  -h, --help            show this help message and exit
  --api_key_secret_id API_KEY_SECRET_ID
                        default app_key :ex) secret manager datadog_app_key name is
                        hogehoge/hogehoge >> input hogehoge/hogehoge
  --app_key_secret_id APP_KEY_SECRET_ID
                        default api_key :ex) secret manager datadog_api_key name is
                        hogehoge1/hogehoge1 >> input hogehoge1/hogehoge1
  --region REGION       default aws region ap-northeast-1 :ex) secret manager region
                        ap-northeast-1 >> input ap-northeast-1
  --resource RESOURCE   default datadog resource dashboard :ex) datadog resource is
                        monitor >> input monitor
  --resource_id RESOURCE_ID
                        datadog resource id :ex) datadog resource id is xxxxx >>
                        input resource id xxxxx
```

