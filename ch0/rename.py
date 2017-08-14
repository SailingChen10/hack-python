import os
import sys
path = '/Users/zhucunli/Desktop/python/任务1'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file)) == True:
        if file.find('py3')<0:
            newname = file.replace("ex","py3-ex")
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print (file,'ok')
