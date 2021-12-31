from flask import Blueprint
import urllib.request
import json

blueprint_main = Blueprint(name="blueprint_main", import_name=__name__)


@blueprint_main.route('/', methods=['GET'])
def main():
    url = "https://data.covid19.go.id/public/api/update.json"

    response = urllib.request.urlopen(url)
    data = response.read()
    covid_data = json.loads(data)

    total_case = covid_data['update']['total']
    update_case = covid_data['update']['penambahan']

    total_active = total_case['jumlah_dirawat']
    total_recovered = total_case['jumlah_sembuh']
    total_positive = total_case['jumlah_positif']
    total_deaths = total_case['jumlah_meninggal']

    new_active = update_case['jumlah_dirawat']
    new_recovered = update_case['jumlah_sembuh']
    new_positive = update_case['jumlah_positif']
    new_deaths = update_case['jumlah_meninggal']

    covid = {"total_positive": total_positive, "new_positive": new_positive,
             "total_deaths": total_deaths, "new_deaths": new_deaths, "total_active": total_active, "new_active": new_active, "total_recovered": total_recovered, "new_recovered": new_recovered}

    return {"ok": True, "message": "success",
            "data": covid}
