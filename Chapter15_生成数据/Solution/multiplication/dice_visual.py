import plotly.express as px
from die import Die

#创建两个D6
die_1=Die()
die_2=Die()

#掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll()*die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_results=die_1.num_sides*die_2.num_sides
poss_results = range(1,max_results + 1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
title="Results of Multiplying Two D6 Dice 1,000 times"
labels={'x':'Result','y':'Frequency of Result'}
fig=px.bar(x=poss_results,y=frequencies,title=title,labels=labels)

#进一步定制图形
fig.update_layout(xaxis_dtick=1)#将x轴上刻度标记的间距设置为1，给每个条形都加上标签，这样所有条形都有标签了
fig.show()

