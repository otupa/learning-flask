"""Fixtures for tests in flask-app"""

from pytest import fixture

from web_site_kripta import create_app


@fixture(scope="module")
def app_instance():
    """This function create an app flask for tests"""
    return create_app()
