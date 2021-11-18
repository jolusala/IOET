import datetime as dt

def strToTime(time):
    return dt.time.fromisoformat(time)

def read_data_file(path):
    with open(path, 'r') as f:
        data = f.readlines()
        outputs = dict() 
        for d in data:
            name, periods = d.split('=')
            periods = periods.split(',')
            aport = dict()
            for p in periods:
                day = p[0:2].strip()
                hours = p[2:].split('-')
                aport[day] = (strToTime(hours[0].strip()), strToTime(hours[1].strip()))
            outputs[name] = aport
    return outputs

