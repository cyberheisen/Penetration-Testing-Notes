import random
import socket

def checkPort(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    state = s.connect_ex(('127.0.0.1',port))
    s.close()
    if state == 0:  
        return False
    return True

def randomPort(port_start=1025, port_end=65535):
    state = False
    max_count = 10
    count = 0
    print('[+] Attempting to select a local random port')
    while not state:
        port = random.randint(port_start,port_end)
        # check if port is available
        state = checkPort(port)
        if state:
            return port
        else:
            count = count + 1
            if count > max_count:
                print('[!] No available ports found after %i attempts ' % max_count)
                break
    

def main():
    port = randomPort()
    print('my random port is: %s' % port)
    return

if __name__ == "__main__":
    main()
    exit()
