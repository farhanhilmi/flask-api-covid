from flask import Blueprint
import urllib.request
import json

blueprint_yearly = Blueprint(name="blueprint_yearly", import_name=__name__)


@blueprint_yearly.route('/yearly', methods=['GET'])
def yearly():
    url = "https://data.covid19.go.id/public/api/update.json"

    response = urllib.request.urlopen(url)
    data = response.read()
    covid_data = json.loads(data)
    daily = covid_data['update']['harian']

    list_of_covid = []
    previous_year = 0

    for key in daily:
        if len(list_of_covid) < 1:
            previous_year = key['key_as_string'].split('-')[0]
            list_of_covid.append({"year": key['key_as_string'].split('-')[0], "recovered": int(key['jumlah_sembuh']['value']), "positive": int(key['jumlah_positif']['value']),
                                  "deaths": int(key['jumlah_meninggal']['value']), "active": int(key['jumlah_dirawat']['value'])})
            continue

        if previous_year == key['key_as_string'].split('-')[0]:
            for item in list_of_covid:
                if (item['year'] == key['key_as_string'].split('-')[0]):
                    item['positive'] += int(key['jumlah_positif']['value'])
                    item['recovered'] += int(key['jumlah_sembuh']['value'])
                    item['deaths'] += int(key['jumlah_meninggal']['value'])
                    item['active'] += int(key['jumlah_dirawat']['value'])
        else:
            previous_year = key['key_as_string'].split('-')[0]
            list_of_covid.append({"year": key['key_as_string'].split('-')[0], "recovered": int(key['jumlah_sembuh']['value']), "positive": int(key['jumlah_positif']['value']),
                                  "deaths": int(key['jumlah_meninggal']['value']), "active": int(key['jumlah_dirawat']['value'])})

    return {"ok": True, "message": "success",
            "data": list_of_covid}
