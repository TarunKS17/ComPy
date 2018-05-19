#utf-8
import subprocess, shlex

filename='testrun'
a=subprocess.Popen(['g++', filename+'.cpp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stats=a.communicate()

if stats[0].decode() != '':
    print('Output:\n')
    print(stats[0].decode())
if stats[1].decode() != '':
    print("Compile time error:\n")
    print(stats[1].decode())

tcf=open('testcases.txt', 'r')
tc=tcf.readlines()
tcf.close()


print("Testing:\n")
run=[]
i = 0
while i<len(tc):
    args=shlex.split('./a.out > '+filename+'.txt')
    b=subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    b.stdin.write(tc[i].encode('utf-8'))
    b.stdin.close()
    output = b.stdout.read().decode()
    error = b.stderr.read().decode()
    print(output)
    print(tc[i+1])
    if output==tc[i+1].rstrip('\n'):
        run.append('Success')
    else:
        run.append('Failed')
    i+=2