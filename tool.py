

import PyPDF2 , os


CRED = '\033[91m'
CEND = '\033[0m'
CREDBG    = '\33[41m'
# Created on 25.02.19 02:06 by tarik

def showLogo():
    print("     *********************************************")
    print("     ************ "+CREDBG + "TARIK'S PDF TOOL" + CEND +"****************")
    print("     ************          ver:0.1****************")
    print("     ************   date: 25.02.19****************")
    print("     *********************************************")

    print("\n ++++Choose an operation: ")
    print(CRED +"#1)"+CEND +" Delete Pages.")
    print(CRED +"#2)"+CEND +" Rotate Pages.")
    print(CRED +"#3)"+CEND +" Extract Pages.")
    print(CRED +"#4)"+CEND +" Add Pages.")
    print(CRED +"#5)"+CEND +" Merge PDF.")
    print("\n++++TYPE AN OPERATION NUMBER : \n")
    print("---->")


def listFiles():
    global pdfFiles
    pdfFiles = []

    for filenames in os.listdir('.'):
        if filenames.endswith(".pdf"):
            pdfFiles.append(filenames)

    pdfFiles.sort(key=str.lower)
    num=0
    for i in pdfFiles:
        num=num+1
        print(str(num) + ")" + i)
    print("\n++++TYPE A FILE NUMBER : \n")
    print("---->")
    global selectedNumber
    selectedNumber=1


def extractPages():
    pdfFileObj= open(pdfFiles[selectedNumber],"rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(CREDBG+ "your file is : " + pdfFiles[selectedNumber] +CEND)
    print("it has " + str(pdfReader.getNumPages())+" pages.")
    print("\n type the page range you want to extract  (ex : 12-12 ,12-15):")

showLogo()
listFiles()
extractPages()
