from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # Получаем информацию о клиенте
        client_ip = self.client_address[0]
        
        # Получаем имя автора из переменной окружения
        author_name = os.getenv('AUTHOR_NAME', 'Неизвестный автор')
        
        # Получаем информацию о сервере
        hostname = socket.gethostname()
        server_ip = socket.gethostbyname(hostname)

        # Формируем HTML-ответ
        response_body = f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="utf-8">
            <title>Информация о клиенте</title>
        </head>
        <body>
            <h1>  Информация о подключении  </h1>
            <p><strong>IP адрес клиента:</strong> {client_ip}</p>
            <p><strong>Имя автора:</strong> {author_name}</p>
            <p><strong>server hostname:</strong> {hostname}</p>
            <p><strong>server ip :</strong> {server_ip}</p>
        </body>
        </html>
        """
        
        # Отправляем ответ
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(response_body.encode('utf-8'))


server_address = ('', 8000)
httpd = HTTPServer(server_address, RequestHandler)
print('Сервер запущен на порту 8000...')
httpd.serve_forever()