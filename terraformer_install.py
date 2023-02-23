import logging
import subprocess
import platform

operation=platform.system()
try:
    subprocess.run(
        [
            "bash",
            "terraformer_install/setup.sh",
            "-e",
            "datadog",

        ], check=True
    )
except subprocess.CalledProcessError:
    logging.warning("Could not install terraformer")
