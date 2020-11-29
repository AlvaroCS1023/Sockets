import socket

mi_socket = socket.socket()
mi_socket.bind( ('localhost', 9000) )
mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    print "CLIENTE CONECTADO!"
    print addr

    peticion = conexion.recv(1024)
    print peticion

    conexion.send("HOLA SOY EL SERVIDOR!")
    conexion.close()

