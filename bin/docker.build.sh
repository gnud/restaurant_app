#!/usr/bin/env bash

SRC="restorant_proj"
imageName="restaurant"
serviceName="restaurant_img"
imageRepo="$imageName"

version="$(python $SRC/restorant_proj/settings.py)"
echo $version

dockerPath() {
    echo $1;
    if [[ -z $1 ]]; then
        echo ".";
    else
        echo "$1";
    fi
}

docker image build --compress -t $imageRepo:$version $(dockerPath)
