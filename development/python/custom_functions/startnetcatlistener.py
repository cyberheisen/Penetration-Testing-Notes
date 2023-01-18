import subprocess

def startNetcatListener(port,path='.'):
    print("[+] Starting netcat listener")
    try:
        proc = subprocess.Popen('%s/nc -lvp %s' % (path,port), shell=True)
        return proc
    except Exception as error:
        print('something went wrong: %s' % error)

port = '4444'

proc = startNetcatListener(port,'/bin')
