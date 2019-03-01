#!/bin/bash

### max number of processes
number=3

task() {
  ### Commands to run on file
}

i=0
while read -r line
do
  if (( i++ >= number ))
  then
    wait -n
  fi
  task "$line" &
done < list.of.files.txt
wait
