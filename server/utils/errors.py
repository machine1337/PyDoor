import sys
import traceback


def errors(error: Exception, line: bool = True) -> str:
    """ Error Handler """
    error_class = error.__class__.__name__
    error_msg = f'{error_class}:'
    try:
        error_msg += f' {error.args[0]}'
    except IndexError:
        pass
    if line:
        _, _, traceb = sys.exc_info()
        line_number = traceback.extract_tb(traceb)[-1][1]
        error_msg += f' (line {line_number})'
    return error_msg