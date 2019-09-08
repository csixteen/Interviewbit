#!/bin/bash
cat sbf.txt | tr -s ' ' '\n' | sort | uniq -c | sort | tr -s '[:space:]' | awk -F' ' '$1==last {printf " %s",$2; next} NR>1 {print "";} {last=$1; printf "%s",$0;} END{print "";}' | sed "s/^[ \t]*//"
