nginx
=====
* Устанавливает пакеты nginx и модулей;
* создает типовой набор конфигов nginx и связанные конфиги logrotate и monit;
* генерирует самоподписанные сертификаты для default_server/

(Упрощённый вариант для Slurm IaC)
## Variables
```yaml
nginx_core:
  worker_processes: int # default: 'auto'
  worker_rlimit_nofile: int # default: 65536
  worker_connections: int # default: 16384

nginx_http:
  large_client_header_buffers: string # default: '8 8k'
  server_names_hash_max_size: int # default: undefined (512) <- сначала крутить это, а не server_names_hash_bucket_size
  server_names_hash_bucket_size: int # default undefined (32|64|128)
  open_file_cache: string # default: 'max=1000 inactive=300s'
  open_file_cache_errors: bool # default: off
  open_file_cache_min_uses: int # default: 2
  open_file_cache_valid: intUNIT # default: 300s
  keepalive_timeout: int # default: 150
  reset_timedout_connection: bool # default: on

nginx_gzip:
  gzip_comp_level: int(1-9) # default: 3

nginx_http_directives: {} # Custom directives for http{} section in the nginx.conf (key: value)

nginx_modules_so: [] # list of loadable modules for load_module directives, format: module_name.so
nginx_modules_rpm: [] # list of loadable modules for installing (get available modules: yum list nginx-module\*)

nginx_default_server:
  http: bool # default: true
  https: bool # default: true

nginx_vhost_default:
  listen: [] # default: undefined (listen 80), format: [ address, ... ]

nginx_vhost_files: # optionally add entire files in /etc/nginx/vhosts.d
  - path # file path relative to files/

# Certbot

nginx_certbot:
  enable: bool # Default: true
  email: string # Default: noreply@southbridge.ru

# vhosts.d files copying from files/etc/nginx/vhosts.d

```
