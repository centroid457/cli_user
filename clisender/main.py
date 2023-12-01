import subprocess
from typing import *


# =====================================================================================================================
# TODO: add execution time


# =====================================================================================================================
class Exx_CliNotAvailable(Exception):
    """CLI exx because of cli can not be available due to have not some of required commands.
    """


class Exx_CliTimeout(Exception):    #use direct subprocess.TimeoutExpired??? NO!!!
    """CLI exx because of timeout expired
    """


class Exx_CliRetcode(Exception):
    """CLI exx because of returnCode is not zero.
    """


class Exx_CliStderr(Exception):
    """CLI exx because of stderr have any data
    """


# =====================================================================================================================
class CliSender:
    """Class which directly send (ONE!) command to OS terminal

    :ivar TIMEOUT: default timeout for execution process
        if timeout expired and process still not finished - raise exx
    :ivar _last_sp: Popen object
    :ivar _last_exx_timeout: saved Exx_CliTimeout if it was
    :ivar last_cmd: command for execution
    :ivar last_stdout: full stdout data
    :ivar last_stderr: full stderr data
    :ivar last_retcode: returned code if process was last_finished
    :ivar last_finished: flag shows if command process was finished
        useful if execute in threading.

    :ivar CMDS_REQUIRED: commands for cli_check_available
        dict with NAME - exact commands which will send into terminal in order to check some utility is installed,
        VALUE - message if command get any error

    :exception Exx_CliNotAvailable:
    :exception Exx_CliTimeout:
    :exception Exx_CliRetcode:
    :exception Exx_CliStderr:
    """
    TIMEOUT: Optional[float] = 2
    RAISE: Optional[bool] = None

    CMDS_REQUIRED: Optional[Dict[str, Optional[str]]] = None

    _last_sp: Optional[subprocess.Popen] = None
    _last_exx_timeout: Optional[Exx_CliTimeout] = None

    last_cmd: str = ""
    last_stdout: str = ""         # USE ONLY "" AS DEFAULT!!!
    last_stderr: str = ""         # USE ONLY "" AS DEFAULT!!!
    last_retcode: Optional[int] = None
    last_finished: Optional[bool] = None

    # init ------------------------------------------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._reinit_values()       # need to keep always one values!

        if not self.cli_check_available():
            raise Exx_CliNotAvailable

    def _reinit_values(self) -> None:
        self._last_sp = None
        self._last_exx_timeout = None

        self.last_cmd = ""
        self.last_stdout = ""
        self.last_stderr = ""
        self.last_retcode = None
        self.last_finished = None

    # SEND ------------------------------------------------------------------------------------------------------------
    def send(self, cmd: Union[str, List[str]], timeout: Optional[float] = None, _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        """execute CLI command in terminal

        :param cmd: commands for execution
        :param timeout: use special timeout step_result_enum, instead of default
        """
        # CMDS LIST ---------------------------------------------------------------------------------------------------
        if isinstance(cmd, (list, )):
            for cmd_item in cmd:
                if not self.send(cmd=cmd_item, timeout=timeout, _raise=_raise):
                    msg = f"[ERROR] {cmd_item=} in full sequence {cmd=}"
                    print(msg)
                    return False

        # params reinit -----------------------------------------------------------------------------------------------
        self._reinit_values()

        # params apply ------------------------------------------------------------------------------------------------
        self.last_cmd = cmd

        if timeout is None:
            timeout = self.TIMEOUT
        if _raise is None:
            _raise = self.RAISE

        # work --------------------------------------------------------------------------------------------------------
        # todo: check for linux! encoding is not necessary!
        self._last_sp = subprocess.Popen(args=cmd, text=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    #, encoding="cp866"
        try:
            self._last_sp.wait(timeout=timeout)
            self.last_stdout = self._last_sp.stdout.read()
            self.last_stderr = self._last_sp.stderr.read()
            self.last_retcode = self._last_sp.returncode
        except subprocess.TimeoutExpired as exx:
            self._last_exx_timeout = Exx_CliTimeout(repr(exx))

        self.last_finished = True
        self.print_state()

        if _raise:
            if self._last_exx_timeout:
                raise self._last_exx_timeout
            if self.last_retcode != 0:
                raise Exx_CliRetcode(self.last_retcode)
            if self.last_stderr:
                raise Exx_CliStderr(self.last_stderr)

        return self.last_finished_success

    # AUXILIARY -------------------------------------------------------------------------------------------------------
    @property
    def last_finished_success(self) -> Optional[bool]:
        """check if process last_finished correct

        :return: True if last_finished with no errors
        """
        return all([self.last_finished, self.last_retcode == 0, not self.last_stderr, not self._last_exx_timeout])

    def print_state(self) -> None:
        print(f"="*50)
        if not self.last_finished_success:
            print(f"[{'#'*21}ERROR{'#'*21}]")
        print(f"{self.last_cmd=}")
        print(f"{self.last_finished_success=}")
        print(f"{self.last_finished=}")
        print(f"{self.last_retcode=}")
        print(f"-" * 50)
        print("self.last_stdout=")
        if self.last_stdout:
            for line in self.last_stdout.split("\n"):
                print(f"\t{line}")
        print(f"-"*50)
        print("self.last_stderr=")
        if self.last_stderr:
            for line in self.last_stderr.split("\n"):
                print(f"\t{line}")
        print(f"-" * 50)
        print(f"{self._last_exx_timeout=}")
        print(f"="*50)

    def cli_check_available(self) -> bool:
        """check list of commands which will show that further work will executable and your environment is ready.

        Useful because commands uwually depends on installed programs and OS.
        so if you want to be sure of it on start point - run it!
        """
        if self.CMDS_REQUIRED:
            for cmd, error_msg in self.CMDS_REQUIRED.items():
                if not self.send(cmd, _raise=False):
                    msg = f"[ERROR] cmd NOT available [{cmd}]"
                    print(msg)
                    self.print_state()
                    return False
        return True


# =====================================================================================================================
