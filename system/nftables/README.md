Role Name
=========

**[alpha]**

Install ans configure **nftables** (w/o firewalld) on CentOS 8 (and probably other el8 derivatives).

Requirements
------------

- CentOS 8
- Ansible >= 2.8

Role Variables
--------------
defaults:
```yaml
nftables:
  ip:
    nat:
      prerouting: []
      postrouting: []
```
vars:
```yaml
nftables_packages: [ nftables ]
```

Dependencies
------------

-

Example Configuraion
----------------

```yaml
nftables:
  ip:
    nat:
      prerouting:
        - iif "eth0" tcp dport { postgresql } dnat to 172.16.100.100
      postrouting:
        - ip daddr 172.16.100.100 oif "eth0" snat to 172.16.100.1
```
Resulting configuration in **/etc/sysconfig/nftables.conf**:
```
table ip nat {
        chain prerouting {
                type nat hook prerouting priority -100; policy accept;
                iif "eth0" tcp dport { postgresql } dnat to 172.16.100.100
        }

        chain postrouting {
                type nat hook postrouting priority 100; policy accept;
                ip daddr 172.16.100.100 oif "eth0" snat to 172.16.100.1
        }
}
```

License
-------

BSD

Author Information
------------------

Mesropyan Nikolay for https://southbridge.io/

