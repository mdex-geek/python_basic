# password strength cheaker
password = 'secure3pass'

if len(password)<6:
    strength ='week password'
elif len(password)<=10:
    strength = 'medium password'
elif len(password)<=16:
    strength = 'strong'


print( strength ,'\n' ,len(password) )