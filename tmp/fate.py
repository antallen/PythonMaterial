import csv
import random

class fate:

    __messages = []
    __moneys = []

    def choise(self):
        with open("fste.csv","r",encoding='utf-8') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                self.__messages.append(row['命運訊息'])
                self.__moneys.append(row['金額'])

        index = random.randrange(0,len(self.__messages))
        return([self.__messages[index],self.__moneys[index]])

if __name__ == "__main__":
    myfate = fate()
    print(myfate.choise())