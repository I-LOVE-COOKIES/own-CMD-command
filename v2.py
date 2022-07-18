
import os

dest = "C:\\Windows\\System32\\"
final = []
liste =[]


def install2():
    final = []
    liste =[]

    print("""

    **********Created by JuzGcheat**************
    *                                          *
    *             Instructions:                *
    *                                          *
    *  1. Create a txt file, with shortcuts    *
    *     (for Examples open Example.txt)      *
    *  2. Chause a Mode                        *
    *------------------------------------------*
    *  1  (Start Shortcut Creator)             *
    *  2  (Remove Shortcuts)                   *
    *  3              Quit                     * 
    *                                          *
    ********************************************


         """)
    v = input("----------->  ")
    v = int(v)
    if v == 1 or 2 or 3:
        if v == 1:
            exe()
        elif v == 2:
            remove()
        elif v == 3:
            quit

    
def Creator(name,url):
    name = dest + name
    url = "@echo off \n" + url
    g = open(name,"w")
    g.write(url)
    g.close()


    

def exe():
    Scr = input("Shortcuts File (dragn drop this file) --->   ")
    with open(Scr, "r") as tf:
        lines = tf.read().split("\n")
        for line in lines:
            liste.append(line)
        tf.close()
        
    for element in liste:
        final = []
        element = element.split(" = ")
        final.append(element)
        for command in final: 
            name = str(command[0])
            url = str(command[1])
            print("name:  ", name, "   url =  ", url)
            name = name + ".bat"
           
            command = []
            Creator(name,url)
    print("you can use your shortcuts now \n (Installation Done (-: )")
    install2()



            
def remove():
    Scr = input("Shortcuts File (dragn drop this file) --->   ")
    with open(Scr, "r") as tf:
        lines = tf.read().split("\n")
        for line in lines:
            liste.append(line)
    tf.close()
    for element in liste:
        final = []
        element = element.split(" = ")
        final.append(element)
        for command in final: 
            name = str(command[0])
            name = dest + name
            name = name + ".bat"
            print("Delte:  ", name)
            if os.path.exists(name):
                os.remove(name)
            
    print("Shortcuts Sucessfull Removed")
    install2()
    
    
    
install2()