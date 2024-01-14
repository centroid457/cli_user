from cli_user import *

victim = CliUser()
victim.send("ping localhost", timeout=0.1)
victim.print_state()
