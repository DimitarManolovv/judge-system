import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

"""
read more for python web servers
"""

def check_submission():
  # call offline judge system

class WebServer(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/submission':
      check_submission()

    self.send_response(200)

httpd = SocketServer.TCPServer(("", 80), WebServer)
httpd.serve_forever()