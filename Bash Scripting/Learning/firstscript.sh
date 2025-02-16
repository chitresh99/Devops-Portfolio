#!/bin/bash

echo "Today is " `date`

echo -e "\nEnter the file path here"
read the_path

echo -e "\nPath has the following files and folders"
ls $the_path


