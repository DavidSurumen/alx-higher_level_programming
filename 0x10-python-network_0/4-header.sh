#!/bin/bash
# Sends GET request, adds header variable, display response body
curl -sH "X-School-User-Id: 98" -G "$1"
