[![CircleCI](https://circleci.com/gh/mtpettyp/ansible-wireguard.svg?style=svg)](https://circleci.com/gh/mtpettyp/ansible-wireguard)



Wireguard
=========

Wireguard role


Role Variables
--------------

* `route_address` - Address range the node should route traffic for (defaults to 10.0.0.1/24)
* `peers` - List of peers to create
    * `name` - Peer name
    * `public_key` - Public key of peer
    * `allowed_ips` - IPs of peer (set in client's `Address` under `[Interface]`)

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    route_address: 10.0.0.1/24
    peers:
      - name: server1
        public_key: 6SeYZu1fy/yoG4EDZwCZ9yZbEMKBL0un3EzcyOYCQAw=
        allowed_ips: 10.0.0.2/24
      - name: server2
        public_key: C2pw84c7zwaTuoQbuYiGjCBHIKtedRMB1EYc+GkhTis=
        allowed_ips: 10.0.0.3/24
  include_role:
    name: "ansible-wireguard"
```


License
-------

MIT

