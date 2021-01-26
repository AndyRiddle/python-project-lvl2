from gendiff.functions.generate_differences import generate_diff
from gendiff.functions.open_json_file import get_data_from_json_file
from gendiff.functions.output_differences import output_diff
from gendiff.functions.search_differences import identify_and_save_differences

# Error: Wrong module metadata violation
# Justified use meta-variable __all__
__all__ = (  # noqa: WPS410
    'generate_diff',
    'get_data_from_json_file',
    'identify_and_save_differences',
    'output_diff',
)
