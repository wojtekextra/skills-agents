import pytest
import os
from unittest.mock import patch, MagicMock

from mailer.web import create_app, load_config


def test_load_config():
    """Test czy konfiguracja ładuje się z env zmiennych"""
    config = load_config()
    assert "SMTP_SERVER" in config
    assert "SMTP_PORT" in config


def test_create_app():
    """Test czy aplikacja Flask się tworzy"""
    app = create_app()
    assert app is not None
    assert app.secret_key is not None


@pytest.mark.skipif(
    not os.path.exists("templates/index.html"),
    reason="Template file not available",
)
def test_subscribe_integration():
    """Integration test dla subscribe route"""
    app = create_app({"TESTING": True})
    client = app.test_client()

    response = client.post(
        "/subscribe", data={"email": "test@example.com"}, follow_redirects=False
    )
    assert response.status_code == 302
