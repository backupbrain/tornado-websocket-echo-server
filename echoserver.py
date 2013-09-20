#!/usr/bin/python
 
import tornado.web
import tornado.websocket
import tornado.ioloop

 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		print "New client connected"
		self.write_message("You are connected")

	def on_message(self, message):
		self.write_message(message)

	def on_close(self):
		print "Client disconnected"


application = tornado.web.Application([
    (r"/", WebSocketHandler),
])
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



