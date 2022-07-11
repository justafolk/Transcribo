import subprocess
result = subprocess.run(['curl','-d','"text=hello%20world"' ,'http://bark.phon.ioc.ee/punctuator' ], stdout=subprocess.PIPE)
import time 
time.sleep(3)
print(result.stdout.decode())
print()

