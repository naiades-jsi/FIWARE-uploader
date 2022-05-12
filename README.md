# FIWARE-uploader for NAIADES

FIWARE uploader for NAIADES bridges the gap between JSI's stream analytics platform and NAIADES framework.

NAIADES framework internally manages data flows with Kafka topics. FIWARE uploader listens at a particular topic in Kafka and uploads the data shared via that topic to the NAIDES platform in a uniform way.

Additionally, FIWARE-uploader is able to upload the data from Kafka topics into an InfluxDB, which can be used as a persistent data storage for additional analytics or visualization purposes.

# Configuration

A generic configuration format is given below. Concrete configurations can contain arbitrary parameters which are use-case specific.

The config JSON is structured into two parts: `config` (for FIWARE-uploader) and `influx_config` (for InfluxDB uploader).

```JSON
{
    "config": {
        "name": "instance_name",
        "api_user": "user",
        "api_pass": "pass",
        "time_name": "timestamp",
        "time_format": "ms",
        "data_name": ["value"],
        "kafka":{
            "topics": [
                "topic_name_1",
                "topic_name_2",
            ],
            "bootstrap_servers": "kafka:9092",
            "offset": "earliest"
        },
        "fiware":{
            "headers": {
                "Fiware-Service": "servicename",
                "Content-Type": "application/json"
            },
            "update": true,
            "url": "http://endpoint.server/v2/entities/",
            "id": "urn:ngsi-ld:XX:YY-name",
            "sensor_name_re": "sensor_name_(.+)_measurement"
        }
    },
    "influx_config": {
        "token" : "token",
        "org" : "influxorg",
        "url" : "http://localhost:8086/"
    }
}
```

For FIWARE-uploader config, the following fields are required:

* `name`: name of the uploader instance (there can be more)
* `api_user`: user for FIWARE
* `api_pass`: password for FIWARE
* `time_name`: field providing timestamp information
* `time_format`: format of the timestamp (`ms` for UNIX in milliseconds, `s` for UNIX in seconds)
* `data_name`: field in the Kafka structure that contains value
* `kafka`: Kafka configuration, which contains array of `topics` and fields for `bootstrap_servers` (URL of the service) and `offset` strategy (which can be `earliest` or TODO)
* `fiware`: configuration for FIWARE uploader, which will include definition of `headers`, `url` of the service, `id` of the FIWARE entity to send the data to and `sensor_name_re` regular expression, which is used to generate concrete sensor name based on data in the Kafka topic

For InfluxDB config there are well specified fields:

* `token`: token for connection to InfluxDB
* `org`: InfluxDB organisation name
* `url`: URL for InfluxDB endpoint

Custom fields for particular data types:
* __TODO__


# Development
__TODO__

# Testing

A particular configuraton can be run on a development system using:

```
python3 main.py -c deployment/config.json
```

We suggest running the tests within production docker environment (see below).


# Building the service/production image
The service should be run within Docker, enabling KSI signature of the data (provided by NAIADES; more data [here](https://gitlab.distantaccess.com/naiades/naiades-platform-poc/-/wikis/home)).

Dockerfile is provided in the home directory. Build the image with the following command:
`docker build -t <image_name> .` from home directory. You also need permissions for e3ailab docker hub repository, to be able to pull base image with KSI.