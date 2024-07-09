from cli_user import *

print()
print()
print()
print()
victim = CliUser()
victim.send("ping localhost", timeout=0.1)
print()
victim.print_state()
"""
[CLI_SEND] [ping localhost]
==================================================
[#####################ERROR#####################]
self.counter=1
self.counter_in_list=0
self.last_cmd='ping localhost'
self.last_duration=0.122466
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

==================================================
[#####################ERROR#####################]
self.counter=1
self.counter_in_list=0
self.last_cmd='ping localhost'
self.last_duration=0.122466
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

print()
print()
print()
print()
victim.send("python --version", timeout=1)
print()
victim.print_state()
"""
[CLI_SEND] [python --version]

==================================================
self.counter=2
self.counter_in_list=0
self.last_cmd='python --version'
self.last_duration=0.044547
self.last_finished=True
self.last_finished_success=True
self.last_retcode=0
--------------------------------------------------
self.last_stdout=
	|'Python 3.11.7'
	|''
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self.last_exx_timeout=None
==================================================
"""
