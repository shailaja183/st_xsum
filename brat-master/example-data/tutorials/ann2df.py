import pandas as pd
import glob

def ann2df(path):
    all_files = glob.glob(path + "/*.ann")
    print(all_files)
    print(len(all_files))

    for file in all_files:
        df = []
        df = pd.read_csv(file, sep='\t', engine='python', header=None)
        df1 = df[1].str.split(expand=True)
        df_new = pd.concat([df[0], df1, df[2]],axis=1)
        df_new.reset_index()
        print(df_new)
        df_new.to_csv(str(file).strip('./').strip('.ann')+'.csv',mode='w+',index=False,header=False)
        print("---")

ann2df(r'./')