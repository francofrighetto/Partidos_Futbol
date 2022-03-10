import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
try:
    s.connect(("www.google.com", 80))
except (socket.gaierror, socket.timeout):
    print("Sin conexión a internet")
else:
    print("Con conexión a internet")
    s.close()