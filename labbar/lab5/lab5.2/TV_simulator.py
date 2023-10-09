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

def select_TV_menu(tv_list):
    print("Välj TV:")
    for i in range(len(tv_list)):
        print(str(i + 1) + ". " + tv_list[i].tv_name)
    print(str(len(tv_list) + 1) + ". Avbryt")
    try:
        new_TV = int(input("val: ")) - 1
        selected_TV = tv_list[new_TV]
    except:
        if(new_TV == len(tv_list)):
            print("programmet avslutas\n")
            return None
        else:
            print("\nfel, försök igen:")
            selected_TV = select_TV_menu(tv_list)
    return selected_TV

def change_channel(selected_TV):
    new_channel = int(input("Ange kanalnummer: "))
    if(not selected_TV.change_channel(new_channel)):
        print("Kanal för den här tvn ska vara mellan 1 och " + str(selected_TV.max_channel) + ", försök igen")
        change_channel(selected_TV)

def increase_volume(selected_TV):
    selected_TV.increase_volume()

def decrease_volume(selected_TV):
    selected_TV.decrease_volume()


def main():
    
    tv_obj_list = read_file("allatv.txt")
    while True:
        tv = select_TV_menu(tv_obj_list)
        if(tv == None):
            break
        options = [change_channel, increase_volume, decrease_volume]
        while True:
            print("\n1. Byt kanal")
            print("2. Höj volymen")
            print("3. Sänk volymen")
            print("4. Avbryt")
            try:
                choice = int(input("val: "))
                if(choice == 4):
                    break
                options[choice - 1](tv)
            except:
                print("\nfel, försök igen\n")

            print(tv)

if __name__ == "__main__":
    main()
