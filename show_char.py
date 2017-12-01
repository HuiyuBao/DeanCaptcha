def show_char(array, use_special_char=True):
    for i in range(12):
        for k in range(4):
            for j in range(10):
                if array[k][i*10 + j] == 0:
                        print("  ", end='')
                elif array[k][i*10 + j] == 1:
                    if use_special_char==True:
                        print("\u2588\u2588", end='')
                        # Unicode character FULL BLOCK
                    else:
                        print("##", end='')
            print("   ", end='')
        print("")
    print(" ")
