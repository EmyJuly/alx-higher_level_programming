#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
<<<<<<< HEAD
    Exception:
=======
    except:
>>>>>>> 2959e380c658609e86b0fbe28d61b364ab81e691
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
