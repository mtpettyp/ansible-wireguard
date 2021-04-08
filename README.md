[![CircleCI](https://circleci.com/gh/mtpettyp/ansible-wireguard.svg?style=svg)](https://circleci.com/gh/mtpettyp/ansible-wireguard)



Wireguard
=========

Wireguard role


Role Variables
--------------

* `route_address` - Address range the node should route traffic for (defaults to 0.0.0.0/0)
* `peers` - List of peers to create
    * `name` - Peer name
    * `public_key` - Public key of peer
    * `allowed_ips` - IPs to route for (defaults to 0.0.0.0/0)

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    route_address: 10.0.0.0/8
    peers:
      - name: server1
        public_key: 6SeYZu1fy/yoG4EDZwCZ9yZbEMKBL0un3EzcyOYCQAw=
      - name: server2
        public_key: C2pw84c7zwaTuoQbuYiGjCBHIKtedRMB1EYc+GkhTis=
        allowed_ips: 10.0.0.0/24
  include_role:
    name: "ansible-wireguard"
```


License
-------

MIT

