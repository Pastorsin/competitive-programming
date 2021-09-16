#!/bin/bash

[ $# -ne 1 ] && echo "ERROR - Missing argument: problem_name" && exit 1

PROBLEM_NAME=$1
ROOT="src"

dir_name=$(python3 -c "print('$PROBLEM_NAME'.lower().replace(' ', '_'))")
dir=$ROOT/$dir_name

mkdir $dir || exit 1

cp templates/main.py $dir
touch $dir/input

echo $dir