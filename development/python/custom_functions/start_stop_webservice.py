import subprocess
import psutil

def startWebServer(port):
    print("[+] starting webserver")
    webserver = subprocess.Popen('/usr/bin/python3 -m http.server %s' % port, shell=True)
    return webserver

def stopWebServer(webserver):
    print("[-] stopping webserver")
    parent = psutil.Process(webserver.pid)
    for proc in parent.children(recursive=True):
        proc.kill()
    parent.kill()
    return
  
 port = '8080'

webserver = startWebServer(port)
stopWebServer(webserver)
