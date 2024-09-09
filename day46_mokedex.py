import os, time

mokedex = {}

def createMokedex():
  while True:
    print("\nMokeBeast Generator")
    name = input("name: ")
    type = input("type: ")
    hp = input("hp: ")
    mp = input("mp: ")
    mokedex[name] = {"type": type, "hp": hp, "mp": mp}
    print("Added to mokedex")
    time.sleep(1)
    os.system("clear")
    prettyPrint()
    time.sleep(3)
    os.system("clear")


def prettyPrint():
    for key, value in mokedex.items():
      print(key,end=" > ")
      for subkey, subvalue in value.items():
        print(f" {subkey}:{subvalue} ", end="|")

createMokedex()

# There is a better implementaion
# def prettyPrint():
#  print("Your Mokedex\n")
# for key, value in mokedex.items():
#   print(f"""{key:<12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""") 
# In the above coode mokedex is unwrapped into key and subvalues of the dictionary value is called by value["type"], value["hp"]


