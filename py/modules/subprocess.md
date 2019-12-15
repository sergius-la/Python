# Subprocess

**Get console output**
```python
cmd = "aapt dump badging {}".format(path)
print(subprocess.getoutput(cmd))

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
out = p.stdout.read()
print(out)
```
<img src="https://github.com/sergius-la/icon_links/blob/master/img/stackoverflow.png" width="14" height="14"> [__Stack OverFlow: Edit enviroment PATH for ubprocess__](https://stackoverflow.com/questions/2231227/python-subprocess-popen-with-a-modified-environment)
```python
import subprocess, os
my_env = os.environ.copy()
my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
subprocess.Popen(my_command, env=my_env)
```