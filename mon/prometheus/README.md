prometheus
==========
Install **prometheus** and some exporters
- node_exporter
- nginxlog-exporter
## Variables
```yaml
prom_master: bool # default: false
prom_version: version # default: 2.12.0
prom_node_exporter_version: version # default: 0.18.1

prom_config_global:
  scrape_interval: time # default: 15s
  evaluation_interval: time # default: 15s

prom_cmdline:
  tsdb_retention_time: time # default: 15d

prom_grafana: bool # default: false

prom_nginxlog_exporter: bool # default: false
prom_nginxlog_exporter_version: version # default: 1.3.0
```
