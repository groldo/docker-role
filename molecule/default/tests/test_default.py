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


def test_docker_command(host):
    """check docker ps"""
    cmd = host.run("docker ps")

    assert cmd.rc == 0


def test_docker_compose_command(host):
    """check docker compose"""
    cmd = host.run("docker-compose --version")

    assert cmd.rc == 0
