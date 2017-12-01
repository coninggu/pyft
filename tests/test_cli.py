# -*- coding: utf-8 -*-
import os
import pytest

from unittest.mock import patch

from click.testing import CliRunner
from pyft import settings, cli


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


@patch('pyft.app.App')
@patch('gunicorn.util.daemonize')
def test_run(mock_app, mock_daemoize, runner):
    result = runner.invoke(cli.run, ['--env', 'prod'])
    assert result.exit_code == 0
    assert mock_app.called
    assert mock_daemoize.called


@patch('os.kill')
def test_shutdown(mock_kill, runner):
    if not os.path.exists(settings.SERVER_PID_FILE):
        with open(settings.SERVER_PID_FILE, 'w') as f:
            f.write('999999')
            f.close()
    result = runner.invoke(cli.shutdown, ['--now'])
    assert result.exit_code == 0
    assert mock_kill.called
    os.remove(settings.SERVER_PID_FILE)


def test_version(runner):
    result = runner.invoke(cli.version)
    assert result.exit_code == 0


@patch('pyft.cli.cli')
def test_main(mock_cli):
    cli.main()
    assert mock_cli.called
