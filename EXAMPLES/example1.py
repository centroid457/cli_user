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
