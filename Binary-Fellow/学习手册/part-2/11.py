from echo import echo
echo(__file__)

fp = open('myfile.txt','w+')
string = 'Hello file world!'
fp.write(string)
fp.close()

fp = open('myfile.txt')
for line in fp:
   print line
