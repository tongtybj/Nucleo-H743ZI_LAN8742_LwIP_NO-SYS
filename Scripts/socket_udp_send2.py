import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.settimeout(1)

    start_t = time.time()
    max_du = 0;
    min_du = 1e6;
    every_t = 0
    
    try:
        while True:

            s.sendto(b'hellohello',("192.168.25.238", 5005))
            try:
                data, addr = s.recvfrom(4096)
            except socket.timeout:
                print("caught a timeout at first echo")

            #print(repr(data))

            try:
                data, addr = s.recvfrom(4096)
            except socket.timeout:
                print("caught a timeout at second echo")

            #print(int.from_bytes(data, 'little'))

            if every_t > 0:
                if time.time() - every_t > max_du:
                    max_du = time.time() - every_t

                if time.time() - every_t < min_du:
                    min_du = time.time() - every_t

            if time.time() - start_t > 1:
                print("du: ", time.time() - every_t, ", max_du: ", max_du,  ", min_du: ", min_du)
                start_t = time.time()


            every_t = time.time()

            time.sleep(0.001)

    except KeyboardInterrupt:
        exit()
