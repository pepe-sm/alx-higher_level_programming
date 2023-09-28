#!/bin/bash
# curl content length to get body size
curl -s "$1" | wc -c
