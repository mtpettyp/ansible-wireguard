[![CircleCI](https://circleci.com/gh/mtpettyp/ansible-wireguard.svg?style=svg)](https://circleci.com/gh/mtpettyp/ansible-wireguard)



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


License
-------

MIT

