import json
from pathlib import Path
path = Path(__file__).resolve().parent/'voting.json'
try:
    with open(path,encoding='utf-8') as file: votes=json.load(file)
except FileNotFoundError:
    votes={}
name = input('Name of the person you are voting for: ').strip()
if name:
    votes[name] = votes.get(name,0)+1
    with open(path,'w',encoding='utf-8') as file:
        json.dump(votes,file,ensure_ascii=False,indent=4)
    print('Votes:',votes[name])
else:
    print('Empty name - no vote recorded')
