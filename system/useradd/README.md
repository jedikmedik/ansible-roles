useradd
=======
Заведение пользователей и групп. Роль не требует явного добавления в список `roles`.
## Variables
```yaml
useradd_users:
  - name: string # Name of the user to create, remove or modify.
    bashrc_insert: |
      block # Optionally add freeform block into user's .bashrc
    comment: string # Optionally sets the description (aka GECOS) of user account (default: '').
    groups: list # Optionally set list of groups user will be added to (default: '').
    shell: string # Optionally set the user's shell (default: /bin/bash).
    home: string # Optionally set the user's home directory.
    home_mode: "oct" # Optionally set the user's home directory access mode (default is 0700)
    password: string # Optionally set the user's password (plaintext)
    password_hash: string # Optionally set the user's password (hash)
    uid: int # Optionally sets the UID of the user.
    state: bool # Whether the account should exist or not (default: true)
    ssh_key: # Optionally sets the params of the generated SSH key
      generate: bool # Whether to generate a SSH key for the user in question. This will not overwrite an existing SSH key.
      type: string # Optionally specify the type of SSH key to generate (default: rsa).
    public_keys: # Optionally set list of public keys will be added to authorized_keys
      - comment: string # Set the comment on the public key.
        type: string # Optionally set key type (default: ssh-rsa)
        data: string # Sets public key data
        options: string # Optionally set a string of ssh key options to be prepended to the key in the authorized_keys file
        state: bool # Whether the given key should or should not be in the file (default: true)
    files: # Optionally put arbitrary file in user home dir from files/ inventory dir
      - src: path # Source file path relative to files/
        dest: path # Destination file path relative to home dir
        mode: "oct" # File mode (default is 0644)
        dirmode: "oct" # Mode of last directory in path (default is 0755)

useradd_groups:
  - name: string # Name of the group to manage.
    gid: int # Optional GID to set for the group.
    state: bool # Whether the group should be present or not on the remote host (default: true).
```
## Dependencies
none
