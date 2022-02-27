import chardet
import subprocess
import platform

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
process = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in process.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
