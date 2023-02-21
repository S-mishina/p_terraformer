from pathlib import Path
import datetime
import subprocess
import logging

def generate_filename():
    """_summary_

    Returns:
        _type_: _description_
    """
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime("%Y-%m-%d-%H-%M")
    return dt_now

def file_handling(dt_now):
    """_summary_

    Args:
        dt_now (_type_): _description_
    """
    # generated_dir = Path("generated")
    # generated_dir.rename(dt_now)

def terraform_init():
    """_summary_
    """
    try:
        subprocess.run(["terraform","init"])
    except subprocess.CalledProcessError:
        logging.warning("")
