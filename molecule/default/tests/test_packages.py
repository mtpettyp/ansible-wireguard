import pytest

"""Role testing packages using testinfra."""


@pytest.mark.parametrize("package", [
    ("wireguard"),
    ("ufw")
])
def test_packages(host, package):
    """Test that the appropriate packages were installed."""
    assert host.package(package).is_installed
