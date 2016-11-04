import os
import time
hostname = 'google.com'


def isInternetUp():
    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        print('internet is up!')
        return True

    else:
        print('internet is down')
        return False


def beep():
    for i in range(10):
        print('\a') #plays a beep


def main():
    while not isInternetUp():
        time.sleep(10)
    beep()


main()
