#! /bin/python3
import os                                                                   #import os lib

default_sink = os.popen("pactl info|grep Sink").read().split()[2]           #default audio output device name set to var 
sinks = os.popen("pactl list short sinks").read().split()                   #all audio output device name set to var 
sink_input = os.popen("pactl list short sink-inputs").read().split()        #now audio output device name set to var 

                                                                            #temp var
index = 0
sink = []
switch_index = []
debug = []

def change():                                                               #parse device name
    os.system("pactl set-default-sink " + nextsink)                         #switch default device
    for num in switch_index:                                                #switch all program to next device
        debug.append("pactl move-sink-input " + num + " " + nextsink)
        os.system("pactl move-sink-input " + num + " " + nextsink)

for num in sinks:                                                           #parse device name
    if num == str(index):
        index +=1
        sink.append(sinks[sinks.index(num) + 1])

nextsink = sink.index(default_sink)                                         #next device name set to var
if nextsink == len(sink) - 1: nextsink = sink[0]
else : nextsink = sink[sink.index(default_sink) + 1]


for num in range(0,len(sink_input),7):                                      #parse program name
    if sink_input[num] != "-": switch_index.append(sink_input[num])

change()                                                                    #call parse device name
                                                                            #u device switched :)
if False: #set "True" that see debug message                                #debug message
    print('default_sink - ', default_sink)
    print('sinks - ', sink)
    print('nextsink - ', nextsink)
    print('sinkinput - ', sink_input)
    print('sw inde - ', switch_index)
    print(debug)

exit(0)                                                                     #end the script