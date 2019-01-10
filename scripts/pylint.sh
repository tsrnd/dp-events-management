#!/bin/sh
mkdir -p ./.tmp/reports
pylint myproject myapp --output-format=json > ./.tmp/reports/pylint.json
