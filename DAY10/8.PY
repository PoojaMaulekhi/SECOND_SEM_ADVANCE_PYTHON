import matplotlib.pyplot as plt
import pandas as pd

# 
revenue=[765,789,435,908,546,7098]
ex=[0,0,1.0,0.1,1]
item=['veg','non-veg','veg']
plt.pie(revenue,label=item,wedgeprops={'edgecolor':'black'},
    explode=ex,
    shadow=True,)