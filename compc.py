#utf-8
import subprocess, shlex, time
 
class compy:
    def __init__(self):
        self.run=[]
        self.filename=''
        self.outputfile=str(time.time())+'.out'
    
    def compile(self, filename):
        self.filename=filename
        args=shlex.split('g++ '+ filename + '.cpp -o ' + self.outputfile)
        a=subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stats=a.communicate()

        if stats[0].decode() != '':
            print('Output:\n')
            print(stats[0].decode())
        if stats[1].decode() != '':
            print("Compile time error:\n")
            print(stats[1].decode())

    def testcases(self):
        tcf=open('testcases.txt', 'r')
        tc=tcf.readlines()
        tcf.close()

        i=0
        print("Testing:\n")

        while i<len(tc):
            #args=shlex.split(self.outputfile + ' > ' + self.filename+'.txt') #not working as it should
            args=shlex.split('./'+self.outputfile)
            b=subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            b.stdin.write(tc[i].encode('utf-8'))
            b.stdin.close()
            output = b.stdout.read().decode()
            error = b.stderr.read().decode()
            if output==tc[i+1].rstrip('\n'):
                self.run.append(' Success')
            else:
                self.run.append(' Failed')
            i+=2
    
    def result(self):
        for i in range(len(self.run)):
            print('Test case '+str(i)+self.run[i])

c1=compy()
c1.compile('testrun')
c1.testcases()
c1.result()



