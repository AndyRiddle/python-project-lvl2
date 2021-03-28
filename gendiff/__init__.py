# Error: Found backslash that is used for line breaking
# Permissible to use break line
from gendiff.formatters.format_diff import \
    STYLISH_FORMATTER as DEFAULT_FORMATTER  # noqa: N400
from gendiff.generate_diff import generate_diff

# Error: Wrong module metadata violation
# Justified use meta-variable __all__
__all__ = (  # noqa: WPS410
    'generate_diff',
    'DEFAULT_FORMATTER',
)
