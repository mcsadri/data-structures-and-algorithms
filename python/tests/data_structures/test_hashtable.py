import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


@pytest.fixture
def hashtable():
    return Hashtable()


def test_set_key_value(hashtable):
    hashtable.set("key1", "value1")
    assert hashtable.get("key1") == "value1"


def test_retrieve_existing_key(hashtable):
    hashtable.set("key2", "value2")
    assert hashtable.get("key2") == "value2"


def test_retrieve_nonexistent_key(hashtable):
    assert hashtable.get("nonexistent_key") is None


def test_unique_keys(hashtable):
    hashtable.set("key3", "value3")
    hashtable.set("key4", "value4")
    hashtable.set("key5", "value5")
    assert set(hashtable.keys()) == {"key3", "key4", "key5"}


def test_collision_handling(hashtable):
    # Set two keys that collide
    hashtable.set("key6", "value6")
    hashtable.set("key106", "value106")
    assert hashtable.get("key6") == "value6"
    assert hashtable.get("key106") == "value106"


def test_retrieve_value_from_collision_bucket(hashtable):
    hashtable.set("key7", "value7")
    hashtable.set("key107", "value107")
    assert hashtable.get("key7") == "value7"
    assert hashtable.get("key107") == "value107"


def test_hash_key_in_range(hashtable):
    hash_value = hashtable.hash("key8")
    assert 0 <= hash_value < hashtable.size
