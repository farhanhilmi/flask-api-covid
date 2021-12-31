from flask import Flask

# load modules
from src.routes.main import blueprint_main
from src.routes.by_year import blueprint_by_year
from src.routes.yearly import blueprint_yearly
from src.routes.monthly import blueprint_monthly
from src.routes.by_date import blueprint_by_date

# init Flask app
app = Flask(__name__)

app.register_blueprint(blueprint_main)
app.register_blueprint(blueprint_by_year)
app.register_blueprint(blueprint_yearly)
app.register_blueprint(blueprint_monthly)
app.register_blueprint(blueprint_by_date)
