[![Test](https://github.com/mtpettyp/ansible-wireguard/actions/workflows/test.yml/badge.svg)](https://github.com/mtpettyp/ansible-wireguard/actions/workflows/test.yml)



Wireguard
=========

Wireguard role


Role Variables
--------------

* `route_address` - Address range the node should route traffic for (defaults to 10.0.0.1/24)
* `wireguard_ui.password` - Password for Wireguard UI

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    route_address: 10.0.0.1/24
    wireguard_ui:
      password: abc123
  include_role:
    name: "ansible-wireguard"
```


Development
-----------

Install dependencies:

```bash
uv sync
```

Run molecule tests:

```bash
uv run molecule test
```


License
-------

MIT
