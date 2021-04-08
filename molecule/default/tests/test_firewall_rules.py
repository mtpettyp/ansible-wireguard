import pytest

"""Role testing services using testinfra."""


@pytest.mark.parametrize("rule", [
    ("51820/udp")
])
def test_ufw_rules(host, rule):
    """Validate that firewall rules are enabled and running """
    assert rule in host.run('ufw status').stdout
