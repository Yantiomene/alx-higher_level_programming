#!/bin/bash
# Sends a URL request and display the body response size
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
