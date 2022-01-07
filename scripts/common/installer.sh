#!/usr/bin/env sh

set -e

if [ "$1" -eq 1 ]; then
    echo "----------------------"
    echo "Installing Dev Mode..."
    poetry install
else
    echo "-----------------------------"
    echo "Installing Production Mode..."
    poetry install --no-dev
fi