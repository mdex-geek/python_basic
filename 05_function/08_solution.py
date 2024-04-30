def fun(**krargs):
    for key,values in krargs.items():
        print(f"{key}:{values}")

fun(power='fly',name="iron man")
fun(power='toffay',name="opentor",locals= 'delhi')