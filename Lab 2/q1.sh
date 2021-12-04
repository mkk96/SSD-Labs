#!/bin/bash
if [ "$#" -ne 3 ]
then
    echo "Error: Wrong argument program require 3 argument"
elif [[ $1 =~ [a-z]+ ]] || [[ $2 =~ [a-z]+ ]] || [[ $3 =~ [a-z]+ ]]
then 
    echo "Error:One or more argument is String"
else
    echo "scale=2 ;$1 + $2 -$3"|bc    
fi
