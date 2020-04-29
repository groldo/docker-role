# docker-role

Install docker on host with ansible.

## Role Variables

You can add multiple docker users to the docker group.

```yaml
docker_apt_release_channel: stable
docker_users: ["vagrant"]
```

## Exmple playbook

    - hosts: servers
      roles:
         - role: docker-role
           vars:
             docker_users: ["vagrant"]

## Usage as dependency

You could also use it as dependency for another role, which relies on docker.
But keep in mind that this dependency is checked every time when the the dependent role is called.
This can be pretty annoying.

requirements.yml
Place this file inside the dependent role

    ---
    - name: docker-role
    src: https://github.com/groldo/docker-role
    version: master

meta/main.yml

    dependencies: [
    "docker-role",
    "traefik-role"
    ]

## reset_connection.yml

A note to the reset_connection.yml.
When adding a user to a group this takes effect after a log out from the running session.
Ansible is trying to minimize the established connections to a host.
After hitting the world wide web my preferred way is to remove the socket which ansible creates,
as all the other smart solutions doesn't seem to work( reconnect via meta, or disable ssh pipelining).