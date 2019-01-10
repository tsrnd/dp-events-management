#!/bin/sh
docker-compose run app sh ./scripts/pylint.sh
pip install -U lintly
# shellcheck disable=SC2086
lintly --format=pylint-json --api-key=$GITHUB_ACCESS_TOKEN < ./.tmp/reports/pylint.json
