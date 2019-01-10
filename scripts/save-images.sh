#!/bin/sh
mkdir -p "$HOME/.docker/images"
# shellcheck disable=SC2016
docker images -a -f dangling=false --format '{{.Repository}}:{{.Tag}} {{.ID}}' \
  | xargs -n 2 -t sh -c 'test -e $HOME/.docker/images/$1.tar.gz || docker save $0 | gzip -2 > $HOME/.docker/images/$1.tar.gz';
