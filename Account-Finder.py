

#  Python--3.9
#  https;//github.com/derradjib76f
#  https://github.com/derradj.i


import requests
import sys
#import webbrowser
import os
import time

def text_Run(s):
        for words in s + '\n':
                sys.stdout.write(words)
                sys.stdout.flush()
                time.sleep(10. / 200)

#os.system("rm -rf Accounts-Finder/SRC/*")

print ('')

first_name = str ( input ("      \33[95mFirst Name of Target:\033[0m ") )
time.sleep(0.35)
print ('')
last_name = str ( input ("       \33[95mLast Name of Target:\033[0m ") )

def Options():

    def Facebook():

        os.system("clear")
        print ('''\33[5m
███████╗░█████╗░░█████╗░███████╗██████╗░░█████╗░░█████╗░██╗░░██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
█████╗░░███████║██║░░╚═╝█████╗░░██████╦╝██║░░██║██║░░██║█████═╝░
██╔══╝░░██╔══██║██║░░██╗██╔══╝░░██╔══██╗██║░░██║██║░░██║██╔═██╗░
██║░░░░░██║░░██║╚█████╔╝███████╗██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝
\033[0m
''')
        print ("")
#       os.system('cd SRC')

        Link_demo = "https://www.facebook.com/"f"{first_name}.{last_name}"
        response_demo = requests.get(Link_demo)
        if response_demo.status_code == 200:
            #os.system('cd SRC')
            print (f"{Link_demo} : \033[0;32mFound\033[0m")
            #webbrowser.open(Link_demo)
            file = open("Valid_Facebook-Demo.txt", "a")
            file.write(f"Valid : {Link_demo}\n")
            print ("")
        else:
            print ('\033[0;31mSorry There are NoThing ON Demo ... \033[0;35m:/\033[0m')
        Account = 0
        for Account in range(10000):
#           os.system('cd SRC')
            Account = Account + 1
            Link = "https://www.facebook.com/"f"{first_name}.{last_name}.{Account}"
            response = requests.get(Link)
            if response.status_code == 200:
                print (f"\33[42m{Link}\033[0m : \33[4mFound\033[0m")
                #webbrowser.open(Link)
                file = open("Valid-Facebook.txt", "a")
                file.write(f"Valid : {Link}\n")
            elif response.status_code == 404:
                print (f"\33[91m{Link}\033[0m : \033[0;31mNot Found\033[0m")
            else:
                print ('\033[0;31mSorry There are A Problem Here \033[0;35m:/\033[0m')
                text_Run("[\033[0;31m-\033[0m] Sorry There Are Other Error Try Again ...")
                time.sleep(1.5)
                Options()

    def Instagram():
        os.system('clear')
        print ('''\33[5m
██╗███╗░░██╗░██████╗████████╗░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░██╗░██████╔╝███████║██╔████╔██║
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
\033[0m
''')
        Link = "https://www.instagram.com/"f"{first_name}.{last_name}"
        response = requests.get(Link)
        if response.status_code == 200:
#           os.system('cd SRC')
            print (f"\033[0;32m{Link} : \33[91mFound\033[0m")
            #webbrowser.open(Link)
            #os.system("cd SRC")
            file = open("Valid_Instagram.txt", "a")
            file.write(f"Valid : {Link}\n")
        elif response.status_code == 404:
            print (f"\33[41m{Link}\033[0m : \033[0;31mNot Found\033[0m")
        else:
            print ('\33[101mSorry There are A Problem Here\33[104m:/\033[0m')
            text_Run("\033[0;31m[-]\033[0m Sorry There Are Other Error Try Again ...")
            time.sleep(1.5)
            Options()

    os.system("clear")
    
    print ('''\33[5m
  BY. This Tool You Can Found The Accounts Facebook of Your Friends in A Simple Way
                                   # By --- B76F #
                               Rate of Seccess is : 1/2\033[0m


               [1]   Facebook                           [2]   Instagram
''')

    time.sleep(1.58)
    option = int ( input ("                                      \033[36mOption :\033[0m ") )
    if option == 1:
        Facebook()
    elif option == 2:
        Instagram()
    else:
        print ("\33[91mError , Try Again !")
        text_Run ("Clear ...")
        time.sleep(1.5)
        os.system("clear")
        Options()

def __Main__():
    Options()
#   os.system('cd SH && bash 01001.sh')

__Main__()
