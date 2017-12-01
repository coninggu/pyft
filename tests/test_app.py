# -*- coding: utf-8 -*-
import pytest
import json

from pyft.app import app, App


@pytest.fixture(scope='module')
def client():
    return app.test_client()


def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_convert(client):
    codes = ['', 'import pyft']
    for code in codes:
        resp = client.post('/convert',
                           data=json.dumps({'code': code}),
                           content_type='application/json')
        assert resp.status_code == 200


def test_app():
    tapp = App({'loglevel': 'Debug'})
    tapp.load()
