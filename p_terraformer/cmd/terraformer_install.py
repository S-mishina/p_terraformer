import logging
import subprocess
import platform

def terraformer_install():
    operation=platform.system()
    try:
        if operation is "Darwin" or "Linux":
            subprocess.run(
                [
                    """curl -LO https://github.com/GoogleCloudPlatform/terraformer/releases/download/$(curl -s https://api.github.com/repos/GoogleCloudPlatform/terraformer/releases/latest | grep tag_name | cut -d '"' -f 4)/terraformer-all-"{}"-amd64""".format(operation)
                ], check=True
            )
            subprocess.run(
                [
                    "chmod",
                    "+x",
                    """terraformer-all-"{}"-amd64""".format(operation)
                ], check=True
            )
    except subprocess.CalledProcessError:
        logging.warning("Could not install terraformer")
