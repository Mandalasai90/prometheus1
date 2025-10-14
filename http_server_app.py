import http.server
from prometheus_client import start_http_server

class HandleRequest(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # ✅ HTML must be inside a Python string
        html = """
        <html>
        <head>
            <title>First Python Application</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f8f8f8;
                    margin-top: 20%;
                    text-align: center; /* centers all inline text */
                }
                .welcome {
                    color: darkblue;
                    font-size: 22px;
                }
            </style>
        </head>
        <body>
            <span class="welcome">Welcome to our first Prometheus-Python application</span>
        </body>
        </html>
        """

        self.wfile.write(bytes(html, "utf-8"))

# ✅ This must be at root level (not inside class)
if __name__ == "__main__":
    start_http_server(5000)  # Prometheus metrics server
    server = http.server.HTTPServer(("localhost", 5000), HandleRequest)
    print("Server running at http://0.0.0.0:5000")
    server.serve_forever()
