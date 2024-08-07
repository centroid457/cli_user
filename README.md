![Ver/TestedPython](https://img.shields.io/pypi/pyversions/cli_user)
![Ver/Os](https://img.shields.io/badge/os_development-Windows-blue)  
![repo/Created](https://img.shields.io/github/created-at/centroid457/cli_user)
![Commit/Last](https://img.shields.io/github/last-commit/centroid457/cli_user)
![Tests/GitHubWorkflowStatus](https://github.com/centroid457/cli_user/actions/workflows/test_linux.yml/badge.svg)
![Tests/GitHubWorkflowStatus](https://github.com/centroid457/cli_user/actions/workflows/test_windows.yml/badge.svg)  
![repo/Size](https://img.shields.io/github/repo-size/centroid457/cli_user)
![Commit/Count/t](https://img.shields.io/github/commit-activity/t/centroid457/cli_user)
![Commit/Count/y](https://img.shields.io/github/commit-activity/y/centroid457/cli_user)
![Commit/Count/m](https://img.shields.io/github/commit-activity/m/centroid457/cli_user)

# cli_user (current v0.1.3/![Ver/Pypi Latest](https://img.shields.io/pypi/v/cli_user?label=pypi%20latest))

## DESCRIPTION_SHORT
send commands into system terminal

## DESCRIPTION_LONG
Designed to send commands into OS terminal


## Features
1. send commands into OS terminal  
2. check if cli commands are accessible (special utilities is installed)  
3. access to standard parts of result in a simple ready-to-use form (stdout/stderr/retcode/full state)  
4. use batch timeout for list  
5. till_first_true  
6. counter/counter_in_list  


********************************************************************************
## License
See the [LICENSE](LICENSE) file for license rights and limitations (MIT).


## Release history
See the [HISTORY.md](HISTORY.md) file for release history.


## Installation
```commandline
pip install cli-user
```


## Import
```python
from cli_user import *
```


********************************************************************************
## USAGE EXAMPLES
See tests, sourcecode and docstrings for other examples.  

------------------------------
### 1. example1.py
```python
from cli_user import *

print()
print()
print()
print()
victim = CliUser()
victim.send("ping localhost", timeout=0.1)
print()
# victim.print_state()
"""
[CLI_SEND] [ping localhost]
....
==================================================
[#####################ERROR#####################]
self.counter=1
self.counter_in_list=0
self.last_cmd='ping localhost'
self.last_duration=1.041
self.last_finished=True
self.last_finished_success=False
self.last_retcode=None
--------------------------------------------------
self.last_stdout=
	|''
	|'РћР±РјРµРЅ РїР°РєРµС‚Р°РјРё СЃ starichenko.corp.element-t.ru [::1] СЃ 32 Р±Р°Р№С‚Р°РјРё РґР°РЅРЅС‹С…:'
	|'РћС‚РІРµС‚ РѕС‚ ::1: РІСЂРµРјСЏ<1РјСЃ '
	|'РћС‚РІРµС‚ РѕС‚ ::1: РІСЂРµРјСЏ<1РјСЃ '
	|''
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self.last_exx_timeout=Exx_CliTimeout()
==================================================
"""

print()
print()
print()
print()
victim.send(["python --version", ("ping localhost", 0.1), ])
"""
[CLI_SEND] [python --version]
.
[CLI_SEND] [('ping localhost', 0.1)]
....
==================================================
[#####################ERROR#####################]
self.counter=3
self.counter_in_list=2
self.last_cmd='ping localhost'
self.last_duration=1.042
self.last_finished=True
self.last_finished_success=False
self.last_retcode=None
--------------------------------------------------
self.last_stdout=
	|''
	|'РћР±РјРµРЅ РїР°РєРµС‚Р°РјРё СЃ starichenko.corp.element-t.ru [::1] СЃ 32 Р±Р°Р№С‚Р°РјРё РґР°РЅРЅС‹С…:'
	|'РћС‚РІРµС‚ РѕС‚ ::1: РІСЂРµРјСЏ<1РјСЃ '
	|'РћС‚РІРµС‚ РѕС‚ ::1: РІСЂРµРјСЏ<1РјСЃ '
	|''
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self.last_exx_timeout=Exx_CliTimeout()
==================================================
[ERROR] cmd_item=('ping localhost', 0.1) in full sequence cmd=['python --version', ('ping localhost', 0.1)]
"""
```

********************************************************************************
