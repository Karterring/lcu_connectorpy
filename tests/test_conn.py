from lcu_connectorpy import Connector


def test_client():
    conn = Connector()
    conn.start()

    assert conn.connected

