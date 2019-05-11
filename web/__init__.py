from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
from BaseHTTPServer import HTTPServer

class Shape(object):
    def __init__(self,host='0.0.0.0', port=8080):
        self.urlMap = {}
        self.host = host
        self.port = port
        self.handler = GetHandler
        self.httpServer = HTTPServer((self.host, self.port), self.handler)
    def run(self):
        print 'Starting server, use <Ctrl-C> to stop'
        self.httpServer.serve_forever()

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        print parsed_path
        message_parts = [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

