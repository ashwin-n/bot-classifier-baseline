import sys
import csv
from utils import *
reload(sys)
sys.setdefaultencoding('utf8')
with open('tweets-bots.csv') as fin:
    with open('tweets-bots.train', 'w') as fout1:
        with open('tweets-bots.test', 'w') as fout2:
            i = 0
            for line in fin:
                line = unicode(line, errors='ignore')
                if i ==0:
                    i+=1
                    pass
                elif i <100000:
                    if  i<60000 and i%2==0:
                        fout1.write(line)
                    else:
                        fout2.write(line)
                    i+=1
                else:
                    break

with open('tweets-social-bots.csv') as fin:
    with open('tweets-social-bots.train', 'w') as fout1:
        with open('tweets-social-bots.test', 'w') as fout2:
            i = 0
            for line in fin:
                line = unicode(line, errors='ignore')
                if i <110000:
                    if i <30000:
                        fout1.write(line)
                    else:
                        fout2.write(line)
                    i+=1
                else:
                    break



with open('tweets-genuine.csv') as fin:
    with open('tweets-genuine.train', 'w') as fout1:
        with open('tweets-genuine.test', 'w') as fout2:
            i = 0
            for line in fin:
                # print line
                line = unicode(line, errors='ignore')
                words = list(csv_read(csv.reader([line])))
                if i ==0:
                    i+=1
                    pass
                elif i <220000:
                    try:
                        if int(words[0][3])%3==0 and i<80000:
                            fout1.write(line)
                        elif int(words[0][3])%3!=0 and i>120000:
                            fout2.write(line)
                    except IndexError:
                        pass
                    i+=1
                else:
                    break
