#!/bin/sh
RESTART_EPOCH="${RESTART_EPOCH:-0}"
exec envoy --restart-epoch $RESTART_EPOCH --config-path /etc/envoy/envoy.yaml --parent-shutdown-time-s 30 --drain-time-s 20
