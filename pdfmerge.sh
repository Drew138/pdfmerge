#!/bin/bash

DEFAULT="combined_file.pdf"
NAME=${1:-$DEFAULT}

python3 ~/python/pdfmerge/fusion.py $NAME
