import csv
import pandas as pd
import matplotlib.pyplot as plt




def convertone(): # convert one used csv python func oler and worked andes for read dtial histoey
    ri = 2000
    b = 0
    with open(f'C:/Users/delta2794900/Documents/kon.csv') as f:
        fal = csv.reader(f)
        s = ri
        y = [s]  # initialize y with initial value of s
        for i in fal:
            a = i[0]
            for a in i:
                prof = a[84:95]
                b = b + 1
                cleaned_data = [d.split(";")[0] for d in prof.split(";")]
                if len(cleaned_data) > 1:
                    sod = cleaned_data[1]
                    if sod != '':
                        sod = float(sod)
                        s = ri + sod
                        ri = s
                        y.append(s)
        plt.plot(range(len(y)), y)

        plt.xlabel('Iteration')
        plt.ylabel('Value of s')
        plt.title('Line Chart of s')
        plt.show()


def converttwo():
    workbalance = []
    df = pd.read_csv('C:/Users/delta2794900/Documents/kon.csv' , delimiter= ';')
    
    df['Time'] = pd.to_datetime(df['Time'], format='%Y.%m.%d %H:%M:%S')
    df = df.sort_values(by='Time')
    startbalance = 10000
    try:
        for i in df.Profit :
            startbalance = startbalance + i
            workbalance.append(startbalance)
            
        
        plt.step( df['Time'] ,workbalance)
        plt.show()
        

    except:
        ('erore')
        

converttwo()
