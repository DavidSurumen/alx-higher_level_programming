#!/bin/bash
# sends a POST request to URL, and display body of response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1" -X POST
