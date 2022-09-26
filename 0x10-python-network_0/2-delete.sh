#!/bin/bash
# sends a DELETE request to the URL passed and displays response body
curl -s "$1" -X DELETE
