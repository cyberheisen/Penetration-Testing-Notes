import subprocess

def startNetcatListener(port,path='.'):
    print("[+] Starting netcat listener")
    proc = subprocess.Popen('%s/nc -lvp %s' % (path,port), shell=True)
    return proc

port = '4444'

startNetcatListener(port,'/bin')
