# -*- coding: utf-8 -*-

from datetime import datetime
from flask import make_response
from functools import wraps, update_wrapper


def never_cache(view):

    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = ', '.join([
            'no-store', 'no-cache', 'must-revalidate',
            'post-check=0', 'pre-check=0', 'max-age=0',
        ])
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)