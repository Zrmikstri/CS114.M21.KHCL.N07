import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
f = open('output.txt', 'r')
lst = f.read().split('Objects:')
f.close()

df = pd.DataFrame(columns=['Frame', 'X', 'Y', 'Width', 'Height'])
for i in range(1, len(lst)):
    count = 0
    for _, j in enumerate(lst[i].split('\n')):
        if j.startswith('bien'):
            temp = " ".join(j.split())
            x = temp[temp.find('left_x') + 8: temp.find('top_y') - 1]
            y = temp[temp.find('top_y') + 7: temp.find('width') - 1]
            w = temp[temp.find('width') + 7: temp.find('height') - 1]
            h = temp[temp.find('height') + 8: temp.find(')')]
            count += 1
            df1 = pd.DataFrame([[i, x, y, w, h]], columns=['Frame', 'X', 'Y', 'Width', 'Height'])
            df = df.append(df1, ignore_index=True)

    if count == 0:
        # print('NO OBJECTS')
        df2 = pd.DataFrame([[i, np.nan, np.nan, np.nan, np.nan]], columns=['Frame', 'X', 'Y', 'Width', 'Height'])
        df = df.append(df2, ignore_index=True)
        continue

df.to_csv('output.csv', index=False)
print(df)
