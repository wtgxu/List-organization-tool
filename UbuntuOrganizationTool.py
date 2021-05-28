import copy
import csv
import os

root_dir = 'original data'
for file in os.listdir(root_dir):

    file_name = root_dir + "/" + file

    #把practice.csv存储到内存 内存里面叫wt
    with open(file_name) as wt:
        #用csv工具的reader（）方法读取内存里的wt创建wt_csv 是row的集合
        wt_csv = csv.reader(wt)

        headers = ['evevt','time','magnitude', 'e_magnitude', 'upperlimit', 'band', 'instrument', 'telescope', 'source','magnitude_sys','mag_source']
        path = "finish"
        # 数据结构
        rows = [

        ]

        for row in wt_csv:
            i = 0
            if row[0] == 'event':
                rows.append(headers)
            else:
                #在这写逻辑
                everow = copy.deepcopy(headers)
                for obj in row:
                    everow[i] = obj
                    i = i+1;
                if everow[4] == 'T':
                    everow[10] = 'limit'
                else:
                    everow[10] = 'Ph'


                if everow[5] == 'u\'':
                    everow[5] = 'u'
                if everow[5] == 'g\'':
                    everow[5] = 'g'
                if everow[5] == 'r\'':
                    everow[5] = 'r'
                if everow[5] == 'i\'':
                    everow[5] = 'i'
                if everow[5] == 'z\'':
                    everow[5] = 'z'
                if everow[5] == 'Ks':
                    everow[5] = 'K'
                if everow[5] == 'C' or everow[5] == 'w' or everow[5] == 'Clear' or everow[5] == 'clear':
                    continue
                if everow[5] == everow[5].lower():
                    everow[9] = 'AB'
                if everow[5][0:1].isupper():
                    everow[9] = 'Vega'
                if everow[7] == 'Swift' and everow[5] == 'U':
                    everow[5] = 'u'
                if everow[7] == 'Swift' and everow[5] == 'M2':
                    everow[5] = 'UVM2'
                if everow[7] == 'Swift' and everow[5] == 'W1':
                    everow[5] = 'UVW1'
                if everow[7] == 'Swift' and everow[5] == 'W2':
                    everow[5] = 'UVW2'
                if everow[6] == 'Swift' and everow[5] == 'U':
                    everow[5] = 'u'
                if everow[6] == 'Swift' and everow[5] == 'M2':
                    everow[5] = 'UVM2'
                if everow[6] == 'Swift' and everow[5] == 'W1':
                    everow[5] = 'UVW1'
                if everow[6] == 'Swift' and everow[5] == 'W2':
                    everow[5] = 'UVW2'
                if everow[5] == 'I1' or everow[5] == 'I2' or everow[5] == 'I3' or everow[5] == 'I4':
                    everow[9] = 'infrared band， need to check the literature'
                if everow[5] == 'orange':
                    everow[9] = 'indetermination'
                if everow[5] == '':
                    everow[9] = 'Manual hidden'
                if everow[9] == 'magnitude_sys':
                    everow[9] = 'Special circumstances need to be reviewed'



                #把每一行添加到rows里面
                rows.append(everow)



        #打开finish\wt.csv文件夹 （w：打开这个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。）
        with open(path+'/'+file,'w',newline='')as wt:
            #使用csv包内的writer（）工具，写入到wt内
            #获取写入的对象
            f_csv = csv.writer(wt)
            #写表头、写一行
            #f_csv.writerow(headers)
            #写入rows对象的内容
            f_csv.writerows(rows)
