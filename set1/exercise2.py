import argparse
import sys

parser = argparse.ArgumentParser(description="where:")
parser.add_argument("mapping", help = "26 letter char-mappig \n or an int-value")
parser.add_argument("-o", help = "keep non-letters as is, honor letter casing", action = "store_true")
parser.add_argument("-d", help = "decrypt", action = "store_true")
try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)
print(args.mapping)

