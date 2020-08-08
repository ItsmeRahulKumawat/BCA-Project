
def only_val(*args):
    print(type(args))
    if len(args) == 3:
        print("Hi Mr "+args[0]+" "+args[1]+" "+args[2])
    else:
        print("Hi Mr "+args[0]+" "+args[1])

lis = ['Rahul','Jagdish','Kumawat']
# only_val('Rahul','Jagdish','Kumawat')
only_val(*lis)

def key_val(**kwargs):
    print(type(kwargs))
    for key,val in kwargs.items():
        print(key, val)

fav_subs = {"Rahul" : 100, "Akash" : 101, "Sudhir" : 102, "Dipesh" : 103}
key_val(**fav_subs)

def master(noraml, *args, **kwargs):
    print(noraml)
    for i in args:
        print(i)
    for key,val in kwargs.items():
        print(key, val)

master("normal", *lis, **fav_subs)