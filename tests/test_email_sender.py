import pytest
from unittest.mock import MagicMock, patch

from mailer.email_sender import EmailSender


@pytest.fixture
def email_sender():
    return EmailSender(
        smtp_server="smtp.test.com",
        smtp_port=587,
        username="test@test.com",
        password="testpass",
    )


def test_create_message(email_sender):
    message = email_sender.create_message("Test Subject", "Test Body", "user@example.com")

    assert message["From"] == "test@test.com"
    assert message["To"] == "user@example.com"
    assert message["Subject"] == "Test Subject"


@patch("mailer.email_sender.smtplib.SMTP")
def test_send_email_success(mock_smtp, email_sender):
    mock_smtp_instance = MagicMock()
    mock_smtp.return_value.__enter__.return_value = mock_smtp_instance

    result = email_sender.send_email("user@example.com", "Subject", "Body")

    assert result is True
    assert mock_smtp_instance.starttls.called
    assert mock_smtp_instance.login.called
    assert mock_smtp_instance.send_message.called


@patch("mailer.email_sender.smtplib.SMTP")
def test_send_bulk(mock_smtp, email_sender):
    mock_smtp_instance = MagicMock()
    mock_smtp.return_value.__enter__.return_value = mock_smtp_instance

    recipients = ["user1@test.com", "user2@test.com", "user3@test.com"]
    failed = email_sender.send_bulk(recipients, "Subject", "Body")

    assert len(failed) == 0
    assert mock_smtp_instance.send_message.call_count == 3


@patch("mailer.email_sender.smtplib.SMTP")
def test_send_bulk_with_failures(mock_smtp, email_sender):
    mock_smtp_instance = MagicMock()
    mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
    # Fail on second recipient
    mock_smtp_instance.send_message.side_effect = [None, Exception("SMTP error"), None]

    recipients = ["user1@test.com", "user2@test.com", "user3@test.com"]

    with patch.object(email_sender, "send_email", side_effect=[True, False, True]):
        failed = email_sender.send_bulk(recipients, "Subject", "Body")

    assert len(failed) == 1
    assert "user2@test.com" in failed
