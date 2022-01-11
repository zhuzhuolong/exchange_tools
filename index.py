import textwrap

import tornado.httpserver

import tornado.ioloop

import tornado.options

import tornado.web
import datetime

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

if __name__ == "__main__":
    print(datetime.datetime.utcnow().replace(microsecond=0).isoformat() + '.000Z')
