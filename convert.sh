#!/bin/bash
for file in $(ls | grep .ipynb)
do
    jupyter nbconvert --to html $file
done
