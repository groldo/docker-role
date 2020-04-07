"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_docker_users(host):
    """Validate if users are included in docker group"""
    user = host.user("vagrant")
    groups = user.groups
    assert "docker" in groups
