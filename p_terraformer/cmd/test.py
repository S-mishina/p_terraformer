from p_terraformer.config.cli_conf import profile_check
import yaml

data=profile_check()
for i in range(len(data)):
    if data["profile"][i]["name"]=="test":
        data["profile"][i]["api_key"]="test1"
        data["profile"][i]["app_key"]="test1"
with open(p_terraformer_config_path, 'w') as f:
    yaml.safe_dump(data, f, sort_keys=False)