#!/usr/bin/env bash

SRC="restaurant_proj"
imageName="restaurant"
serviceName="restaurant_img"
imageRepo="$imageName"

version="$(python $SRC/restaurant_proj/settings.py)"
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
