from cmath import inf
from post_FIWARE import SendData

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

    # Display help if no arguments are defined
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    # Parse input arguments
    args = parser.parse_args()
    #print("here", flush=True)
    with open("config/" + args.config) as configuration:
        conf = json.load(configuration)
    
    config = conf["config"]

    if("influx_config" in conf):
        influx_config = conf["influx_config"]
    else:
        influx_config = None

    braila_anomaly = SendData(config, config_influx=influx_config)

    braila_anomaly.send()

if (__name__ == '__main__'):
    main()
