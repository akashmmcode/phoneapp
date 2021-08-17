# d = {"name":"Ricky"}


# def get(d,key):
#     try:
#         return d[key]
#     except KeyError:
#         return None

# print(get(d,"nscac"))

while True:
    try:
        num = int(input("please enter a number"))

    except ValueError:
        print("did not enter a valid input")

    else:
        print("u entered a proper number")
        break

print("END GAME")
    # finally:
    #     print("runs no matter what")
