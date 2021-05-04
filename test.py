from time import sleep

def textWrite(text, time):
    for i in text:
        print(i,sep='', end='')
        sleep(time)

print("This is a test because I wanna write something in python lmao")
sleep(5)
print("...oh, you still here?")
print("well, since you're still here", sep='', end='')
textWrite("...", 1)
