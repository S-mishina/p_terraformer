#!/bin/bash
curl -LO https://github.com/GoogleCloudPlatform/terraformer/releases/download/$(curl -s https://api.github.com/repos/GoogleCloudPlatform/terraformer/releases/latest | grep tag_name | cut -d '"' -f 4)/terraformer-aws-darwin-amd64
curl -LO https://github.com/GoogleCloudPlatform/terraformer/releases/download/$(curl -s https://api.github.com/repos/GoogleCloudPlatform/terraformer/releases/latest | grep tag_name | cut -d '"' -f 4)/terraformer-datadog-darwin-amd64
chmod +x terraformer-datadog-darwin-amd64
chmod +x terraformer-aws-darwin-amd64
sudo mv terraformer-datadog-darwin-amd64 /usr/local/bin/terraformer-datadog
sudo mv terraformer-aws-darwin-amd64 /usr/local/bin/terraformer-aws