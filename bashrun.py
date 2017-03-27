#!/usr/bin/python3
import subprocess
import os

def listOfCommand():
    listOfCommandValue = []
    inputOne = "sudo apt-get remove openjdk*"
    inputTwo = "sudo add-apt-repository ppa:webupd8team/java"
    inputThree = "sudo apt-get update"
    inputFour = "sudo apt-get install oracle-java8-installer"
    inputFive = "java -version"
    inputSix = "javac -version"
    inputSeven = "sudo apt-get install oracle-java8-set-default"
    listOfCommandValue.append(inputOne)
    listOfCommandValue.append(inputTwo)
    listOfCommandValue.append(inputThree)
    listOfCommandValue.append(inputFour)
    listOfCommandValue.append(inputFive)
    listOfCommandValue.append(inputSix)
    listOfCommandValue.append(inputSeven)
    return listOfCommandValue

def removeElement(executCommand):
    # subprocess.call("sudo apt-get remove openjdk*", shell = True)
    subprocess.call(executCommand, shell = True)

def excessMethod():
    listOfCommandValue = listOfCommand()
    for i in listOfCommandValue:
        removeElement(i)

def main():
    excessMethod()

if __name__=="__main__":
    main()
