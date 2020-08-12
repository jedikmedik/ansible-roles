gitlab-runner
=============
Install and register gitlab-runner.
+ Only one [[runner]] per node is currently supported
+ optionally setup python-virtualenv with ansible.
## Variables
```yaml
runner_url: uri # Runner URL [$CI_SERVER_URL]
runner_reg_token: string # Runner's registration token [$REGISTRATION_TOKEN]
runner_description: string # Runner name (default: inventory_hostname) [$RUNNER_NAME]
runner_tags: [] # Tag list [$RUNNER_TAG_LIST]

runner_config:
  concurrent: int # Jobs concurrency (default: 1)
  run_untagged: bool # Register to run untagged builds (default: false) [$REGISTER_RUN_UNTAGGED]
  custom_build_dir: bool # Enable job specific build directories (default: false) [$CUSTOM_BUILD_DIR_ENABLED]

runner_ansible: bool # Create virtualenv with ansible installed
runner_ansible_version: version # REQUIRED if runner_ansible

runner_ansible_cfg: # optional
  - section: string
    options:
      <key>: <value>

runner_ansible_packages:
  - python-virtualenv
  - python-pip
  - python2-mitogen
  - unzip

runner_ansible_libs:
  - "ansible=={{ runner_ansible_version }}"
  - netaddr
  - selinux
  - jmespath
```
