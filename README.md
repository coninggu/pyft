# PYFT: Online Python Formatter
파이썬 코드를 스타일에 맞추어 아름답게 변환해주는 온라인 포맷터 입니다. 
구글의 오픈소스인 YAPF(Github)를 활용하여 구현하였습니다.

![Image](static/v1.0.0.png)

homepage: [http://pyformatter.com](http://pyformatter.com)

## Requirements
- Python 3.5
- [YAPF](https://github.com/google/yapf)
- [Bootstrap3](https://getbootstrap.com)

## Install
    $ pyvenv-3.5 boot
    $ source boot/bin/activate
    $ pip install pip --upgrade
    $ pip install -e .

## Usage
PYFT는 개발 모드(dev mode), 운영 모드(prod mode) 두 가지의 웹 서버 환경을 제공합니다. 

개발 모드는 웹 서버 프로세스를 1개로 고정합니다. 아래 명령어로 개발 모드를 시작합니다. 
    
    $ pyft run 

운영 모드는 서버 CPU 개수의 50%를 사용합니다. 아래 명령어로 운영 모드를 시작합니다. 

    $ pyft run -env prod

프로세스가 가동하면 http://127.0.0.1:8080에 접근하여 코드를 변환 할 수 있습니다.

## Command Line Interface

<pre>
Usage: pyft [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  run       Run worker server.
  shutdown  Shutdown running servers.
  version   Print version string.
</pre>

## Author
Minwoo Cho / [@coninggu](http://coninggu.github.io)