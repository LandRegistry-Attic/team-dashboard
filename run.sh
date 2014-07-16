#!/bin/bash

export PORT=5000

if [[ $1 == "dev" ]]; then
    export SETTINGS='config.DevelopmentConfig'
    python run_dev.py
else
    export SETTINGS='config.Config'
    foreman start
fi
