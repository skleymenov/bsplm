"""Bench scale PLM"""

__version__ = "0.0.0"  # auto replace by poetry-dynamic-versioning

package_name = __name__
authors = (("Sergey Kleymenov", "sergeykleymenov@gmail.com"),)

authors_email = ", ".join(f"{email}" for _, email in authors)

__license__ = "MIT"
__author__ = ", ".join(f"{name} <{email}>" for name, email in authors)

# It's same persons right now
__maintainer__ = __author__

__all__ = (
    "__author__",
    "__license__",
    "__maintainer__",
    "__version__",
)
