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

prod*)
    export SETTINGS='config.ProductionConfig'
    exec foreman start
    ;;

*)
    export SETTINGS='config.ProductionConfig'
    exec python run_dev.py
    ;;
esac
