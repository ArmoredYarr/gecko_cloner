'''
Today's thing is pickle serialization. Partially because I have spent most of the day trying to fix VSCode and
the python language extension for it. 

This is heavily based on the video here: https://www.youtube.com/watch?v=qt15PnF8x-M
Thanks to NeuralNine for creating it. I will be using a lot of his tutorial videos early on here to help
me come up with ideas for future stuff to do in the Thing A Day series of projects.
'''
import pickle
from datetime import datetime

# Some variables to serialize.
some_text = "Text is a thing"
an_int = 42
some_kind_of_float = 9.3

# Need to store these externally.
# for instance if we wanted to store calculation results so we don't have to re-run the calculations.
# This is the non-pickled way and works fine for primitive data types
with open('data.txt', 'w') as f:
    f.write(some_text +'\n')
    f.write(str(an_int) +'\n')
    f.write(str(some_kind_of_float) +'\n')
    f.close()

with open('data.txt', 'r') as f:
    data = f.read().splitlines()
    for line in data:
        print(line)
    f.close()
    

#This gets incredibly complicated as you increase the complexity of the data type. So you can use pickle.
class Gecko:
    #I am using a gecko as an example as that's what's on my mind at the moment and I have spent a lot of time
    # modeling gecko data.
    def __init__(self, name, birthdate, morphs):
        self.name = name
        # A datetime. 
        self.birthdate = datetime.strptime(birthdate, '%d/%m/%y %H:%M:%S')
        self.morphs = morphs

    def stringify_morph_list(self):
        # I just like to have nice neat printing for lists...
        morph_str = ''
        cur_morph = 0
        for morph in self.morphs:
            morph_str += morph 
            cur_morph +=1
            if cur_morph < len(self.morphs):
                morph_str += ', '
        return morph_str

    def __str__(self):
        # 
        return (f'Gecko: {self.name} born {str(self.birthdate)} | Morphs: {self.stringify_morph_list()}')

    def add_morph(self, morph):
        self.morphs.append(morph)

    def change_name(self, name):
        self.name = name

    def serialize(self):
        # Here we can write a method to handle serializing any object of this class.
        with open(self.name + '.pickle_db', 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def deserialize(gecko_name):
        # Here we can just pass the name of a gecko and get back the serialized data if it exists.
        try:
            with open(gecko_name + '.pickle_db', 'rb') as f:
                return pickle.load(f)
        except:
            return "Such a gecko does not exist!"

# This is Vyv. He's my lab ra--... best bud. He has volunteered to be cloned via pickling.
vyv = Gecko("Vyv", '18/09/19 01:55:19', ['Tremper', 'Blizzard', 'Blazing Blizzard'])
vyv.add_morph('Radar')

# The file can be called whatever you want, the extension doesn't matter. WB mode for writing.
with open('vyv.db_pickle', 'wb') as f:
    pickle.dump(vyv, f)
    f.close()

# Now I will clone Vyv from his pickle. Man that sounds weird when I read it back...
with open('vyv.db_pickle', 'rb') as f:
    evil_vyv = pickle.load(f)

#He seems to have picked up some mutations in the cloning process...
evil_vyv.add_morph('Diablo Blanco')
evil_vyv.add_morph('Goatee')

print("Here's Vyv!")
print(str(vyv))
print("===============================")
print("And Vyv again? No wait! That's not Vyv!")
print(str(evil_vyv))
print("===============================")

# Pickle can be pretty handy for saving data if you don't want to use a database.
# Actually, I think you could reliably pickle some data, upload it to object storage, pull it down
# and load the data right back from it if you needed to. That gives me an idea for a future thing a day project.

# Using the serialize and deserialize methods on the class it can be even more readable.
evil_vyv.change_name('Evyv') #Evyv, the evilist Vyv... or is he?
evil_vyv.serialize()

#We can deserialize based on a name here.
even_more_evil_vyv = Gecko.deserialize('Evyv')
even_more_evil_vyv.change_name('Steve') #The evilest of names, so I am told.
even_more_evil_vyv.add_morph("A second goatee taped over the first")

print("I think the cloning machine is broken...")
print(str(even_more_evil_vyv))
print('===============================')

print('Well, at least Vyv\'s still here.')
print(str(vyv))