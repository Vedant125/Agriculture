import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns
df = pd.read_csv('datafile (2).csv')
st.header('Analysis of Agriculture Data from 2006-2011')


st.set_option('deprecation.showPyplotGlobalUse', False)
col = df.columns[1:]
crop = st.sidebar.selectbox("Select Crop ",df['Crop             '])
crop_list = ['Total Foodgrains', 'Rice', 'Wheat', 'Jowar', 'Bajra', 'Maize',
       'Ragi', 'Small millets', 'Barley', 'Coarse Cereals', 'Cereals',
       'Gram', 'Arhar', 'Other Pulses', 'Total Pulses',
       'Total Non-Food grains ', 'Total Oilseeds', 'Groundnut', 'Sesamum',
       'Rapeseed &Mustard', 'Linseed', 'Castor seed', 'Safflower',
       'Niger seed', 'Sunflower', 'Soyabean', 'Nine Oilseeds', 'Coconut',
       'Cotton seed', 'Total Fibers', 'Cotton(lint)', 'Jute', 'Mesta',
       'Jute & Mesta', 'Sannhamp ', 'Tea ', 'Coffee ', 'Rubber ',
       'Total Spices', 'Black pepper', 'Dry chilies ', 'Dry ginger ',
       'Turmeric ', 'Arecanut  ', 'Cardamom ', 'Coriander', 'Garlic  ',
       'Total Fruits & Vegetables', 'Potato', 'Tapioca', 'Sweet potato  ',
       'Onion', 'Banana  ', 'Sugarcane', 'Tobacco']
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black',
          'orange', 'purple', 'brown', 'gray', 'olive']
if crop :

    type = st.radio('' , ['Production' , 'Area' , 'Yield' ,'Area vs Yield'])
    if type == 'Production':
        plt.plot(df.columns[1:6],df.iloc[crop_list.index(crop)].values[1:6] , color = random.choice(colors) , linestyle = 'dashed')
        plt.xticks(rotation=45)
        plt.grid()
        plt.xlabel('Year')
        plt.ylabel('Production (quintal / hectare)')
        plt.title(crop)
        st.pyplot()
    elif type == 'Area':
        plt.plot(df.columns[6:11], df.iloc[crop_list.index(crop)].values[6:11], color=random.choice(colors),
                 linestyle='dashed')
        plt.xticks(rotation=45)
        plt.grid()
        plt.xlabel('Year')
        plt.ylabel('Area(hectare)')
        plt.title(crop)
        st.pyplot()

    elif type == 'Yield':
        plt.plot(df.columns[11:], df.iloc[crop_list.index(crop)].values[11:], color=random.choice(colors),
                 linestyle='dashed')
        plt.xticks(rotation=45)
        plt.grid()
        plt.xlabel('Year')
        plt.ylabel('Yield (quintal / hectare)')
        plt.title(crop)
        st.pyplot()

    elif type == 'Area vs Yield':
        sns.barplot(x=df.iloc[crop_list.index(crop)].values[6:11], y=df.iloc[crop_list.index(crop)].values[11:], palette=colors , hue=df.columns[6:11])
        plt.xticks(rotation=45)
        plt.grid()
        plt.xlabel('Area(hectare)')
        plt.ylabel('Yield (quintal / hectare)')
        plt.title(crop)
        # plt.legend(df.columns[6:11])
        st.pyplot()


# st.line_chart(df , x= 'Production 2006-07', y = 'Production 2007-08' )
