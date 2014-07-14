#!/bin/bash

export SETTINGS='config.Config'
export PORT=5000

if [[ $1 == "dev" ]]; then
    python run_dev.py
else
    foreman start
fi
