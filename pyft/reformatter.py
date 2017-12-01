# -*- coding: utf-8 -*-
import json

from yapf.yapflib.yapf_api import FormatCode
from yapf.yapflib import style

from pyft import settings


class ReFormat():
    def __init__(self, original_code, style_name=None, style_opts=None):
        self.error_msg = ''
        self.original_code = original_code
        self.style_name = style_name if style_name in style._STYLE_NAME_TO_FACTORY else settings.DEFAULT_STYLE
        self.style_opts = style_opts
        self.style_config()
        self.reformating_code()

    def style_config(self):
        style_factory = style._STYLE_NAME_TO_FACTORY.get(self.style_name)
        if style_factory is not None:
            self.style_config = style_factory()

        if self.style_opts is not None:
            for key, value in self.style_opts.items():
                if key in self.style_config:
                    self.style_config[key] = value

    def reformating_code(self):
        try:
            self.reformatted_code, self.result = FormatCode(self.original_code, style_config=self.style_config)
        except Exception as e:
            self.result = 'error'
            self.error_msg = str(e)

    def get_reformatted_code(self, default_resp, format='json'):
        resp = default_resp.copy()
        if self.result == 'error':
            resp['status'] = 'error'
            resp['message'] = self.error_msg
        else:
            resp['result']['reformatted_code'] = self.reformatted_code

        if format == 'json':
            resp = json.dumps(resp)

        return resp
