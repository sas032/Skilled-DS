class Fruits: pass

banana = Fruits()

banana.color = 'yellow'
banana.value = 30

import pickle

filehandler = open('Fruits.pkl', 'wb')
pickle.dump(banana, filehandler)
filehandler.close()

file=open('Fruits.pkl', 'rb')
obj_file = pickle.load(file)
file.close()

print(obj_file.color, obj_file.value, sep=', ')

