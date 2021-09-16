import json
import pickle
with open ('file2.json', 'r') as f:
    res= json.load(f)

with open('file.pickle', 'wb') as f:
    pickle.dump(res, f)
f.close

with open('file.pickle', 'rb') as f:
    res=pickle.load(f)
print(res)