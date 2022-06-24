#!/bin/bash

NUMH=(8, 16)
NUMP=(4, 32)
NUMS=(4, 32)
DIRS=("./4s_8h/" "./8s_16h/")

DIR=${DIRS[$1]}
PUBS=${NUMP[$1]}
SUBS=${NUMS[$1]}
HOSTS=${NUMH[$1]}

OUT_DIR="$DIR""/inputs"
TOPIC_FILE="topics.json"


let TOPICS="$(sed '/[{}]/d' $TOPIC_FILE | wc -l)"
echo "topics = $TOPICS"
rm -f $OUT_DIR/*

for i in $(seq $HOSTS)
do
    file="$OUT_DIR/h$i.txt"

    # SUBS
    topic_id="$(shuf -i 0-$[$TOPICS-1] -n $SUBS)"
    for j in $topic_id
    do
        topic_name=$(grep -E \ $j,?$ $TOPIC_FILE | awk '{print $1}' | sed 's/[":]//g')
        echo  "subscribe,$topic_name,0,." >> $file
    done
    
    # PUBS
    usable=$(seq 0 $[$TOPICS - 1]) 
    for j in $topic_id
    do 
        usable=$(echo $usable | sed s/$j//)
    done
    
    for j in $(seq $PUBS)
    do
        let rand=$[$RANDOM % $PUBS]
        let rand++
        topic_id2=$(echo $usable | cut -d' ' -f $rand)
        topic_name=$(grep -E \ $topic_id2,?$ $TOPIC_FILE | awk '{print $1}' | sed 's/[":]//g')
        let counter_$topic_id2++
        content="${topic_name}_content_$[counter_$topic_id2]"
        echo "publish,$topic_name,30,$content" >> $file
    done

    shuf $file -o $file
done