import xmltodict
import requests

from src.driver.domain.driver import Driver


def get_current_drivers():
    response = requests.get("https://ergast.com/api/f1/current/drivers")

    doc = xmltodict.parse(response.text)

    drivers = []
    for driver in doc['MRData']['DriverTable']['Driver']:
        drivers.append(Driver(
            driver['@code'], driver['FamilyName'], int(driver['PermanentNumber'])))

    return drivers
