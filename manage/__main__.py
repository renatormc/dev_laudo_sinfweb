import argparse
from . import config
from . import actions as act


parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action="store_true",
                    help="Verbose mode")
subparsers = parser.add_subparsers(
    dest="command", required=True, help='Command to be used')

p_prepare = subparsers.add_parser("prepare")
p_prepare.add_argument("direction", choices=(
    "up", "down"), help="Direction up or down")

p_dist = subparsers.add_parser("dist")

args = parser.parse_args()
config.verbose = args.verbose


if args.command == "prepare":
    act.prepare(args.direction)
elif args.command == "dist":
    act.dist()
