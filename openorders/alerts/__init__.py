from flask import Blueprint
from openorders.db import get_db

alerts_blueprint = Blueprint('alerts', __name__)

from . import views
