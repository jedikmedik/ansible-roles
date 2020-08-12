Role Name
=========

Download and unpack **terraform** binary from official site.

Requirements
------------

RHEL or CentOS (tested on CentOS 8)

Role Variables
--------------

```yaml
terraform:
  version: semver # Required
  osarch: string # linux_amd64 (default) or linux_386
  bin_path: path # default: /usr/bin
```

Dependencies
------------

none

License
-------

BSD

Author Information
------------------

Mesropyan Nikolay for https://southbridge.io/
