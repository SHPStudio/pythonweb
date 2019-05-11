from interface import interface

class ImageConroller(interface):
    def do_GET(self, handler, param=None):
        handler.send_response(200)
        handler.end_headers()
        handler.wfile.write("hello")
        return


    def do_POST(self, handler, data=None):
        pass