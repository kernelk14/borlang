#!/usr/bin/env python3

import os
import getopt
import sys

program = '''write "Hello"'''

def usage():
    print("""
Borlang Programming Language, created by Khyle Isaias at https://github.com/kernelk14

help:
    borlang [subcommand] <program>

    subcommands:
          -h    --help            Print this help message
""")

def interpret(program):
    for p, op in enumerate(program):
        print(program.split())


def run(program):
    #  TODO: Make a run definition for the code.
    interpret(program)
usage()
# run(program)