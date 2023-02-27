import logging
import yaml
import os

from p_terraformer.config.cli_conf import profile_check

def add_datadog_profile():
    # TODO: Write summary
    """_summary_

    Args:
        resource_id (str):  aws resource id
        resource (str):     aws resource name
    """
    # TODO: Make it possible to retrieve from the util
    p_terraformer_config_folder = os.getenv("HOME")+"/.p_terraformer"
    os.makedirs(p_terraformer_config_folder, exist_ok=True)
    p_terraformer_config_path=p_terraformer_config_folder+"/config.yaml"

    if not os.path.exists(p_terraformer_config_path):
        with open(p_terraformer_config_path, "w") as f:
            f.write("profile: []\n")

    # TODO: If there is a profile with the same name, make it an update.
    data=profile_check()
    profile_name=input("Please enter a profile name >")
    api_key=input("secret manager api_key >")
    app_key=input("secret manager app_key >")
    if profile_name == "" or api_key == "" or app_key == "":
        logging.info("profile_name or api_key or app_key None")
        return
    result = [d for d in data["profile"] if d['name'] == profile_name]
    if not result:
        new_data = {
            "name": profile_name,
            "api_key": api_key,
            "app_key": app_key
        }
        data["profile"].append(new_data)
        with open(p_terraformer_config_path, "w") as f:
            yaml.safe_dump(data, f, sort_keys=False)
    else:
        for i in range(len(data)):
            if data["profile"][i]["name"]==profile_name:
                data["profile"][i]["api_key"]=api_key
                data["profile"][i]["app_key"]=app_key
        with open(p_terraformer_config_path, 'w') as f:
            yaml.safe_dump(data, f, sort_keys=False)
