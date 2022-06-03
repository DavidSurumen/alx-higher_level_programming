#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_dir = dir(hidden_4)
    for i in range(len(all_dir)):
        if all_dir[i][:2] != "__":
            print("{}".format(all_dir[i]))
