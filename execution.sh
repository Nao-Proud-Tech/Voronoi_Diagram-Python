#!/bin/bash

# Setting command line arguments
DATA_NUM=5000
IMG_W=512
IMG_H=512
LINE_TYPE=8
C_MAP='gnuplot'

mkdir -p data

python3 make_img.py \
    --data_num ${DATA_NUM} \
    --height ${IMG_H} \
    --width ${IMG_W} \
    --type ${LINE_TYPE} \
    --cmap ${C_MAP} \
