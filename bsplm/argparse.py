from configargparse import ArgumentParser

ENV_VAR_PREFIX = "BSPLM_"


def add_inventory_args(parser: ArgumentParser):
    group = parser.add_argument_group("Inventory tools")
    group.add_argument("--check-inventory", action="store_true", default=True, help="Check inventory integrity")
    group.add_argument("--sort-inventory", action="store_true", help="Sort inventory by PartNumbers")


parser = ArgumentParser(auto_env_var_prefix=ENV_VAR_PREFIX)
add_inventory_args(parser)
