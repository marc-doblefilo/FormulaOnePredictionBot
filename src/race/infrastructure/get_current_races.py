import xmltodict
import requests
from datetime import datetime

def get_current_races():
    response = requests.get("https://ergast.com/api/f1/current/races")

    doc = xmltodict.parse(response.text)

    races = []
    for race in doc['MRData']['RaceTable']['Race']:
        isClosed: bool = False
        isFinished: bool = False
        date = datetime.strptime(race['Date'] + " " + race['Time'], '%Y-%m-%d %H:%M:%SZ')

        if(date < datetime.utcnow()):
            isClosed = True

        response_results = requests.get(f"https://ergast.com/api/f1/current/{race['@round']}/results")
        doc_results = xmltodict.parse(response_results.text)

        if(len(doc_results['MRData']['RaceTable']) > 2):
            isFinished = True

        races.append([race['@season'], race['@round'], race['RaceName'], isClosed, isFinished])

    return races
