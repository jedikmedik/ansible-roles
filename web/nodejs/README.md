nodejs
======
Very simple role for nodejs installing
## Actions
+ Set up Nodejs rpm repo (`curl|bash` method, see https://github.com/nodesource/distributions/blob/master/README.md#rpm)
+ Install nodejs rpm package
## Variables
```yaml
nodejs_major_version: int # Mandatory
nodejs_yarn_install: bool # default: false
```
## Dependencies
-
