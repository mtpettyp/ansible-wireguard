import pytest

"""Role testing users using testinfra."""


@pytest.mark.parametrize("public_key", [
    ("6SeYZu1fy/yoG4EDZwCZ9yZbEMKBL0un3EzcyOYCQAw="),
    ("C2pw84c7zwaTuoQbuYiGjCBHIKtedRMB1EYc+GkhTis=")
])
def test_peers(host, public_key):
    """Validate that WireGuard is setup correctly """
    assert "peer: " + public_key in host.run("wg show").stdout
