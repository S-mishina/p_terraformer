import logging
import subprocess
import platform

def terraformer_install():
    operation=platform.system()
    try:
        subprocess.run(
            [
                "bash",
                "terraformer_install/setup.sh",
                "-e",
                operation,
            ], check=True
        )
    except subprocess.CalledProcessError:
        logging.warning("Could not install terraformer")