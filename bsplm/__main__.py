import os

from bsplm import __version__ as bsplm_version
from bsplm.argparse import parser


def main():
    print(f"bench scale PLM version {bsplm_version}")
    arguments = parser.parse_args()
    print(os.getcwd())
    print(arguments)


if __name__ == "__main__":
    main()
