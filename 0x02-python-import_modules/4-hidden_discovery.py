#!/user/bin/python3
if __name__ == "__main__":
    import hidden_4

    for name indir(hidden_4):
        if name[:2] != "__":
            print("{}".format(name))

