import pytest
import pathlib
import platform
from typing import *

from cli_sender import *


# =====================================================================================================================
class Test:
    def test__ok(self):
        victim = CliSender()

        if "Windows" in platform.system():
            cmd_line = "ping -n 1 localhost"
        else:
            cmd_line = "ping -c 1 localhost"

        assert victim.send(cmd_line, timeout=2)
        assert victim.last_cmd == cmd_line
        assert victim.last_finished is True

        assert victim._last_exx_timeout is None
        assert bool(victim.last_stdout) is True
        assert bool(victim.last_stderr) is False
        assert victim.last_retcode == 0
        assert victim.last_finished_success

    def test__exx_timeout(self):
        victim = CliSender()

        cmd_line = "ping localhost"
        assert not victim.send(cmd_line, timeout=0.1)
        assert victim.last_cmd == cmd_line
        assert victim.last_finished is True

        assert isinstance(victim._last_exx_timeout, Exx_CliTimeout)
        assert bool(victim.last_stdout) is False
        assert bool(victim.last_stderr) is False
        assert victim.last_retcode is None
        assert not victim.last_finished_success

    def test__exx_not_exists(self):
        victim = CliSender()

        cmd_line = "ping123"
        assert not victim.send(cmd_line, timeout=10)
        assert victim.last_cmd == cmd_line
        assert victim.last_finished is True

        assert victim._last_exx_timeout is None
        # assert bool(victim.last_stdout) is False
        assert bool(victim.last_stderr) is True
        assert victim.last_retcode not in [0, None]
        assert not victim.last_finished_success

    def test__exx_cli_available(self):
        # one cmd ------------------------------------------------
        class CliSenderForAvailable(CliSender):
            CMDS_REQUIRED = {"ping123": None, }

        try:
            victim = CliSenderForAvailable()
        except Exception as exx:
            assert isinstance(exx, Exx_CliNotAvailable)

        # two cmd ------------------------------------------------
        if "Windows" in platform.system():
            cmd_ping_1 = "ping -n 1 localhost"
        else:
            cmd_ping_1 = "ping -c 1 localhost"

        class CliSenderForAvailable(CliSender):
            CMDS_REQUIRED = {cmd_ping_1: None, }

        victim = CliSenderForAvailable()
        assert victim.cli_check_available()


# =====================================================================================================================
