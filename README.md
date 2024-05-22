# cli_user (v0.0.8)

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
See tests and sourcecode for other examples.

------------------------------
### 1. example1.py
```python
from cli_user import *

victim = CliUser()
victim.send("ping localhost", timeout=0.1)
victim.print_state()
"""
==================================================
[#####################ERROR#####################]
self.counter=1
self.counter_in_list=0
self.last_cmd='ping localhost'
self.last_duration=0.109938
self.last_finished=True
self.last_finished_success=False
self.last_retcode=None
--------------------------------------------------
self.last_stdout=
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self.last_exx_timeout=Exx_CliTimeout("TimeoutExpired('ping localhost', 0.1)")
==================================================
"""

victim.send("python --version", timeout=1)
victim.print_state()
"""
==================================================
self.counter=2
self.counter_in_list=0
self.last_cmd='python --version'
self.last_duration=0.087947
self.last_finished=True
self.last_finished_success=True
self.last_retcode=0
--------------------------------------------------
self.last_stdout=
	|'Python 3.12.1'
	|''
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self.last_exx_timeout=None
==================================================
"""
```

********************************************************************************
