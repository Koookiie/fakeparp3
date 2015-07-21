from flask import g, render_template
from functools import wraps
from erigam.lib import get_time, PING_PERIOD
from erigam.lib.api import join, get_online_state
from erigam.lib.request_methods import db_connect, get_log

def require_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.user.globalmod:
            return render_template('admin_denied.html')
        return f(*args, **kwargs)
    return decorated_function

def mark_alive(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if get_online_state(g.redis, g.user.chat, g.user.session_id) == "offline":
            db_connect()
            get_log()
            g.joining = join(g.sql, g.redis, g.log, g.user)
        else:
            g.redis.zadd('chats-alive', g.user.chat+'/'+g.user.session_id, get_time(PING_PERIOD*2))
            g.joining = False
        return f(*args, **kwargs)
    return decorated_function
