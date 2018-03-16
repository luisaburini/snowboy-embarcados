#!/bin/bash

echo "36" > /sys/class/gpio/export
echo "37" > /sys/class/gpio/export
echo "38" > /sys/class/gpio/export
echo "39" > /sys/class/gpio/export
echo "170" > /sys/class/gpio/export

echo "out" > /sys/class/gpio/gpio36/direction
echo "out" > /sys/class/gpio/gpio37/direction
echo "out" > /sys/class/gpio/gpio38/direction
echo "out" > /sys/class/gpio/gpio39/direction
echo "out" > /sys/class/gpio/gpio170/direction

SPATH="/home/root/apalis-imx6"

python ${SPATH}/demo-embarcados.py ${SPATH}/snowboy.umdl ${SPATH}/alexa.umdl 
