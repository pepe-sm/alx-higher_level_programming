#!/bin/bash
# Output status ode
curl -sw '%{http_code}' -o /dev/null "$1"
