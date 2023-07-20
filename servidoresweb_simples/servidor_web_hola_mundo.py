"""
SERVIDOR WEB SIMPLE QUE ESCUCHA EN UN PUERTO
Ejecutar en el servidor: 
python /home/ubuntu/myprojectsinpython/servidoresweb_simples/servidor_web_hola_mundo.py
"""
import http.server
import socketserver

PORT = 8000


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Hola Mundo!", "utf8"))
        return


Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
