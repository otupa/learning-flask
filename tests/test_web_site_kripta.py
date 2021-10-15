"""Tests For Flask-App Web Site"""


def test_app_name(app_instance):
    """Test application name"""
    assert app_instance.name == "web_site_kripta.web_site_kripta"
