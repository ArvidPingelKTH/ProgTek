from TV import TV

#converts a text file of TV object parameters into a list of TVs
def read_file(file_name):
    tv_list = []
    try:
        file = open(file_name, "r")
        for line in file:
            line = line.strip()
            line = line.split(",")
            tv = TV(line[0], int(line[4]), int(line[1]), int(line[3]), int(line[2]))
            tv_list.append(tv)
        file.close()
    except FileNotFoundError:
        print("File not found")
    return tv_list

#saves every tv from a list to a text file
def write_file(tv_list, file_name):
    try:
        file = open(file_name, "w")
        for tv in tv_list:
            file.write(tv.str_for_file())
        file.close()
    except FileNotFoundError:
        print("File not found")

def main():

    tv1 = TV()
    print(tv1)
    tvlista = read_file("allatv.txt")  
    for tv in tvlista: print(tv)

    tvlista[0].change_channel(330)
    for tv in tvlista: print(tv)

    write_file(tvlista, "allatv.txt")  
    tvlista = read_file("allatv.txt")  
    for tv in tvlista: print(tv) 

if __name__ == "__main__":
    main()
