#!/bin/bash

function runOnPi(){
python moisture.py ;
python motiondetection.py &
python flame.py &
wait
}