import os
import sys
import time


def print_slow(str):
    for char in str:
        time.sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()


print_slow('Hello , This is JARVIS\n');

i=1;
k=1;
y='true';
while (y=='true'):
    if (i>1):
        if(i>=k):
            print_slow('Welcome Once again !!\n');
    print_slow('How can I help you ?\n');
    p = str(input());

    if ('close' in p):
        print_slow('Closing System....\nTHANKYOU SO MUCH');
        y='false';
        os.system('exit')
    else:
        if ('dont' in p):
            print_slow('Sure , I will not Execute...\n');
        else:
            if (('launch' in p) or ('execute' in p) or ('run' in p) or ('open' in p) or ('change' in p)):
                if('chrome' in p):
                    print_slow('Opening Chrome....\n');
                    os.system('chrome');
                elif('notepad' in p):
                    print_slow('Opening Notepad....\n');
                    os.system('notepad');
                elif('vlc' in p):
                    print_slow('Opening VLC Media Player....\n');
                    os.system('vlc');
                elif('media' in p):
                    print_slow('Opening Windows Media Player...\n');
                    os.system('wmplayer');
                else:
                    print_slow('I cant perform this operation, Try something else..\n');
                    k=i;
                    k+=1;
                    continue;

            else:
                print_slow('No such Operation Specified\n');
        print_slow('Do you want to perform another operation ?\n');
        x=input();
        if ('yes' in x):
            i+=1;
            print_slow('Setting up for next operation...\n');
            os.system('cls');
        else:
            y='false';
            print_slow('Closing System...\nTHANKYOU SO MUCH !!');
            os.system('exit');




