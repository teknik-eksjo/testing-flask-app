import pytest
from flask import url_for


def test_app_exists(app):
    assert app is not None


def test_app_is_testing(app):
    assert app.config['TESTING']
