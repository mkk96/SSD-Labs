#!/bin/bash
grep -w -i "is" $1
tail -n `wc $1  | awk '{print (int($1/2)+5) }' `  $1 | head -n 10
awk '{print $3,$5}' $1
