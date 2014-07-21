#!/bin/bash

export PORT=5000

case "$1" in
dev*)
    export SETTINGS='config.DevelopmentConfig'
    exec python run_dev.py
    ;;

test)
    export SETTINGS='config.TestConfig'
    exec py.test
    ;;

*)
    export SETTINGS='config.Config'
    exec foreman start
esac
