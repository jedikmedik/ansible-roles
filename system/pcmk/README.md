pcmk
====
Setup Pacemaker + Corosync cluster (w/o resources)
## Variables
```yaml
pcmk_pool: string # Pool name; MANDATORY
pcmk_cluster_name: string # Cluster name; default: CLUSTER-{{ pcmk_pool|upper }}
pcmk_pcsd_restart_daily: bool # default: false
```
## Inventory
```ini
[<pcmk_pool>] ; group with cluster members
node1
node2
; ...
```
## Notes
### Replace failed node
Failed node replacing is not implemented. Do it manually if necessary. (`[c]` - cluster node, `[n]` - new node)
```
[c] ~# pcs cluster node remove --force nodeF
(.. node reinstalling ..)
[n] ~# yum install pcs
[c] ~# pcs cluster auth nodeF
[c] ~# pcs cluster node add nodeF
[n] ~# pcs cluster start
```
