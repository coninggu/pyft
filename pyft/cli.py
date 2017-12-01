# -*- coding: utf-8 -*-
import click
import os
import signal

from gunicorn import util
from pyft import __version__, settings


@click.group()
def cli():
    pass


@cli.command('run', help='Run worker server.')
@click.option('--env', '-e', default='dev', help='Run as a daemon.')
def run(env):
    """ 웹서버를 실행한다.
    
    웹서버 환경은 dev, prod 로 구분되고 프로세스 개수는 환경에 따라 다르다.
    
    dev 모드는 무조건 1개로 고정하고 prod 모드는 settings.SERVER_PROCESS 값만큼 결정된다.
    
    """
    from pyft.app import App

    options = {
        'bind': '%s:%s' % (settings.SERVER_HOST, settings.SERVER_PORT),
        'timeout': settings.SERVER_TIMEOUT,
        'pidfile': settings.SERVER_PID_FILE,
        'loglevel': 'debug' if settings.DEBUG else 'error',
        'proc_name': settings.SERVER_PROCESS_NAME,
        'limit_request_lint': settings.LIMIT_REQUEST_LINE,
        'limit_request_fields': settings.LIMIT_REQUEST_FIELDS,
        'limit_request_field_size': settings.LIMIT_REQUEST_FIELD_SIZE,
    }

    if env == 'prod':
        util.daemonize(False)
        options['workers'] = int(settings.SERVER_PROCESS)

    App(options).run()


@cli.command('shutdown', help='Shutdown running servers.')
@click.option('--now', '-n', is_flag=True, help='Shutdown now.')
def shutdown(now):
    """ 웹서버를 종료한다."""
    try:
        if settings.SERVER_PID_FILE:
            pidfile = settings.SERVER_PID_FILE
            if os.path.exists(pidfile):
                with open(pidfile) as f:
                    pid = int(f.read().strip())
                os.kill(pid, signal.SIGKILL if now else signal.SIGTERM)
                click.echo(pid)
    except ProcessLookupError as e:
        click.echo(e)


@cli.command(help='Print version string.')
def version():
    click.echo(__version__)


def main():
    cli()
