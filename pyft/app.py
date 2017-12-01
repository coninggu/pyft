# -*- coding: utf-8 -*-
import gunicorn.app.base

from flask import Flask, render_template, request, jsonify
from gunicorn.six import iteritems
from yapf.yapflib import style
from pyft.reformatter import ReFormat
from pyft import __version__, __author_email__, __url__

app = Flask(__name__)

DEFAULT_RESP = {
    'status': 'ok',
    'message': 'success',
    'result': {
        'reformatted_code': ''
    }
}


@app.route('/', methods=['GET'])
def index():
    context = {
        'version': __version__,
        'author_email': __author_email__,
        'url': __url__,
        'code_styles': [i for i in sorted(style._STYLE_NAME_TO_FACTORY, reverse=True)]
    }
    return render_template('index.html', **context)


@app.route('/convert', methods=['POST'])
def convert():
    req = request.get_json()
    code = req.get('code')
    style_name = req.get('style')
    if not code:
        return '', 200

    resp_data = ReFormat(code, style_name=style_name).get_reformatted_code(DEFAULT_RESP)

    return jsonify(resp_data)


class App(gunicorn.app.base.BaseApplication):
    def __init__(self, options=None):
        self.options = options or {}
        self.application = app
        super(App, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
