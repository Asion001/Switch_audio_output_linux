#! /bin/python3
import os

default_sink = os.popen("pactl info|grep Sink").read().split()[2]
sinks = os.popen("pactl list short sinks").read().split()
sink_input = os.popen("pactl list short sink-inputs").read().split()

index = 0
sink = []
switch_index = []
debug = []

def change():
    os.system("pactl set-default-sink " + nextsink)
    for num in switch_index:
        debug.append("pactl move-sink-input " + num + " " + nextsink)
        os.system("pactl move-sink-input " + num + " " + nextsink)

for num in sinks:
    if num == str(index):
        index +=1
        sink.append(sinks[sinks.index(num) + 1])

nextsink = sink.index(default_sink)
if nextsink == len(sink) - 1: nextsink = sink[0]
else : nextsink = sink[sink.index(default_sink) + 1]


for num in range(0,len(sink_input),7):
    if sink_input[num] != "-": switch_index.append(sink_input[num])

change()

if False:
    print('default_sink - ', default_sink)
    print('sinks - ', sink)
    print('nextsink - ', nextsink)
    print('sinkinput - ', sink_input)
    print('sw inde - ', switch_index)
    print(debug)

exit(0)