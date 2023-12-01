# clisender
Designed to send commands into OS terminal

## Features
1. send commands into OS terminal
2. check if cli commands are accessible (special utilities is installed)
3. access to standard parts of result in a simple ready-to-use form (stdout/stderr/retcode/full state)

## License
See the [LICENSE](LICENSE) file for license rights and limitations (MIT).


## Release history
See the [HISTORY.md](HISTORY.md) file for release history.


## Installation
```commandline
pip install clisender
```

## Import

```python
from clisender import *
```


## GUIDE

### USAGE

```python
from clisender import *

victim = CliSender()

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
	
	ЋЎ¬Ґ­ Ї ЄҐв ¬Ё б starichenko.corp.element-t.ru [::1] б 32 Ў ©в ¬Ё ¤ ­­ле:
	ЋвўҐв ®в ::1: ўаҐ¬п<1¬б 
	
	‘в вЁбвЁЄ  Ping ¤«п ::1:
	    Џ ЄҐв®ў: ®вЇа ў«Ґ­® = 1, Ї®«гзҐ­® = 1, Ї®вҐап­® = 0
	    (0% Ї®вҐам)
	ЏаЁЎ«Ё§ЁвҐ«м­®Ґ ўаҐ¬п ЇаЁҐ¬ -ЇҐаҐ¤ зЁ ў ¬б:
	    ЊЁ­Ё¬ «м­®Ґ = 0¬бҐЄ, Њ ЄбЁ¬ «м­®Ґ = 0 ¬бҐЄ, ‘аҐ¤­ҐҐ = 0 ¬бҐЄ
	
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self._last_exx_timeout=None
==================================================
"""
```
