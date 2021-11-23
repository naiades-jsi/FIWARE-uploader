# BUILDING: docker build -t <container_name> .
# RUNNING: docker run <container_name> <python_program_path> <config_file_path>
# e.g. docker run --network="host" fiware_uploader_alicante_consumption
FROM ubuntu:20.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /
# CMD ["python3", "main.py", "-c", "deployment/alicante_consumption.json"]
# CMD ["python3", "main.py", "-c", "deployment/braila_ad.json"]
# CMD ["python3", "main.py", "-c", "deployment/braila_leak.json"]
# CMD ["python3", "main.py", "-c", "deployment/braila_leakage_group.json"]
CMD ["python3", "main.py", "-c", "deployment/carouge_watering.json"]
