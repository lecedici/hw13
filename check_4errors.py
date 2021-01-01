def find_error():
    count = 0
    with open("C:\\users\\xxdima\\Desktop\\Course DevOps\\log.txt") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            for word in words:
                if word == "ERROR":
                    return True
    return False