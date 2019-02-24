import os
if __name__ == "__main__":
    [a, b] = input().split(" ")
    print([a, b])
    file_input = open("input.txt", "r")
    [a, b] = file_input.read().split(" ")
    file_output = open("output.txt", "w")
    file_output.write(str([a, b]))
    file_input.close()
    file_output.flush(), file_output.close()