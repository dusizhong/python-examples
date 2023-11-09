# 导入excel，去重,添加uuid
import pandas as pd

print("正在处理...")
df = pd.read_excel("单位信息20231102.xlsx")
df = df.drop_duplicates(subset=["单位名称"])
df.to_excel("data.xlsx", index=False)
print("处理完成！")