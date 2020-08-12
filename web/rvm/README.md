rvm
===
* install rvm
* install ruby
* setup puma service
## Variables
```yaml
rvm_ruby_version: int.int[.int] # REQUIRED

rvm_puma:
  - user: string # REQUIRED
    version: path # REQUIRED: puma binary version (/home/{{ user }}/app/vendor/bundle/ruby/{{ version }}/bin/puma)
    debug: bool # default: False
    vars: {} # variables e.q. DB_NAME, RAILS_ENV, ...
```
