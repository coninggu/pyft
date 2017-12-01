# -*- coding=utf-8 -*-
import os
import multiprocessing

DEBUG = True

DEFAULT_STYLE = 'pep8'
""" reformat 기본 코드 스타일.

제공되는 스타일은 'pep8', 'chromium', 'google', 'facebook' 이다.

Since version 1.0.0
"""

SERVER_PROCESS = multiprocessing.cpu_count() / 2
""" 서버의 프로세스 개수.

개발(dev) 모드에서는 값을 무시하고 1개로 고정한다.

since version 1.0.0
"""

SERVER_PROCESS_NAME = 'pyft'
""" 프로세스 이름.

since version 1.0.0
"""

SERVER_HOST = '127.0.0.1'
""" 서버의 listening socket 이 bind 하는 인터페이스.

Since version 1.0.0
"""

SERVER_PORT = 8000
""" 서버가 listening 하는 socket 의 port.

Since version 1.0.0
"""

SERVER_TIMEOUT = 30
""" POST 요청을 처리하는데 소요되는 최대 시간(초).

Since version 1.0.0
"""

SERVER_PID_FILE = os.path.join(os.path.dirname(__file__), 'pyft.pid')

""" 서버의 ``pid`` 가 기록되는 경로.

Since version 1.0.0
"""

# Security
LIMIT_REQUEST_LINE = 4094
""" request line 최대 크기.(Bytes)

0 무제한. 0 ~ 8190의 값을 가진다.

Since version 1.0.0
"""

LIMIT_REQUEST_FIELDS = 100
""" request 최대 헤더 필드 수.

0 ~ 32768의 값을 가진다.

Since version 1.0.0
"""

LIMIT_REQUEST_FIELD_SIZE = 8190
""" request 헤더 필드의 최대 크기.
 
0 무제한.

Since version 1.0.0
"""
