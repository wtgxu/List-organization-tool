# List-organization-tool
使用python批量处理超新星观测数据csv文档

本code仅进行了下列任务，未在下列的步骤需要手动完成

1.  在列表尾增加了  mag_source  和  magnitude_sys  两列
2.  如果  upperlimit  列是F,或者空白， mag_source  列 填Ph 
3.  如果  upperlimit  列是T，              mag_source  列填limit
4.  将  band  列 u' 替换为 u ，g' 替换为 g ，r' 替换为 r ，i' 替换为 i ，z' 替换为 z ，Ks 替换为 K 
5.  如果 band 列出现 C 或者 w 将整行删除
6.  如果 band 列是小写字母，magnitude_sys 列填 ab
7.  如果 band 列首字母是大写的，在magnitude_sys列填 Vega
8   如果 telescop 或者 instrument 是 Swift ，将band列的 U 替换为 u、M2 替换为 UVM2、W1 替换为 UVW1、W2 替换为 UVW2
9.  如果 band 列是I1，I2，I3，I4，这4种之一  在 magnitude_sys 列 标注出“infrared band， need to check the literature”（红外波段，需要查文献确定星等系统）
10.  如果 band 列为 orange ，在 magnitude_sys 列 标注出“indetermination”（不确定）交由甘文沛师兄处理
11.  如果 band 列为 空白 ，在 magnitude_sys 列 标注出 “Manual hidden”（手动隐藏，我不会写这个的code）
12. 如果 band 列 上述情况都不是，那么在 magnitude_sys 列 标注出 “Special circumstances need to be reviewed”（特殊情况 需要查看）

使用方法
1.  将甘文沛师兄的批量下载code下载下来的csv文件，粘贴到original data（原始数据）文件夹
2.  运行程序（wins系统运行UbuntuOrganizationTool.py   Ubuntu系统运行UbuntuOrganizationTool.py）
3.  结果输出在finish（完成）文件夹


2021\5\22
2021\5\20 第二版（在第八条添加了，如果instrument列是Swift，也要修改波段）