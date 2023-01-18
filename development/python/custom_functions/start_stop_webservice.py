from subprocess import Popen, PIPE
import psutil
import time

def startWebServer(port,version='standard'):
    print("[+] starting %s webserver" % version)
    if version.lower() == 'upload':
        webserver = Popen('python3 -m uploadserver %s' % port, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    else:        
        webserver = Popen('python3 -m http.server %s' % port, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    time.sleep(2)
    return webserver

def stopWebServer(webserver):
    print("[-] stopping webserver")
    parent = psutil.Process(webserver.pid)
    for proc in parent.children(recursive=True):
        proc.kill()
    parent.kill()
    return
  
port = '8080'
version = 'upload'
webserver = startWebServer(port,version)
# if using the upload server, files can be uploaded using curl
# curl -X POST url/upload -F files=@'file1.txt'

stopWebServer(webserver)
