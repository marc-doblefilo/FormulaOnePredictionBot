from typing import List
import xmltodict
import requests

def get_current_drivers_code() -> List:
    response = requests.get("https://ergast.com/api/f1/current/drivers")

    doc = xmltodict.parse(response.text)

    drivers = []
    for driver in doc['MRData']['DriverTable']['Driver']:
        drivers.append(driver['@code'])

    return drivers
