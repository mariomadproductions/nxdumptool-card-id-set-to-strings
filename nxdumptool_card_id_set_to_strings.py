#!/usr/bin/env python3
import argparse
from pathlib import Path

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser.parse_args()

def main():
    args = get_args()
    input_file_path = Path(args.file)

    if input_file_path.stat().st_size != 12:
        raise ValueError('Wrong file size')
    
    with open(input_file_path, 'rb') as file:
        print('Card ID 1: ' + file.read(4).hex().upper())
        print('Card ID 2: ' + file.read(4).hex().upper())
        print('Card ID 3: ' + file.read(4).hex().upper())

if __name__ == '__main__':
    main()
