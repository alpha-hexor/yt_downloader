import re

def parse(result):
    #sanitize result
    r=result.replace("audio only","audio_only").replace("video only","video_only")
    x=r.split("\n")[2:]
    p=[ re.findall(r'(\d+|\w+)\s+(\w+)\s+(audio_only|\d+x\d+)\s+(\d+|)\s+(\d+|)\s+\|\s+(\d+\.\d+?[KMG]i?B|).*\|\s+(audio_only|\w+|\w+\.\w+|\w+\.\w+\.\w+|\w+\.\w+\.\w+\.\w+)\s+(\d+k|)\s+(\w+|video_only|\w+\.\w+|\w+\.\w+\.\w+|\w+\.\w+\.\w+\.\w+).*',i) for i in x]
    p=p[:-1]
    ids = [i[0][0]for i in p]
    ext = [i[0][1]for i in p]
    res = [i[0][2]for i in p]
    size = [i[0][5]for i in p]
    formats = [i[0][-1]for i in p]
    
    return ids,ext,res,size,formats
    