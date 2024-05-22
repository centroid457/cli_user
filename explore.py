# DON'T DELETE!
# useful to start smth without pytest and not to run in main script!

from cli_user import *

victim = CliUser()
victim.send("ping localhost", timeout=0.1)
victim.print_state()
