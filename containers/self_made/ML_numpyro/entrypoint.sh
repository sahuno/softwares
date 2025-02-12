#!/bin/bash

if [[ "$1" == "jupyter" ]]; then
    jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
else
    exec "$@"
fi

