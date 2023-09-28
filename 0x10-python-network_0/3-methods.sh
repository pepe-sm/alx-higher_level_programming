#!/bin/bash
# takes url and displays http method server will take
curl -sI $1 | grep 'Allow' | cut -d " " -f2-
