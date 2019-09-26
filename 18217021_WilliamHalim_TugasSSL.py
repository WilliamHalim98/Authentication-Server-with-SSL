#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Nama : William Halim
#NIM  : 18217021

from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class CustomHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self) : 
        if self.headers['Authorization'] == None:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('no auth header received', 'UTF-8'))
            pass
        elif self.headers['Authorization'] == 'Basic YW5vdGhlcjptZQ==':
            self.do_HEAD()
            self.wfile.write(bytes(self.headers['Authorization'], 'UTF-8'))
            self.wfile.write(bytes(' authenticated!', 'UTF-8'))
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write(bytes(self.headers['Authorization'], 'UTF-8'))
            self.wfile.write(bytes(' not authenticated', 'UTF-8'))
            pass

def main():
    listen_target = ('192.168.5.105', 10001) #192.168.5.105 adalah private ip address dari laptop saya
    certificate_file = '/certificate.pem'
    private_key_file = '/privkey.pem'
    try:
        httpd = HTTPServer(listen_target, CustomHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket,certfile=certificate_file, keyfile=private_key_file, server_side=True)
        print ('started httpd...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ('^C received, shutting down server')

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




