import json
import pytest
from pathlib import Path
import tempfile

from mailer.subscribers import SubscriberManager


@pytest.fixture
def temp_storage():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        temp_path = f.name
    yield temp_path
    Path(temp_path).unlink(missing_ok=True)


def test_add_subscriber(temp_storage):
    manager = SubscriberManager(storage_path=temp_storage)

    result = manager.add_subscriber("user@example.com")
    assert result is True
    assert "user@example.com" in manager.list_subscribers()


def test_add_duplicate_subscriber(temp_storage):
    manager = SubscriberManager(storage_path=temp_storage)

    manager.add_subscriber("user@example.com")
    result = manager.add_subscriber("user@example.com")

    assert result is False
    assert len(manager.list_subscribers()) == 1


def test_add_empty_email(temp_storage):
    manager = SubscriberManager(storage_path=temp_storage)

    result = manager.add_subscriber("")
    assert result is False
    assert len(manager.list_subscribers()) == 0


def test_remove_subscriber(temp_storage):
    manager = SubscriberManager(storage_path=temp_storage)

    manager.add_subscriber("user@example.com")
    result = manager.remove_subscriber("user@example.com")

    assert result is True
    assert len(manager.list_subscribers()) == 0


def test_remove_nonexistent_subscriber(temp_storage):
    manager = SubscriberManager(storage_path=temp_storage)

    result = manager.remove_subscriber("user@example.com")
    assert result is False


def test_list_subscribers(temp_storage):
    manager = SubscriberManager(storage_path=temp_storage)

    manager.add_subscriber("user1@example.com")
    manager.add_subscriber("user2@example.com")

    subscribers = manager.list_subscribers()
    assert len(subscribers) == 2
    assert "user1@example.com" in subscribers
    assert "user2@example.com" in subscribers


def test_persistence(temp_storage):
    manager1 = SubscriberManager(storage_path=temp_storage)
    manager1.add_subscriber("user@example.com")

    manager2 = SubscriberManager(storage_path=temp_storage)
    subscribers = manager2.list_subscribers()

    assert "user@example.com" in subscribers


def test_case_normalization(temp_storage):
    manager = SubscriberManager(storage_path=temp_storage)

    manager.add_subscriber("User@Example.COM")
    manager.add_subscriber("user@example.com")

    assert len(manager.list_subscribers()) == 1
    assert "user@example.com" in manager.list_subscribers()


def test_whitespace_trimming(temp_storage):
    manager = SubscriberManager(storage_path=temp_storage)

    manager.add_subscriber("  user@example.com  ")
    assert "user@example.com" in manager.list_subscribers()
