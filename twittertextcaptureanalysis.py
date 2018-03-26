import string
import operator
import sys


def mosttweetedusers():
    input_file = input("Enter the input file path: ")
    input_file_path = input_file + '.txt'

    with open(input_file_path, encoding="latin-1") as File1:
        hello1 = File1.readlines()
    a = {}
    for dat in hello1:

        file2= dat.split()
        if file2[0] in a:
            a[file2[0]] += 1
        else:
            a[file2[0]] = 1
    a = sorted(a.items(), key=operator.itemgetter(1), reverse=True)

    outputFile = open(r'C:\Users\divya1\Desktop\SSDI\Most.txt', 'w', encoding="utf-8")
    outputFile.write("The top 10users who have tweeted the for the entire timeline: \n",)
    for i in range(0,10):
        outputFile.write("The user " + a[i][0] + " tweeted " + str(a[i][1]) + " times" + "\n")

    outputFile.close


mosttweetedusers()


def mostUsersPerHour():
    input_file = input("Enter the input file path: ")
    input_file_path = input_file + '.txt'

    with open(input_file_path, encoding="latin-1") as File1:
        hello2 = File1.readlines()

    b = {}
    for dat in hello2:
        fileTemp = dat.split()
        fileTemp2 = fileTemp[1].split(":")
        twitterTemp = fileTemp[0] + " " + fileTemp2[1]
        if twitterTemp in b:
            b[twitterTemp] += 1
        else:
            b[twitterTemp] = 1
    b = sorted(b.items(), key=operator.itemgetter(1), reverse=True)

    b2 = {}
    totalNumPostsInFile = 0
    for dat in b:
        totalNumPostsInFile += 1
        if (dat[0].split()[1]) in b2:
            b2[dat[0].split()[1]] += 1
        else:
            b2[dat[0].split()[1]] = 1
    b2 = sorted(b2.items(), key=operator.itemgetter(1))

    totalEntriesToPrint = 10 * len(b2)
    outputFile = open(r'C:\Users\divya1\Desktop\SSDI\MostTweetedperHour.txt', 'w',
                      encoding='utf-8')

    for x in range(0, len(b2)):

        Search = 10

        for dat in b:
            if Search == 0:
                break
            if dat[0].split()[1] == b2[x][0]:
                outputFile.write("Username: " + dat[0].split()[0] + "\n Hour: " + b2[x][0] + "\n")

                Search -= 1
    outputFile.close


mostUsersPerHour()


def maxFollowers():
    input_file = input("Enter the input file path: ")
    input_file_path = input_file + '.txt'

    with open(input_file_path, encoding="latin-1") as File1:
        hello1 = File1.readlines()

    c = {}
    for dat in hello1:
        fileTemp = dat.split()
        if fileTemp[0] not in c:
            c[fileTemp[0]] = int(fileTemp[-2])

    c = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
    outputFile = open(r'C:\Users\divya1\Desktop\SSDI\Maximumfollowers.txt', 'w',
                      encoding="utf-8")
    outputFile.write("The top 10 users who has the maximum followers: " + "\n\n")

    for i in range(0, 10):
        outputFile.write(str(i + 1) + ". Username: " + c[i][0] + " -> Number of Followers: " + str(c[i][1]) + "\n\n")
    outputFile.close


maxFollowers()


def maxRetweet():
    input_file = input("Enter the input file path: ")
    input_file_path = input_file + '.txt'

    with open(input_file_path, encoding="latin-1") as File1:
        hello1 = File1.readlines()

    d = {}
    for dat in hello1:

        fileTemp = dat.split()
        y = len(fileTemp) - 2
        tweet = "\""
        for x in range(4, y):
            tweet += fileTemp[x] + " "
        tweet += " ::::;:::: " + fileTemp[0]

        if tweet not in d:
            d[tweet] = int(fileTemp[-1])

    outputFile = open(r'C:\Users\divya1\Desktop\SSDI\Maximumretweets.txt', 'w', encoding="utf-8")
    d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    outputFile.write("The top 10 tweets that has the max no of retweets : " + "\n\n")

    for x in range(0, 10):
        outputFile.write(str(x + 1) + ". Username: " + d[x][0].split()[-1] + "\n Tweet: " +
                         d[x][0].split("::::;::::")[0] + "\n No of retweets: " + str(d[x][1]) + "\n\n")
    outputFile.close


maxRetweet()

##commited new