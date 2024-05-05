def debug(func):
    def wrapper(*args,**kwargs):
       args_value = ', '.join(str(arg) for arg in args)
       kwargs_value=', '.join(f"{k}:{v}"  for k,v in kwargs.items())
       print(f"calling:{func.__name__} with args:{args_value} and kwargs {kwargs_value}")
       return func(*args,**kwargs)
        # we return the definition of wrapper 
    return wrapper

@debug
def greet(name , greeting = 'namaste'):
    print(greeting , name)

greet('chai',greeting='hanji')


