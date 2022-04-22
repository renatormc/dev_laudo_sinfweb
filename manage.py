import argparse
from manage import config
from manage import actions as act
import os

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action="store_true",
                    help="Verbose mode")
subparsers = parser.add_subparsers(
    dest="command", required=True, help='Command to be used')

p_prepare = subparsers.add_parser("prepare")
p_prepare.add_argument("direction", choices=(
    "up", "down"), help="Direction up or down")

p_dist = subparsers.add_parser("dist")

p_db_migrate = subparsers.add_parser("db_migrate")
p_db_upgrade = subparsers.add_parser("db_upgrade")
p_db_downgrade = subparsers.add_parser("db_downgrade")


args = parser.parse_args()
config.verbose = args.verbose


if args.command == "prepare":
    act.prepare(args.direction)
elif args.command == "dist":
    act.dist()
elif args.command == "db_migrate":
    os.system("alembic revision --autogenerate -m \"teste\"")
elif args.command == "db_upgrade":
    os.system("alembic upgrade head")
elif args.command == "db_downgrade":
    os.system("alembic downgrade head")
