deploy-ruby-app
====
Build and deploy (rolling-update) ruby application (using nginx load-balancer and PostgreSQL database).

For use in `.gitlab-ci.yml` **only** with one of a following tags: `setup`, `build`, `deploy`.
## Variables
```yaml
deploy_app: string # app name
deploy_user: string # user for executing build tasks and running puma
deploy_repo: string # repository address

deploy_lb_node: inventory_name # Load balancer nginx node
deploy_pg_node: inventory_name # PostgreSQL node

deploy_build_cleanup: bool # default: false; do git clone every time before build
deploy_build_packages: [] # packages installed before build
deploy_secret_key_base: string

deploy_prod_db: # production database credentials
  name: string # db name
  user: string # db user
  password: string # db password
  host: address # db host address

deploy_test_db: { } # testing database credentials

deploy_prod_environment: # environment variables for build processes; example:
  RAILS_ENV: production
  SECRET_KEY_BASE: "{{ deploy_secret_key_base }}"
  DB_HOST: "{{ deploy_db['host'] }}"
  DB_NAME: "{{ deploy_db['name'] }}"
  DB_USER: "{{ deploy_db['user'] }}"
  DB_PASSWORD: "{{ deploy_db['password'] }}"

deploy_build_environment: { }
deploy_test_environment: { }

deploy_version: string # default: HEAD
```
