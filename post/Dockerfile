# BUILDING: docker build -t <container_name> .
# RUNNING: docker run <container_name> <python_program_path> <config_file_path>
# e.g. docker run --network="host" fiware_uploader_alicante_consumption
FROM e3ailab/ksi-base
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /

# CMD ["python3", "main.py", "-c", "deployment/alicante_consumption.json"]
# e3ailab/uploader_alicante_consumption_ircai

# CMD ["python3", "main.py", "-c", "deployment/alicante_ad.json"]
# e3ailab/uploader_alicante_ad_ircai

# CMD ["python3", "main.py", "-c", "deployment/alicante_salinity_ms.json"]
# e3ailab/uploader_alicante_salinity_ms_ircai

# CMD ["python3", "main.py", "-c", "deployment/braila_ad.json"]
# e3ailab/uploader_braila_ad_ircai

# CMD ["python3", "main.py", "-c", "deployment/braila_leakage_accurate.json"]

# CMD ["python3", "main.py", "-c", "deployment/braila_leakage_approximate.json"]

# e3ailab/uploader_braila_consumption_ircai
# CMD ["python3", "main.py", "-c", "deployment/braila_consumption.json"]

# CMD ["python3", "main.py", "-c", "deployment/braila_ad_ms.json"]
# e3ailab/uploader_braila_ad_ms_ircai

# CMD ["python3", "main.py", "-c", "deployment/carouge_watering.json"]
# e3ailab/uploader_carouge_watering_ircai