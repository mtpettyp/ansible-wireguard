import pytest

"""Role testing services using testinfra."""


@pytest.mark.parametrize("name", [
    ("wg-quick@wg0"),
    ("wireguard-ui"),
    ("wgui.path")
])
def test_services(host, name):
    """Validate that services are enabled and running """
    service = host.service(name)
    assert service.is_enabled
    assert service.is_running


@pytest.mark.parametrize("name", [
    ("wgui.service")
])
def test_enabled(host, name):
    """Validate that services are enabled """
    service = host.service(name)
    assert service.is_enabled
