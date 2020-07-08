import json

def addRecord(time, score, user='none'):
    record_dict = {
        'user': user,
        'time': time,
        'score': score
    }
    record_json = json.dumps(record_dict)
    with open('../record.json', 'w') as record_file:
        record_file.write(record_json)

def readRecord():
    with open('../record.json', 'r+') as f:
        cr = json.load(f)
    f.close()
    return cr


if __name__ == '__main__':
    print(readRecord())
