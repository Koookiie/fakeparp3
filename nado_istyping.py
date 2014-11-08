import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from tornado.gen import engine, Task
import ujson as json
from tornadoredis import Client
import redis

print "WS Server started!"

r = redis.Redis()
wsclients = set()

class WSHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self, chat):
        self.chat = chat
        self.redis_listen("chat:"+str(self.chat))
        self.remote_ip = self.request.headers.get('X-Forwarded-For', self.request.headers.get('X-Real-Ip', self.request.remote_ip))
        wsclients.add(self)
        print '[{ip}|{chat}] connected to server ({connected} connected to server)'.format(
            ip=self.remote_ip,
            chat=self.chat,
            connected=len(wsclients)
        )

    def on_message(self, msg):
        print "[{ip}|{chat}] WS message: {msg}".format(
            ip=self.remote_ip,
            chat=self.chat,
            msg=msg
        )
        message = json.loads(msg)
        if message["a"] in ("typing", "stopped_typing") and 'c' in message:
            try:
                counter = int(message['c'])
                session = r.hget("chat.%s.counters" % (self.chat), counter)
                if self.remote_ip != r.hget("session.%s.meta" % (session), "last_ip"):
                    return
            except TypeError:
                return
            r.publish("chat:"+str(self.chat), json.dumps({
                "a": message["a"],  # action
                "c": counter  # counter
            }))

    def on_close(self):
        self.redis_client.unsubscribe("chat:"+str(self.chat))
        wsclients.discard(self)
        print '[{ip}|{chat}] connection closed. ({connected} connected to server)'.format(
            ip=self.remote_ip,
            chat=self.chat,
            connected=len(wsclients)
        )

    @engine
    def redis_listen(self, channel):
        self.redis_client = Client()
        yield Task(self.redis_client.subscribe, channel)
        self.redis_client.listen(self.on_redis_message, self.on_redis_unsubscribe)

    def on_redis_message(self, message):
        if message.kind == "message":
            self.write_message(message.body)

    def on_redis_unsubscribe(self, callback):
        self.redis_client.disconnect()

settings = dict(
    debug=True,
    gzip=True,
)

application = tornado.web.Application([
    (r'/([^/]+)', WSHandler),
], **settings)


if __name__ == "__main__":
    application.autoreload = True
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8081)
    tornado.ioloop.IOLoop.instance().start()
