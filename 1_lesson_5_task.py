import chardet
import subprocess
import platform

portals = ['yandex.ru', 'youtube.com']

param = '-n' if platform.system().lower() == 'windows' else '-c'
for portal in portals:
    args = ['ping', param, '2', portal]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
