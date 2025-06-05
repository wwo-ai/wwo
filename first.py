import streamlit as st
import pandas as pd   # 导入Pandas并用pd代替
st.title("🕶学生 小李-数字档案",anchor='xuesheng')
st.header("🔑 基础信息",anchor='学生')
st.text("学生id:NEO-230-51170-117")
st.text("注册时间:1145.1.4 19:19:8|精神状态:✅不是很正常\n当前教室:实训楼301|安全等级:绝密")
st.header("📊技能矩阵")
c1, c2, c3 = st.columns(3)
c1.metric(label="c语言",help='我说这是c语言你盐井虾吗', value="95%", delta="2%")
c2.metric(label="python", value="87%", delta="-1%")
c3.metric(label="java", help='我说这是java你尔多隆吗',value="68%", delta="-10%")
st.subheader("Streamlit课程进度")
my_range = range(1, 101)
numbers = st.select_slider('Streamlit课程进度', options=my_range)
# 定义数据,以便创建数据框
data = {
    '日期':[2023-10-5,2023-10-5,2023-10-12],
    '任务':['学生数字档案','课程管理系统','数据图表展示'],
    '状态':['✅完成','🕒进行中','✖️未完成'],
    '难度':['★★☆☆☆','★☆☆☆☆','★★★☆☆']
}
# 定义数据框所用的索引
index = pd.Series(['01', '02','03'], name=' ')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('🔎任务日志')
st.table(df)
st.subheader('🔐最新代码成果')
python_code='''def  matrix_breach():
while True:
      if detect_vulunerability():
         explit()
         return "ACCESS GRANTED"
         else:
               stealth_evade()
'''
st.code(python_code,language=None)