# from ed discussion #164

import altair as alt
import pandas as pd
import os
from toolz.curried import pipe

def create_json_dir_transformer(data_dir):
    """
    Creates a custom Altair data transformer that saves datasets as JSON files in a specified directory.

    Args:
        data_dir (str): Directory to store JSON files. Default is 'altairdata'.

    Returns:
        function: A data transformer function.
    """
    def json_dir(data):
        os.makedirs(data_dir, exist_ok=True)
        return pipe(data, alt.to_json(filename=data_dir + '/{prefix}-{hash}.{extension}'))
    return json_dir


def setup_altair_for_large_data(data_dir, renderer='jupyterlab'):
    """
    Configures Altair to handle large datasets by:
    1. Registering and enabling a custom JSON data transformer.
    2. Disabling the default row limit.
    3. Enabling the specified renderer.

    Args:
        data_dir (str): Directory to store JSON files. Default is 'altairdata'.
        renderer (str): Renderer to enable. Default is 'jupyterlab'.
    """
    json_dir_transformer = create_json_dir_transformer(data_dir)
    alt.data_transformers.register('json_dir', json_dir_transformer)
    alt.data_transformers.enable('json_dir')

    alt.data_transformers.disable_max_rows()

    if renderer:
        alt.renderers.enable(renderer)