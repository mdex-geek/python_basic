def even_geneartor(n):
    for i in range(2,n+1,2):
        yield i 
        # yeild -> it return the value but it store function  in a memory and store the state also

for num in even_geneartor(10):
    print(num)
