# cli_sender
Designed to send commands into OS terminal

## Features
1. send commands into OS terminal
2. check if cli commands are accessible (special utilities is installed)
3. access to standard parts of result in a simple ready-to-use form (stdout/stderr/retcode/full state)
4. use batch timeout for list
5. till_first_true
6. counter/counter_in_list

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


## GUIDE

### USAGE

```python
from cli_user import *

victim = CliUser()

cmd_line = "ping localhost"
victim.send(cmd_line, timeout=0.1)
victim.print_state()
"""
==================================================
self.last_cmd='ping -n 1 localhost'
self.last_finished_success=True
self.last_finished=True
self.last_retcode=0
--------------------------------------------------
self.last_stdout=
	
    ###STDOUT PING!!!
	
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self._last_exx_timeout=None
==================================================
"""
```
