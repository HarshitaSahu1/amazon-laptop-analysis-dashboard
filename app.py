import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "123":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()  # This refreshes the app to show dashboard
        else:
            st.error("Invalid username or password")
   


def all_analysis():

    final_dataset_products = pd.read_csv("finalized_data_csvv.csv")
    st.sidebar.subheader('🚪 Logout')
    if st.sidebar.button('Logout'):
        st.session_state.clear()
        st.rerun()
    
    #final_dataset_products = pd.read_csv(r'C:\Users\Harshita Sahu\OneDrive\Documents\Web_scrapping_data\finalized_data_csvv.csv')
    final_dataset_products = final_dataset_products.drop(columns = ['Unnamed: 0'])
    st.title("Product Data Analysis")
    
    Titles = final_dataset_products['Titles'].unique()
    Series = final_dataset_products['Series'].unique()
    Processor_brands = final_dataset_products['Processor Brand'].unique()
    Processor_types = final_dataset_products['Processor Type'].unique()
    Price_cat = final_dataset_products['Prices_Category'].unique()


    #selected_laptop = st.sidebar.selectbox('select a laptop',Titles)
    selected_laptop = st.sidebar.multiselect('select multiple laptops',Titles,key = 'Laptop')
    selected_series = st.sidebar.multiselect('select multiple series',Series,key = 'Series')
    selected_Processor_Brand = st.sidebar.multiselect('select multiple processor brands',Processor_brands,key = 'Processor_Brand')
    selected_Price_category = st.sidebar.multiselect('select multiple price categories',Price_cat,key = 'Prices_Category')

    filtered = final_dataset_products.copy()
    if selected_laptop:
        filtered = filtered[filtered['Titles'].isin(selected_laptop)]
    if selected_series:
        filtered = filtered[filtered['Series'].isin(selected_series)]
    if selected_Processor_Brand:
        filtered = filtered[filtered['Processor Brand'].isin(selected_Processor_Brand)]
    if selected_Price_category:
        filtered = filtered[filtered['Prices_Category'].isin(selected_Price_category)]


    tab1,tab2,tab3,tab4,tab5 = st.tabs(['📊 Data overvies & analysis','⚖️ Comparative Analysis','👥⭐ Rating Analysis','🔗 URL Analysis','📌Wrap Up'])

    with tab1:
        st.subheader('📊Final Dataset Preview')
        st.dataframe(final_dataset_products.head())

        

        if filtered['Titles'].notna().any():
             Most_sold_Laptop = filtered.groupby('Titles')['Qty_sold_last_month_'].sum().sort_values(ascending = False).head(1).reset_index()['Titles'][0]
        else: 
            Most_sold_Laptop = 'N/A'

        if filtered['Series'].notna().any():
            Most_sold_Series = filtered.groupby('Series')['Qty_sold_last_month_'].sum().sort_values(ascending = False).head(1).reset_index()['Series'][0]
        else:
            Most_sold_Series = 'N/A'

        if filtered['Item model number'].notna().any():
            Most_sold_model_number = filtered.groupby('Item model number')['Qty_sold_last_month_'].sum().sort_values(ascending = False).head(1).reset_index()['Item model number'][0]
        else:
            Most_sold_model_number = 'N/A'
        
        if filtered['Prices_Category'].notna().any():
            Top1_Price_Categories = filtered.groupby('Prices_Category')['Qty_sold_last_month_'].sum().sort_values(ascending = False).head(1).reset_index()['Prices_Category'][0]
        else:
            Top1_Price_Categories = 'N/A'

        if filtered['Processor Brand'].notna().any():
            Most_sold_Processor_Brand = filtered.groupby('Processor Brand')['Qty_sold_last_month_'].sum().sort_values(ascending = False).head(1).reset_index()['Processor Brand'][0]
        else:
            Most_sold_Processor_Brand = 'N/A'

        if filtered['Processor Type'].notna().any():
            Top1_Processor_Type = filtered.groupby('Processor Type')['Qty_sold_last_month_'].sum().sort_values(ascending = False).head(1).reset_index()['Processor Type'][0]
        else:
            Top1_Processor_Type = 'N/A'


        kpis = {'Most_sold_Laptop': Most_sold_Laptop, 'Most_sold_Series': Most_sold_Series, 'Most_sold_model_number': Most_sold_model_number, 'Top1_Price_Categories': Top1_Price_Categories, 'Most_sold_Processor_Brand': Most_sold_Processor_Brand, 'Top1_Processor_Type': Top1_Processor_Type}
        st.markdown('---')
        st.subheader('🎯 Key Performance Indicators (KPIs)')
        Kpis = pd.DataFrame(list(kpis.items()),columns=['KPIS','VALUES'])
        st.table(Kpis)


        Top_5_series = filtered.groupby('Series')['Qty_sold_last_month_'].sum().sort_values(ascending = False).head(5)
        Top_5_series = Top_5_series.reset_index()



        st.subheader('Visualizations')
        #st.markdown("<hr style =' border:2px solid #E6D98B;'>",unsafe_allow_html = True)

        col1,spacer,col2 = st.columns([1,0.05,1])

        with col1:
            def most_sold_series_products(Top_5_series):
                st.subheader('📊 Top 5 Sold Series Distribution')
                fig,axes = plt.subplots(constrained_layout = True)
                #axes.set_title('Sold_Series_Distributions',fontsize = 15)
                axes.pie(x = 'Qty_sold_last_month_',labels = 'Series',data =Top_5_series,autopct = '%1.1f%%',startangle=90,textprops={'fontsize':14})
                return fig
 
            st.pyplot(most_sold_series_products(Top_5_series),use_container_width = True)

            st.markdown(" ")
            with st.expander("What this chart means?"):
                st.markdown("""<div style  = "background-color:#FFF9C4 ; padding :10xp;">\
                "Distribution of series based on quantity sold in last month.\
            it helps us to findout which series is most sold in top 5 series". </div>""",unsafe_allow_html = True
            )
        with spacer:
           st.markdown(
            "<div style='border-left:2px solid #aaa; height:450px;'></div>",
            unsafe_allow_html=True
            )

        with col2:
            price_qty_sold = filtered[['Prices','Qty_sold_last_month_']].corr()
            def relationship_btw_prices_qty_sold(price_qty_sold) :
                st.subheader('🔗Relationship Btw Prices & Qty_sold_last_month')
                fig,axes = plt.subplots(constrained_layout = True)
                #axes.set_title('Relationship Btw Prices & Qty_sold_last_month',fontsize = 15)
                sns.heatmap(price_qty_sold,annot = True,ax = axes)
                return fig
            st.pyplot(relationship_btw_prices_qty_sold(price_qty_sold))

            with st.expander("What this chart means?"):
                st.markdown("""<div style = "background-color:#FFF9C4;padding:10px;">\
                            "This heatmap shows a correlation between Prices and Quantity sold last month.\
                            a negative low correlation indicates that prices does not have a strong impact on qty sold",</div>""",unsafe_allow_html = True)

        st.markdown('---')


        col3,spacer,col4 = st.columns([1,0.05,1])

        with col3:
            def price_and_qty_sold(filtered):
               # st.subheader("Prices\n V/S Qty_sold Trend")
                st.markdown("""<div style = 'font-weight:bold; font-size:29px;'>
                            💰📈Prices<br> V/S Qty_sold Trend </div>""",unsafe_allow_html = True
                            )
                fig,axes = plt.subplots(figsize = (8,6.5))
                sns.scatterplot(data = filtered ,x = 'Prices',y = 'Qty_sold_last_month_',ax  = axes,s = 60)
                sns.regplot(data = filtered ,x = 'Prices',y = 'Qty_sold_last_month_',scatter = False,color = 'red',ax = axes)
                #plt.title('Prices V/S Qty_sold trend')
                plt.xticks(rotation = 90)
                return fig
            st.pyplot(price_and_qty_sold(filtered))

            with st.expander("What this chart means?"):
                st.markdown("""<div style ="background-color :#FFF9C4 ; padding :10px;">\
                            "The scatter plot showns the prices and qty sold last month\
                             .The line indicates how is the relationship btw them.\"</div>""",unsafe_allow_html = True)
        with spacer:
            st.markdown("<div style = 'border-left:2px solid #aaa;height:450px'></div>",unsafe_allow_html = True)

        with col4:
            price_cat_dist = filtered.groupby('Prices_Category')['Qty_sold_last_month_'].mean()
            price_cat_dist = price_cat_dist.reset_index()
            def price_distributions(price_cat_dist):
                st.subheader('📊Price_Category_Dist Based Qty_Sold_Last_Month')
                fig,axes = plt.subplots(constrained_layout = True)
                #axes.set_title('Price Distribution Based on Qty_Sold_Last_Month',fontsize = 15)
                axp = sns.barplot(x = price_cat_dist['Prices_Category'],y = price_cat_dist['Qty_sold_last_month_'] ,ax = axes,color = 'hotpink')
                for p in axes.patches:
                    axes.text(x = p.get_x()+p.get_width()/2,y = p.get_height()+0.5 , s = int(p.get_height()),ha = 'center')
                return fig

            st.pyplot(price_distributions(price_cat_dist),use_container_width = True)
            with st.expander("What this chart means?"):
                st.markdown("""<div style = "background-color :#FFF9C4 ; padding :10px;">\
                            "This Barplot shows which type of price category are being sold the most in last month
                            which helps in finding the customer buying pattern".</div>""",unsafe_allow_html = True)
                
        st.markdown('---')

        Top_5_product = filtered.groupby('Titles')['Qty_sold_last_month_'].sum().sort_values(ascending = False).head(5).reset_index()
        def sold_products(Top_5_product):
            st.subheader('🏆Top 5 Sold Products')
            fig,axes = plt.subplots(figsize = (8,6))
            #axes.figure(figsize = (20,20))
            #axes.set_title('Most Sold Laptops',fontsize = 15)
            axes.barh(y = Top_5_product['Titles'],width = Top_5_product['Qty_sold_last_month_'],color = 'purple',alpha = 0.5)
            for p in axes.patches:
                axes.text(p.get_width(),p.get_y()+p.get_height()/2,int(p.get_width()))
            return fig
        st.pyplot(sold_products(Top_5_product))

        with st.expander('What this chart means?'):
            st.markdown('<div style = "background-color :#FFF9C4;padding :10px;">\
            "This bar shows the top 5 laptops which are sold most in last month.\"</div>',unsafe_allow_html = True)

    with tab2:
        Titles = final_dataset_products['Titles'].unique()
        Series = final_dataset_products['Series'].unique()
        Processor_brands = final_dataset_products['Processor Brand'].unique()
        Processor_types = final_dataset_products['Processor Type'].unique()
        Price_cat = final_dataset_products['Prices_Category'].unique()


        #selected_laptop = st.sidebar.selectbox('select a laptop',Titles)

        selected_laptops_for_comparative_analysis = st.multiselect('select_laptops_for_comparative_analysis',Titles,key = 'compare laptops')
        if len(selected_laptops_for_comparative_analysis) == 0 or len(selected_laptops_for_comparative_analysis) ==1:
            st.warning('Please select at least 2 laptops to make comparative analysis')
        
    #selected_series = st.sidebar.selectbox('select a series',Series)
    #selected_processor_brand = st.sidebar.selectbox('select a processor brand',Processor_brands)
    #selected_processor_type = st.sidebar.selectbox('select a processor type',Processor_types)
    #selected_price_cat = st.sidebar.selectbox('select a price category',Price_cat)
        else:
            st.subheader('⚖️ Filtered Data preview for Comparative Analysis')
            filtered_data_products = final_dataset_products[
            (final_dataset_products['Titles'].isin(selected_laptops_for_comparative_analysis))]
            #(final_dataset_products['Series'] == selected_series)&
            #(final_dataset_products['Processor Brand'] == selected_processor_brand)&     
            #(final_dataset_products['Processor Type'] == selected_processor_type)&
            #(final_dataset_products['Prices_Category'] == selected_price_cat)]

            st.write(filtered_data_products)


            st.markdown('<div style = "font-weight:bold;font-size:25px;"> 🆚📊 Comparative Analysis Visualizations</div>',unsafe_allow_html = True)
            
            st.write('----------------------------------------------------------------',)


            st.markdown("""<div style = 'font-weight:bold;font-size:20px;text-align :center'> 💲📊 Prices Category Distribution Among Selected Laptops</div>""",unsafe_allow_html = True)
            st.markdown(" ")
            #prices = filtered_data_products.groupby('Titles')['Prices_Category'].unique().reset_index().explode('Prices_Category')
            prices = filtered_data_products.groupby(['Prices_Category','Titles']).size().reset_index(name = 'counts')
            fig,axes = plt.subplots(figsize = (8,6))
            sns.scatterplot(data = prices, x = 'Prices_Category',y = 'Titles',size = 'counts',s = 120,ax = axes,color = 'green')
            axes.set_xticklabels(axes.get_xticklabels(),rotation = 90)
            axes.set_xlabel('Prices Category',fontdict = {'fontsize' :15})
            axes.set_ylabel('Titles',fontdict = {'fontsize' :15})
            
            #for i ,value in enumerate(prices['counts']):
            #   plt.text(i,value,int(value),ha = 'center',va = 'top')
            st.pyplot(fig)

            with st.expander("What this chart means?"):
                st.markdown("""<div style = 'background-color:#FFF9C4;padding:10px;border:1px solid #FFD54F;'>\
                            "This scatter plot shows the distribution of price categories among selected laptops.\
                            The size of the points helps us to understand and compare which laptop is sold in which price category".</div>""",unsafe_allow_html = True)



            st.markdown("----------------------------")
            
    
            st.markdown('<div style = "font-weight:bold;font-size :20px;text-align:center">⭐ Average Ratings Among Selected Laptops</div>',unsafe_allow_html = True)
            ratings_dist = filtered_data_products.groupby('Titles')['Ratings'].mean().reset_index()

            fig,axes = plt.subplots(figsize = (8,6))
            axes.barh(ratings_dist['Titles'],ratings_dist['Ratings'],color = 'orange')
            for p in axes.patches:
                axes.text(p.get_width(),p.get_y()+p.get_height()/2,int(p.get_width()))

            axes.set_xlabel('Average Ratings',fontdict = {'fontsize' :15})
            axes.set_ylabel('Titles',fontdict = {'fontsize' :15})
            st.pyplot(fig)

            with st.expander('What this chart means?'):
                st.markdown("""<div style = "background-color:#FFF9C4;padding:10px;border:1px solid #FFD54F;">\
                            "This bar chart shows the average rating btw laptops which helps in analysing which laptop is more liked by customers".
                            </div>""",unsafe_allow_html = True)


            st.markdown('----------------------------')
            st.markdown(" ")
            st.markdown('<div style = "font-weight:bold;font-size:20px;text-align:center">📦 Quantity Sold Last Month Comparison Among Selected Laptops</div>',unsafe_allow_html = True)
            plt.title('Quantity Sold Last Month Comparison') 
            fig,axes = plt.subplots(figsize = (8,6))
            #axes.set_title('Qty_sold_last_month_compared',fontsize = 25)
            sns.barplot(y = 'Titles' , x = 'Qty_sold_last_month_',data = filtered_data_products,ax = axes,color = 'purple',alpha = 0.5)
            for p in axes.patches:
                axes.text(x = p.get_width()+0.5, y = p.get_y()+p.get_height()/2,s = int(p.get_width()),va = 'center')
            axes.set_xticklabels(axes.get_xticklabels(),rotation = 90)
            axes.set_xlabel('Qty_sold_last_month_',fontdict = {'fontsize' :15})
            axes.set_ylabel('Titles',fontdict = {'fontsize' :15})

            st.pyplot(fig)

            with st.expander('What this chart means?'):
                st.markdown("""<div style = "background-color :#FFF9C4;padding:10px;border:1px solid #FFD54F;">\
                            "This chart shows the which laptop is sold the most in last month among selected laptops
                            it helps in understanding the sales performance of each laptop".<div>""",unsafe_allow_html = True )

            st.markdown('----------------------------')
            st.markdown(" ")
            st.markdown('<div style = "font-weight:bold;font-size:20px;text-align:center">💲 Prices Comparison Among Selected Laptops</div>',unsafe_allow_html = True)
            prices_dist =filtered_data_products.groupby('Titles')['Prices'].mean().reset_index()
            fig,axes = plt.subplots(figsize = (8,6))
            axes.set_title('Prices Compared',fontsize = 25)
            y =  range(len(prices_dist['Titles']))
            x = prices_dist['Prices']
            plt.scatter(x,y,marker = 'o',s = 100,color = 'green')
            #x = range(len(filtered_data_products['Prices']))
            for i ,value in enumerate(x):
                plt.text(value +0.5 , i,int(value),ha = 'center',va = 'top')
            plt.yticks(y,prices_dist['Titles']) 
        
        # plt.yticks(rotation = 90)
            st.pyplot(fig)

            with st.expander('What this chart means'):
                st.markdown(""" <div style = "background-color:#FFF9C4;padding:10px;border:1px solid #FFD54F;">\
                            "This charts shows different laptops and there prices \
                            It helps in customer behaviour in terms of prices". </div>""",unsafe_allow_html = True)
                
            st.markdown('--------------------')
            st.markdown(" ")

            st.markdown('<div style= "font-weight:bold;font-size:20px;text-align:center">\
                        🏷️📉Discount Percentage Comparison</div>',unsafe_allow_html = True)
    
            fig,axes = plt.subplots(figsize = (8,6))
            #axes.set_title('Discount Percnt Comparision',fontsize = 25)
            discount = filtered_data_products.groupby('Titles')['Discount_prct'].mean().reset_index()
            sns.barplot(y = discount['Titles'],x = discount['Discount_prct'],ax = axes,color = 'hotpink')
            for p in axes.patches:
                axes.text(p.get_width(),p.get_y()+p.get_height()/2,int(p.get_width()))
            st.pyplot(fig)

            with st.expander('What this chart explains?'):
                st.markdown("""<div style = "background-color :#FFF9C4; padding:2px; border: 1px solid #FFD54F;">\
                            "This chart shows which laptop is giving more discount \
                            This helps in making an analysis that how customer are behaving in terms of more discount".</div>""",unsafe_allow_html = True)

     

    with tab3:
        st.subheader('👥⭐ Rating Analysis')

        st.markdown("-----------------------")
        st.markdown(" ")

        st.markdown("""<div style = "font-weight:bold; font-size :21px ; text-align:center;"
                    >⭐📈 Relationship Between Ratings, Rating Counts & Qty Sold (by Processor Type)</div>""",unsafe_allow_html = True)
        
        
        multiselect_laptops = st.multiselect('select_laptops_to_compare',Titles)
        
        k = final_dataset_products[final_dataset_products['Titles'].isin(multiselect_laptops)]
        if len(k)>0:
            k = k
        else :
            k = final_dataset_products
        st.write(k.head(5))
     

        #key = 'compare laptops')
    
        ratings_processor_type_dist =k.groupby('Processor Type').agg(avg_rating = ('Ratings','mean'),rating_counts = ('Ratings_counts','sum'),qty_sold_most = ('Qty_sold_last_month_','sum')).sort_values(by = ['rating_counts','avg_rating','qty_sold_most'],ascending = False).reset_index()
        def processor_brand_analysis(ratings_processor_type_dist):
            x = np.arange(len(ratings_processor_type_dist))
            width = 0.35
            fig,axes = plt.subplots(1,2,figsize = (10,5))
            axes =axes.flatten()
            
            axes[0].bar(x = x-width/2,height = ratings_processor_type_dist['qty_sold_most'],width = width,data = ratings_processor_type_dist,label = 'Avg_Qty_Sold')
            
        # for i,value in enumerate(ratings_processor_type_dist['qty_sold_most']):
            #    if value>0:
            #       axes[0].text(i-width/2,value+0.5,value,ha = 'center')
            
            
            axes[0].bar(x = x+width/2 ,height = ratings_processor_type_dist['rating_counts'],data = ratings_processor_type_dist,width = width,label = 'Rating_counts',alpha = 0.5)
        # for i,value in enumerate(ratings_processor_type_dist['rating_counts']):
            #    axes[0].text(i+width/2,value+0.5,value,ha = 'center')
            axes[0].set_title('Avg_Qty_sold & Ratings_counts')
            axes[0].set_xticks(x)
            axes[0].set_xticklabels(ratings_processor_type_dist['Processor Type'],rotation = 90)
            axes[0].set_xlabel('Processor Type')
            axes[0].legend()
            
            axes[1].plot(x,ratings_processor_type_dist['avg_rating'],color = 'r' , marker = 'o',linewidth = 3,zorder = 5,label = 'Avg_Ratings')
            for i,value in enumerate(ratings_processor_type_dist['avg_rating']):
                if value>0:
                    axes[1].text(i,value+0.0005,round(value,1),ha = 'center',va = 'bottom')
            axes[1].set_xticks(x)
            axes[1].set_xticklabels(ratings_processor_type_dist['Processor Type'],rotation = 90)
            axes[1].set_title('Average_Ratings')
            axes[1].set_xlabel('Processor Type')
            axes[1].legend()
            return fig 
        st.pyplot(processor_brand_analysis(ratings_processor_type_dist))

        with st.expander('What this chart means?'):
            st.markdown("""<div style = 'background-color :#FFF9C4; padding:2px;border:1px solid #FFD54F';>
                        "This chart represents how the in the ratings of a processor type along with rating_counts and Qty_sold_last_month\
                            This will helps in analyzing the true processor type which is high in ratings as well as in Qty_sold". </div>""",unsafe_allow_html = True)
        


        #st.subheader('Rating Analysis')

        st.markdown("-----------------------")
        st.markdown(" ")

        st.markdown("""<div style = "font-weight:bold; font-size :21px ; text-align:center;"
                    >💻⚙️📈  Relationship Between Ratings, Rating Counts & Qty Sold (by Processor Brand)</div>""",unsafe_allow_html = True)
        ratings_processor_brand = k.groupby('Processor Brand').agg(avg_ratings = ('Ratings','mean'),Rating_counts = ('Ratings_counts','sum'),avg_qty_sold = ('Qty_sold_last_month_','sum'))
        ratings_processor_brand = ratings_processor_brand.reset_index()
        def processor_brand_analysis(ratings_processor_brand):
            x = np.arange(len(ratings_processor_brand))
            width = 0.35
            fig,axes = plt.subplots(1,2,figsize = (10,5))
            axes =axes.flatten()
            
            axes[0].bar(x = x-width/2,height = ratings_processor_brand['avg_qty_sold'],width = width,label = 'Avg_Qty_Sold')
            
            for i,value in enumerate(ratings_processor_brand['avg_qty_sold']):
                axes[0].text(i-width/2,value+0.0005,value,ha = 'center')
            
            
            axes[0].bar(x = x+width/2 ,height = ratings_processor_brand['Rating_counts'],width = width,label = 'Rating_counts',alpha = 0.5)
            for i,value in enumerate(ratings_processor_brand['Rating_counts']):
                axes[0].text(i+width/2,value+0.0005,value,ha = 'center')
            axes[0].set_title('Avg_Qty_sold & Ratings_counts')
            axes[0].set_xticks(x)
            axes[0].set_xticklabels(ratings_processor_brand['Processor Brand'])
            axes[0].set_xlabel('Processor Brand')
            axes[0].legend()
            
            axes[1].plot(x,ratings_processor_brand['avg_ratings'],color = 'r' , marker = 'o',linewidth = 3,zorder = 5,label = 'Avg_ratings')
            for i,value in enumerate(ratings_processor_brand['avg_ratings']):
                axes[1].text(i,value+0.05,round(value,2))
            axes[1].set_xticks(x)
            axes[1].set_xticklabels(ratings_processor_brand['Processor Brand'])
            axes[1].set_title('Average_Ratings')
            axes[1].set_xlabel('Processor Brand')
            axes[1].legend()
            return fig
        st.pyplot(processor_brand_analysis(ratings_processor_brand))

        with st.expander('What this chart means?'):
            st.markdown("""<div style = 'background-color :#FFF9C4; padding:2px;border:1px solid #FFD54F';>
                        "This chart represents how the in the ratings of a processor brand along with rating_counts and Qty_sold_last_month\
                            This will helps in analyzing the true processor brand which is high in ratings as well as in Qty_sold". </div>""",unsafe_allow_html = True)
        


        st.markdown("-----------------------")
        st.markdown(" ")

        st.markdown("""<div style = "font-weight:bold; font-size :21px ; text-align:center;"
                    >🔗📊 Relationship Between Ratings, Rating Counts & Qty Sold (by Laptop series)</div>""",unsafe_allow_html = True)
        series_ratings = k.groupby('Series').agg(Avg_ratings = ('Ratings','mean'),Total_Ratings_count = ('Ratings_counts','sum'),Total_Qty_sold = ('Qty_sold_last_month_','sum')).sort_values(by = ['Total_Qty_sold','Total_Ratings_count','Avg_ratings'],ascending = False)
        series_ratings = series_ratings.reset_index()
        def Series_analysis(series_ratings):
            x = np.arange(len(series_ratings))
            width = 0.50
            fig,axes = plt.subplots(1,2,figsize = (10,5))
            axes = axes.flatten()
            
            axes[0].bar(x-width/2,series_ratings['Total_Qty_sold'],width = width,label = 'Total_Qty_Sold')
            axes[0].set_xticks(x)
            axes[0].set_xticklabels(series_ratings['Series'])
            axes[0].tick_params('x',rotation = 90)
            axes[0].set_xlabel('Series')
            
            
            axes[0].bar(x+width/2,series_ratings['Total_Ratings_count'],alpha = 0.3,color = 'hotpink',width = width,label = 'Total_Ratings_Count')
            axes[0].set_title('Total_Qty_Sold & Total_Ratings_Count')
            axes[0].legend()
            
            
            axes[1].plot(x+width/2,series_ratings['Avg_ratings'],marker = 'x',label = 'Avg_ratings',color = 'r')
            for i,value in enumerate(series_ratings['Avg_ratings']):
                if pd.notna(value):
                    axes[1].text(i-width/2,value+0.0005,round(value,2))
            axes[1].set_title('Average Ratings Based on Series')
            axes[1].legend()
            axes[1].set_xticks(x)
            axes[1].set_xticklabels(series_ratings['Series'])
            axes[1].set_xlabel('Series')
            axes[1].tick_params('x',rotation = 90)
            return fig
        st.pyplot(Series_analysis(series_ratings))

        with st.expander('What this chart means?'):
            st.markdown("""<div style = 'background-color :#FFF9C4; padding:2px;border:1px solid #FFD54F';>
                        "This chart represents how the in the ratings of a Series along with rating_counts and Qty_sold_last_month\
                            This will helps in analyzing the true Series which is high in ratings as well as in Qty_sold". </div>""",unsafe_allow_html = True)
        
    
    with tab4:
        st.subheader('🔗 URL Analysis')
        
        input_url = st.text_input('Enter the products urls')
        filtered = final_dataset_products.copy()
    

        if input_url:
            filtered = filtered[filtered['urls'] == input_url]
            st.write(filtered)

            st.markdown(f'### Product :{filtered["Titles"].values[0]}')

            col1,spacer,col2 = st.columns([1,0.05,1])

            col1.metric("Price",filtered["Prices"])
            with spacer:
                st.markdown("<div style= 'border-left:2px solid #aaa; height:90px;'></div>",
                            unsafe_allow_html = True)
          
            col2.metric("Qty_sold_last_month_",filtered["Qty_sold_last_month_"])
            

            col3,spacer,col4 = st.columns([1,0.05,1])
            col3.metric("Ratings",filtered["Ratings"])

            with spacer:
                st.markdown('<div style = "border-left:2px solid #aaa; height :90px;"></div>',unsafe_allow_html = True)
            col4.metric("Ratings_counts",filtered["Ratings_counts"])

            st.markdown('---------------')
            
            st.subheader('Product Features')
            features = filtered[['Titles','Series','Item model number','Processor Brand','Processor Type','Prices_Category']]
            st.table(features.T)
        
        else:
            st.warning('Please enter a valid url to analyze')

    with tab5:
        st.subheader('Final Takeaways')
        st.markdown('### 🔍 Key Analysis Insights')
        st.markdown("""
        - Numerical factors alone are **not the primary drivers of laptop sales**.
        - Quantity sold shows **very low correlation** with:
            - Price
            - Discount percentage
            - Customer ratings
        - This indicates that **laptop features and specifications** play a more significant role in purchase decisions.
        - Customers are increasingly **willing to pay higher prices** for better features and performance.
        - A noticeable shift is observed from **low-price category laptops to higher-price category laptops**.
        """)

        st.markdown('### ⚠️ Data Considerations & Limitations')
        st.markdown("""
        - The dataset is **limited in scope and time period**.
        - Sales data is available for **only one month**, restricting trend analysis.
        - Predictive or forecasting analysis cannot be reliably performed.
        - Results should be interpreted as **indicative insights**, not absolute conclusions.
        """)


            
if st.session_state.logged_in:
    all_analysis()
