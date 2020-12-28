from flask import request

from flask_restx import Resource, Namespace, fields

from ..service.pyex import receive_pyex_symbols

#from ..util.pyex import PyEXDto

#api = PyEXDto.api
#_pyex_data = PyEXDto.pyex_data
api = Namespace('PyEXSymbols', description="iexCloud symbols operations")

@api.route('/symbols')
class PyEXSymbols(Resource):

    @api.response(200, "iexCloud symbols received")
    def post(self, *args, **kwargs):
        """Receive iexCloud symbols that math pattern """
        data = request.json
        symbols_pattern = data['symbols_pattern']
        return receive_pyex_symbols(symbols_pattern)

