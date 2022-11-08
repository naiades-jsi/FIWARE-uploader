# imports
from cmath import inf
from post_FIWARE import SendData

import argparse
import sys
import json
import logging

# setting version
fiware_uploader_version = "1.0.9"

# logging
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", level=logging.INFO)

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
    with open("config/" + args.config) as configuration:
        conf = json.load(configuration)

    config = conf["config"]

    if("influx_config" in conf):
        influx_config = conf["influx_config"]
    else:
        influx_config = None

    LOGGER.info("FIWARE-uploader v%s", fiware_uploader_version)
    LOGGER.info("Starting FIWARE-upload for %s", args.config)
    worker = SendData(config, config_influx=influx_config)
    worker.send()

if (__name__ == '__main__'):
    main()
