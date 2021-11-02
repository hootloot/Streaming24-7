from datetime import datetime, timedelta
import os
import json


f = open('main.json')
data = json.load(f)

current_time = datetime.now()

index = 0
for i in data['overall']:
    times = i['dur' + str(index)]
    current_time += timedelta(hours=times)
    print(i['path' + str(index)] + ' ' + str(current_time))

    
    