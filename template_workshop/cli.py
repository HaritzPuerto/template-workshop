"""CLI interface for template_workshop project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

import argparse
from .fibonacci import Fibonacci


def parse_args():
    parser = argparse.ArgumentParser(description="Fibonacci calculator")
    parser.add_argument(
        "n", type=int, help="The number to calculate the Fibonacci sequence"
    )
    return parser.parse_args()


##########################


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m template_workshop` and `$ template_workshop `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    ##### YOUR CODE HERE #####
    args = parse_args()
    fib = Fibonacci()
    print(fib.fib(args.n))
    ##########################
