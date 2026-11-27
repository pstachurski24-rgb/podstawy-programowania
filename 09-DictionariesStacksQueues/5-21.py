import json
from pathlib import Path
movie = {'title':'Inception','director':'Christopher Nolan','release_year':2010,'genre':'Science fiction','rating':8.8,'watched':True}
path = Path(__file__).resolve().parent/'favourite.json'
with open(path,'w',encoding='utf-8') as file:
    json.dump(movie,file,ensure_ascii=False,indent=4)
print('Saved:',path.name)
