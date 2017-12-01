# -*- coding: utf-8 -*-
import json

from pyft.reformatter import ReFormat
from pyft.app import DEFAULT_RESP


def test_success():
    style_opts = {
        'COLUMN_LIMIT': 120
    }
    cls = ReFormat('', style_opts=style_opts)
    jcode = cls.get_reformatted_code(DEFAULT_RESP)
    code = json.loads(jcode)
    assert code['message'] == DEFAULT_RESP['message']
    assert code['status'] == DEFAULT_RESP['status']


def test_error():
    cls = ReFormat(';')
    cls.get_reformatted_code(default_resp=DEFAULT_RESP)
