if __name__ == "__main__":
    with open('data/d01.data') as fp:
        data = fp.readlines()

    data = ([ int(x.rstrip()) for x in data])
    
    ans = sum(map(lambda x: (x // 3) - 2, data))

    print(ans)