#!/usr/bin/env python
import sys 

def main(args):
    print("Hello from simple python script!")
    print("Passed args: {}".format(args))
    exit(0)


if __name__ == "__main__":
    main(sys.argv)