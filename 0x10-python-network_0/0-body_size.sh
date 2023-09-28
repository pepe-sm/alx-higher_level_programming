#!/bin/bash
# curl content length to get body size
curl --head "$1" | grep 'Content-Length' | cut -d " " -f 2
