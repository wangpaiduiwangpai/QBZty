import requests
url = "https://kvideo01.youju.sohu.com/3d20ac9c-4e4f-4fec-bc45-b0150a9b13db2_0_0.mp4?sign=df3ca8b7fe25a530b5ffab51b19102cf&t=1722163300"
res = requests.get(url)
open("性感不出我所料.mp4", 'wb').write(res.content)
