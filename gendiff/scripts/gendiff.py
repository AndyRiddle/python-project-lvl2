#!/usr/bin/env python
import argparse

from gendiff import generate_diff


def main():

    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output',
    )
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    formater = args.format

    return generate_diff(first_file, second_file, formater)


if __name__ == '__main__':
    main()
