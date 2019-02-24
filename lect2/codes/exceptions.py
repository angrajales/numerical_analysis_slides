if __name__ == "__main__":
    a, b = [2, 0]
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Always execute")
    try:
        f = open("doesnotexists.txt", "r")
    except Exception as e:
        print(e)