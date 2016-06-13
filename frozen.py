#!/usr/bin/env python
import sys
import os

frozen = """import zipfile
import os
import shutil
zipdata = '''%s'''

if __name__ == "__main__":
    os.mkdir('.extract')
    os.chdir('.extract')
    with open('.test.zip', 'w') as zipf:
        zipf.write(zipdata.decode('base64'))
    zipfile.ZipFile('.test.zip').extractall()
    out = os.system('%s')
    os.remove('.test.zip')
    os.chdir('..')
    shutil.rmtree('.extract')
"""

def main():
    with open(sys.argv[1] + '.py', 'w') as exe:
        with open(sys.argv[2]) as zipf:
            zipdata = zipf.read()
        exe.write(frozen % (zipdata.encode('base64'), sys.argv[3]))
    out = os.system('cython --embed -o .out.c %s.py' % sys.argv[1])
    out = os.system('gcc -Os -I $HOME/.local/include/python2.7 -o %s .out.c -lpython2.7 -lpthread -lm -lutil -ldl' % sys.argv[1])
    os.remove('.out.c')
    os.remove(sys.argv[1] + '.py')

if __name__ == "__main__":
    main()
