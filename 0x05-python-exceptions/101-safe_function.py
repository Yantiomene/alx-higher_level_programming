#!/usr/bin/python3
def safe_function(fct, *args):
    '''Safe execute a function'''
    import sys

    try:
        val = fct(*args)
    except Exception as ex:
        val = None
        sys.stderr.write("Exception: {}\n".format(ex))
    finally:
        return (val)
