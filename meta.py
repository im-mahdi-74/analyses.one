import csv

import matplotlib.pyplot as plt


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

