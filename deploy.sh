#!/bin/bash
set -e

MACHINE_ID=1 PORT=8001 nohup python server.py &
MACHINE_ID=2 PORT=8002 nohup python server.py &

sudo systemctl start nginx

while sleep 60; do
    echo "running"
done