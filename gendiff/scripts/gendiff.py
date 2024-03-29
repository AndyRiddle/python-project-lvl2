#!/usr/bin/env python
import argparse

from gendiff import DEFAULT_FORMATTER, generate_diff


def main():

    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default=DEFAULT_FORMATTER,
        help='set format of output',
    )
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format

    print(generate_diff(first_file, second_file, formatter))


if __name__ == '__main__':
    main()
