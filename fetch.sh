#!/bin/bash

PROJ="$HOME""/project/pubsub/"

HOST_LOG="$PROJ""outputs"
SWITCH_LOG="$PROJ""logs"
OUT_FILE="data.json"

rm $OUT_FILE

echo "{" >> $OUT_FILE

for file in $SWITCH_LOG/*.log
do
    valid_apph=$(grep 'hdr.apph.isValid' $file | grep true$ | grep -v 'includes/egress.p4' | wc -l)
    from_cpu=$(grep 'hdr.apph.isValid' $file | grep true$ | grep -v 'includes/egress.p4' | grep CPU_PORT | wc -l)
    to_cpu=$(grep 'out of port 255' $file | wc -l)

    swname=$(echo $file | rev | cut -d\/ -f1 | rev | cut -d. -f1)

	echo "	\"$swname\": {" >> $OUT_FILE
	echo "		\"valid_apph\":$valid_apph""," >> $OUT_FILE
	echo "		\"from_cpu\":$from_cpu""," >> $OUT_FILE
	echo "		\"to_cpu\":$to_cpu" >> $OUT_FILE
	echo "	}," >> $OUT_FILE
done

CURR_COUNT=0
FILE_COUNT=$(ls -1 $HOST_LOG/ | wc -l)

for file in $HOST_LOG/*
do
	let CURR_COUNT++

    rep=$(grep old$  $file | wc -l)
    pub=$(grep 'SND: sending publish\|RCV: received publish' $file | wc -l)
    sub=$(grep 'SND: sending subscribe\|RCV: received subscribe' $file | wc -l)
    not=$(grep 'SND: sending notify\|RCV: received notify' $file | wc -l)
    req=$(grep 'SND: sending request\|RCV: received request' $file | wc -l)
    res=$(grep 'SND: sending response\|RCV: received response' $file | wc -l)

    hostname=$(echo $file | rev | cut -d\/ -f1 | rev | cut -d. -f1)

	echo "	\"$hostname\": {" >> $OUT_FILE
	echo "		\"repeated\":$rep""," >> $OUT_FILE
	echo "		\"publish\":$pub""," >> $OUT_FILE
	echo "		\"subscribe\":$sub""," >> $OUT_FILE
	echo "		\"notify\":$not""," >> $OUT_FILE
	echo "		\"request\":$req""," >> $OUT_FILE
	echo "		\"response\":$res" >> $OUT_FILE

	if [[ CURR_COUNT -eq FILE_COUNT ]]; then
		echo "	}" >> $OUT_FILE
	else
		echo "	}," >> $OUT_FILE
	fi
	
done

echo "}" >> $OUT_FILE