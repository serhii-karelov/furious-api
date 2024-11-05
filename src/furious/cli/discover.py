from importlib import import_module
from pathlib import Path
from fastapi import FastAPI
from furious.cli.exceptions import FuriousException
from furious.cli.config import get_config_key
from furious.cli.setup import is_set_up

"""
High-level of what we want: 
    read config
    if has workdir => set it
    if has app => import it
    otherwise => guess the module
        and get the app from the guessed module
"""


def guess_and_import_module():
    workdir = get_config_key("workdir")
    package_name = workdir.name
    potential_modules = (
        "main",
        "app",
        "main.main",
        "main.app",
        "app.main",
        "app.app",
        f"{package_name}.main",
        f"{package_name}.app",
    )
    for m in potential_modules:
        try:
            module = import_module(m)
        except ImportError:
            continue

        if module.__file__:  # return if not a package.
            return module  # otherwise, continue

    raise FuriousException(
        "Module with the FastAPI application cannot be found. "
        'Please specify it explicitly in pyproject.toml -> [tools.furious] -> app = "main.app:app"'
    )


def import_app():
    assert is_set_up()
    app_path = get_config_key("app")

    if app_path is None:
        module = guess_and_import_module()
        return find_app(module)
    else:
        module_name, app_name = app_path.rsplit(":", 1)
        module = import_module(module_name)
        return getattr(module, app_name)


def find_app(module):
    for obj in module.__dict__.values():
        if isinstance(obj, FastAPI):
            return obj
    raise FuriousException(
        "ASGI application cannot be discovered.\n"
        "You have to specify application path explicitly in pyproject.toml"
    )
