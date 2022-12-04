import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("firstArg")
parser.add_argument("secondArg", type=int)


args = parser.parse_args()

print(args)

print(f"command is: {sys.argv[0]}")
print (f"first arg is {args.firstArg}")
print (f"second arg is {args.secondArg}")

#python argParseDemo.py --help
