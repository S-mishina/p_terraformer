from pathlib import Path
import datetime
import subprocess
import logging

def generate_filename():
    """_summary_
    """
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime("%Y-%m-%d-%H-%M")
    return dt_now

def file_handling(dt_now):
    """_summary_

    Args:
        dt_now (str): _description_
    """
    generated_dir = Path("generated")
    generated_dir.rename(dt_now)

def terraform_init():
    """_summary_
    Execute terraform init
    """
    try:
        subprocess.run(["terraform","init"])
    except subprocess.CalledProcessError:
        logging.warning("terraform init did not work!")
