#!/bin/bash
pico2wave -l=en-GB -w=/tmp/test.wav "$1"
aplay /tmp/test.wav
rm /tmp/test.wav
