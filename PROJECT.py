from typing import *


# =====================================================================================================================
class PROJECT:
    # AUX --------------------------------------------------
    _VERSION_TEMPLATE: Tuple[int] = (0, 0, 1)

    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_INSTALL: str = "cli-user"
    NAME_IMPORT: str = "cli_user"
    KEYWORDS: List[str] = [
        "cli", "cli user", "cli sender",
        "os terminal", "os terminal sender", "os terminal user",
    ]

    # GIT --------------------------------------------------
    DESCRIPTION_SHORT: str = "send commands into system terminal"

    # README -----------------------------------------------
    pass

    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
    DESCRIPTION_LONG: str = """
Designed to send commands into OS terminal
    """
    FEATURES: List[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "send commands into OS terminal",
        "check if cli commands are accessible (special utilities is installed)",
        "access to standard parts of result in a simple ready-to-use form (stdout/stderr/retcode/full state)",
        "use batch timeout for list",
        "till_first_true",
        "counter/counter_in_list",
    ]

    # HISTORY -----------------------------------------------
    VERSION: Tuple[int, int, int] = (0, 0, 7)
    VERSION_STR: str = ".".join(map(str, VERSION))
    TODO: List[str] = [
        "..."
    ]
    FIXME: List[str] = [
        "..."
    ]
    NEWS: List[str] = [
        "apply new pypi template",
        "add param print_all_states",
    ]


# =====================================================================================================================
if __name__ == '__main__':
    pass


# =====================================================================================================================
