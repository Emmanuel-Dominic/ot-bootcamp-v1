from functools import wraps


#################################################
#                 STEP ONE                      #
#        With a normal function call            #
#################################################
def get_name():
    print("Bootcamp")


get_name()


#################################################
#                STEP TWO                       #
#        With First-Class Functions             #
#################################################
def my_function(func):
    return func()


my_function(get_name)


#################################################
#                STEP THREE                     #
#        With First Decorator Functions         #
#################################################
def is_anonymous(func):
    def wrapper():
        print("Hi,")
        func()
        print("You're welcome!")
    return wrapper


# @is_anonymous
def get_user():
    print("IsAdmin")


get_user = is_anonymous(get_user)
get_user()


#################################################
#                STEP FOUR                      #
# Second Decorator Function with args and kwags #
#################################################
def is_superuser(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("IsSuperAdmin!")
    return wrapper


@is_superuser
def check_superuser(name):
    if name == "superuser":
        print("You're a super user.")
    else:
        print("You're an anonymous user.")


check_superuser("admin")


#################################################
#                STEP FIVE                      #
# Decorator Functions with @wraps decorator     #
#################################################
def is_admin(func):
    print("Line 74", func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("IsAdmin!")
        return result
    return wrapper


def is_user(func):
    print("Line 85", func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("IsAnonymous!")
        return result
    return wrapper


@is_user
@is_admin
def check_user(name):
    if name == "admin":
        print("You're an admin.")
    else:
        print("You're an anonymous user.")
    return name


check_user("admin")
