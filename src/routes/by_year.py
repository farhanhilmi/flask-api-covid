from flask import Blueprint
import urllib.request
import json

blueprint_by_year = Blueprint(name="blueprint_by_year", import_name=__name__)


@blueprint_by_year.route('/yearly/<year>', methods=['GET'])
def by_year(year):
    url = "https://data.covid19.go.id/public/api/update.json"

    response = urllib.request.urlopen(url)
    data = response.read()
    covid_data = json.loads(data)

    daily = covid_data['update']['harian']

    positive = 0
    recovered = 0
    deaths = 0
    active = 0

    for key in daily:
        if (key['key_as_string'].split('-')[0] == year):
            positive += int(key['jumlah_positif']['value'])
            recovered += int(key['jumlah_sembuh']['value'])
            deaths += int(key['jumlah_meninggal']['value'])
            active += int(key['jumlah_dirawat']['value'])

    covid = {"year": year, "positive": positive,
             "deaths": deaths, "active": active, "recovered": recovered}

    return {"ok": True, "message": "success",
            "data": covid}
