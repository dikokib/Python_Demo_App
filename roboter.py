from csv import writer
from fabric.colors import red, green, yellow, blue, magenta, cyan, white
import os

file_path = r'C:\Users\JP17340\Documents\Python Scripts\personal.csv'

def talk():
    print(yellow('こんにちは！私の名前はロボ太です。あなたの名前はなんですか？ \n ▼名前を入力▼'))
    name = input()

    print(yellow(name+'さん！どんな人が好きですか？'))
    appearance = input()

    print(yellow(appearance+'ですか！センスいいですね！また会いましょう！'))

    csv_output(name,appearance)


def csv_output(name_to_csv,appearance_to_csv):
    if os.path.exists(file_path):
        with open('personal.csv', 'a', newline='') as f1:
            print(name_to_csv,appearance_to_csv, file=f1)
        #writer_object1 = writer(f1)
        #writer_object1.writerow([name_to_csv,appearance_to_csv])  
    else:
        with open('personal.csv', 'w') as f2:
            print(name_to_csv,appearance_to_csv, file=f2)
        #writer_object2 = writer(f2)
        #writer_object2.writerow([name_to_csv,appearance_to_csv])  

talk()


