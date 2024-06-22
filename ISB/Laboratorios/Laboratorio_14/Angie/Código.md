import time
import hmac
import hashlib
import json
import requests
import random

def upload_ei(_name_label, _values, hmac_key, api_key):
    HMAC_KEY = hmac_key
    API_KEY = api_key
    emptySignature = ''.join(['0'] * 64)

    # Assuming Fs is your sampling frequency in Hz
    Fs = 360
    Ts = (1 / Fs) * 1000

    data = {
        "protected": {
            "ver": "v1",
            "alg": "HS256",
            "iat": time.time()  # epoch time, seconds since 1970
        },
        "signature": emptySignature,
        "payload": {
            "device_name": "ac:87:a3:0a:2d:1b",
            "device_type": "NANO33BLE",
            "interval_ms": Ts,
            "sensors": [
                { "name": "Volts", "units": "adu/mv" }
            ],
            "values": _values
        }
    }

    # Encode in JSON
    encoded = json.dumps(data)

    # Sign message
    signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg=encoded.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

    # Set the signature again in the message, and encode again
    data['signature'] = signature
    encoded = json.dumps(data)

    # Upload the file
    res = requests.post(
        url='https://ingestion.edgeimpulse.com/api/training/data',
        data=encoded,
        headers={
            'Content-Type': 'application/json',
            'x-file-name': _name_label,
            'x-api-key': API_KEY
        }
    )

    if res.status_code == 200:
        print('Uploaded file to Edge Impulse', res.status_code, res.content)
    else:
        print('Failed to upload file to Edge Impulse', res.status_code, res.content)


HMAC_KEY = "80f1fc9e4ae9f0baa08a6b79ad42ce5e"
API_KEY = "ei_3f30652431732b51bd34c9ef7fe05495b96bb31370c6bbf3"
NAME_LABEL = "EMG_4"
FILE_PATH = "ejemplo_emg.txt"



def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


with open(FILE_PATH, 'r') as file:
    values = [list(map(float, line.strip().split())) for line in file if is_float(line.strip().split()[0])]


chunk_size = 1000
chunks = [values[i:i + chunk_size] for i in range(0, len(values), chunk_size)]


for i, chunk in enumerate(chunks):
    if len(chunk) == chunk_size:  # Asegurarse de que solo suba fragmentos completos de 1000 muestras
        file_name = f"EMG_3{i+1}.json"
        upload_ei(file_name, chunk, HMAC_KEY, API_KEY)
