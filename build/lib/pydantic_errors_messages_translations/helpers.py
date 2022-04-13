
from typing import List
from pydantic import ValidationError


def _display_errors(errors: List[dict]) -> str:
    return '\n \n'.join(f'{_display_error_loc(e)}:\n  - {e["msg"]}' for e in errors)


def _display_error_loc(error: dict) -> str:
    return ' -> '.join(str(e) for e in error['loc'])


def convert_error_to_human_readable(errors: dict) -> str:
    return _display_errors(errors)
