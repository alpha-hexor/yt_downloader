from parse_output import *

import subprocess as sp
url = "https://www.youtube.com/watch?v=qQIKlRpwSbU"
result =  sp.run(['yt-dlp','-q','-F', url],capture_output=True).stdout.decode()
ids,ext,res,size,formats=parse(result)
