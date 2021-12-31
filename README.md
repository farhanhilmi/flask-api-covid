# flask-api-covid

flask-api-covid providing data on COVID-19 cases in Indonesia.

## Installation
1. Clone the repo
2. Install the required packages contained in requirements.txt
```
pip install -r requirements.txt
```

## Run the app
Execute flask run command to run the app
```
flask run
```

# Usage

By default the server starts on port `5000`. 

:warning: Important!

You have to login first before sending the request otherwise it will respond 403.

User already has dummy data with `username`: `userone` and `password`: `12345`.

## Get the overall Covid-19 case data

Method: `GET`

Endpoint: `/`

#### Response
```
{
    "data": {
        "new_active": <value>,
        "new_deaths": <value>,
        "new_positive": <value>,
        "new_recovered": <value>,
        "total_active": <value>,
        "total_deaths": <value>,
        "total_positive": <value>,
        "total_recovered": <value>
    },
    "message": "success",
    "ok": true
}
```

## Get data on COVID-19 cases in a given year

Method: `GET`

Endpoint: `/yearly/<year>`

Example:
```
http://localhost:5000/yearly/2020
```

#### Response
```
{
    "data": {
        "active": <value>,
        "deaths": <value>,
        "positive": <value>,
        "recovered": <value>,
        "year": "2020"
    },
    "message": "success",
    "ok": true
}
```

## Get data on COVID-19 cases per year

Method: `GET`

Endpoint: `/yearly`

Example:
```
http://localhost:5000/yearly
```

#### Response
```
{
    "data": [
        {
            "active": <value>,
            "deaths": <value>,
            "positive": <value>,
            "recovered": <value>,
            "year": <value>
        },
        ...
    ],
    "message": "success",
    "ok": true
}
```

## Get COVID-19 case data per month

Method: `GET`

Endpoint: `/monthly`

Example:
```
http://localhost:5000/monthly
```

#### Response
```
{
    "data": [
        {
            "active": <value>,
            "deaths": <value>,
            "month": "2020-03",
            "positive": <value>,
            "recovered": <value>
        },
        {
            "active": <value>,
            "deaths": <value>,
            "month": "2020-04",
            "positive": <value>,
            "recovered": <value>
        },
        ...
    ],
    "message": "success",
    "ok": true
}
```

## Get data on Covid-19 cases on a certain date

Method: `GET`

Endpoint: `/daily/<year>/<month>/<date>`

Example:
```
http://localhost:5000/daily/2020/11/10
```

#### Response
```
{
    "data": {
        "active": 232,
        "deaths": 72,
        "positive": 3779,
        "recovered": 3475,
        "year": "2020-11-10"
    },
    "message": "success",
    "ok": true
}
```
