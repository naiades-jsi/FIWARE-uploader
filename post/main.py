#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="Modeling component")

    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        default="config.json",
        help=u"Config file located in ./config/ directory",
    )

    parser.add_argument(
        "-w",
        "--watchdog",
        dest="watchdog",
        action='store_true',
        help=u"Ping watchdog",
    )

    # Display help if no arguments are defined
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    # Parse input arguments
    args = parser.parse_args()

    with open("config/" + args.config) as configuration:
        conf = json.load(configuration)
    
    

if __name__ == '__main__':
    main()
