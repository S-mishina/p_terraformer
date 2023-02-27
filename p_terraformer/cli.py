"""
This module provides a wrapper for the Terraformer,
allowing users to programmatically interact with Terraformer.
"""

import logging
from p_terraformer.cmd import terraformer_install
from p_terraformer.cmd.args import parse_args
from p_terraformer.cmd.datadog_generator import datadog_cmd
from p_terraformer.cmd.p_terraformer_config_generator import add_datadog_profile

def main():
    logging.basicConfig(level=logging.INFO)
    args,parser,datadog_parser=parse_args()
    if args.provider == None:
        parser.print_help()
    elif args.provider == "datadog":
        if args.subcommand == None:
            logging.info("not Command secret or type")
            logging.info("""
                        sample Command
                        ex) p_terraformer datadog aws_secret or default_secret
                        """)
            datadog_parser.print_help()
        else:
            datadog_cmd(args)
    elif args.provider == "aws":
        pass
    elif args.provider == "profile":
        add_datadog_profile()
    elif args.provider == "terraformer_install":
        terraformer_install()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()