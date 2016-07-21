# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

def _jupyter_server_extension_paths():
    return [{
        "module": "nbexamples"
    }]

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'nbexamples',
        'require': 'nbexamples/main'
    }]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("nbexample enabled!")