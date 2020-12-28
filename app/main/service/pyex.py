import pyEX

iex_cloud_client = pyEX.Client(
        api_token='Tpk_1e8fef17ee254009a45873d2c1b76828',
        version='sandbox'
    )

def receive_pyex_symbols(symbols_pattern):
    all_symbols = [symbol_dict['symbol'] for symbol_dict in iex_cloud_client.symbols()]
    selected_symbols = [symbol for symbol in all_symbols if symbol.startswith(symbols_pattern)]
    return selected_symbols
