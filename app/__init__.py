from flask_restx import Api
from flask import Blueprint

from .main.controller.pyex import api as iex_cloud_symbols_ns

from flask import Blueprint

blueprint = Blueprint('api', __name__)

api = Api(
	blueprint,
	title="iexCloud API",
	version='0.1',
	description='receive iexCloud symbols by pattern',
    )

api.add_namespace(iex_cloud_symbols_ns, path='/iex')
