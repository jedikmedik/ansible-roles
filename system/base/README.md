base
====
Base role for Slurm iac-ansible.
+ Set SELinux state;
+ set hostname;
+ install [some packages](vars/main.yml);
+ setup `etckeeper`;
+ configure journald;
+ configure ntpd;
+ populate `/etc/hosts`;
+ optionally setup zsh and set prompt theme.
## Variables
```yaml
base_selinux_state: string # enforcing (default), permissive or disabled

base_ntp_custom_servers: [] # Optional set NTP servers (FQDN list)
base_ntp_pool: [] # ru (default), de, etc.

base_sysctl_vars:
  key: value

base_zsh_enable: bool # default: false

env: string # prod, test, aux. Use for shell prompt colorization.
```
