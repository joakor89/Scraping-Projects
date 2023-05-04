def my_gen():
    for i in range(0, 201):
        if i % 2 == 0:
            yield i  

my_first_gen = my_gen()

for i in range(100):
    print(next(my_first_gen))
