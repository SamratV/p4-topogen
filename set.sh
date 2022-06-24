#!/bin/bash

PROJ="$HOME""/project/pubsub/"
DIRS=("./4s_8h/" "./8s_16h/")

DIR=${DIRS[$1]}

cp "$DIR""clone.json" "$PROJ""clone.json"
cp "$DIR""rules.json" "$PROJ""rules.json"
cp "$DIR""topo.json" "$PROJ""topology2.json"

rm -r "$DIR""inputs"
mkdir "$DIR""inputs"

./input.sh $1

rm -r "$PROJ""inputs"
mkdir "$PROJ""inputs"

cp -R "$DIR""inputs/." "$PROJ""inputs"