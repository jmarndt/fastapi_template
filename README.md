# FastAPI Template
This repo is a template for FastAPI. It provides a clean and modular directory structure, along with a basic `ping` endpoint to confirm functionality. Included is a `run_api.py` script to make it simple to run the API locally for development or in prodcution.

## Setup
Before running the API a few dependencies need to be installed (FastAPI and Uvicorn). It is recommended to do this in a virtual environment, but doing so is optional.

Create virtual environment (and activate it):
```
python3 -m venv .env && source .env/bin/activate
```

Update pip and install requirements:
```
python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
```

### API Name
There is a variable `API_NAME`. This is important to note since by default the API base route will be based on this variable and is also used in the `create_systemd_service.py` when creating a service.

## Running
Simply run the `run_api.py` script to start the API in dev mode:
```
python3 run_api.py
```

To see additional options run it with the help flag:
```
python3 run_api.py -h
```

### As systemd
For systems with systemd, you can create a service to run the API by running the `create_systemd_service.py` script. This script will utilize the `run_api.py` script with the `--prod` flag, so make sure to edit the `run_api.py` settings to your liking, or edit the `create_systemd_service.py` accordingly.