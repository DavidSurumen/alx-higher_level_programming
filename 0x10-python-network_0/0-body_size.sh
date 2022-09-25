#!/usr/bin/env bash
# Displays size of body of response from a URL
curl -sI "$1" | grep Content-Length | cut -d " " -f2
