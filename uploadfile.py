from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import streamlit as st
import pandas as pd


global mfat
global uploaded_file
uploaded_file = st.file_uploader("upload FK file", type={"xlsx"})
if uploaded_file is not None:
        #mfa2 = pd.read_excel(uploaded_file, sheet_name=['ff1', 'Sheet1'])
        mfa2 = pd.read_excel(uploaded_file)
        #st.session_state.df922 = pd.read_excel(uploaded_file, sheet_name=['ff1', 'Sheet1'])
        #specific_sheet = mfa2['Sheet1']
        st.write(mfa2)
        


        gb = GridOptionsBuilder.from_dataframe(mfa2)
        gb.configure_selection(
                selection_mode="multiple",
                use_checkbox=True,
                pre_selected_rows=None,  # <-- Set to manually persist checkbox state
            )
        for column in mfa2.columns:
                    gb.configure_column(column, filter=True)

        gridOptions = gb.build()
        mfa = AgGrid(
                mfa2,
                gridOptions=gridOptions,
                update_mode=GridUpdateMode.GRID_CHANGED,
                columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
                #data_return_mode=DataReturnMode.FILTERED   # <-- Gets filtered data, but not filters applied to columns
            )

        if st.button('Check availability'):
            mfa4 =mfa['data']
            fild = pd.DataFrame(mfa['columns_state'])
            #fild2= fild[["colid"]]
            
            #above_35= fild[fild["hide"] == 'False']
            above_35= fild["hide"] 
            above_36= fild["colId"] 
            list_from_df = above_36.values.tolist()
            #list_from_column = df['numbers'].tolist()
            list_from_column = fild["colId"].tolist()
            
            fild["hide"] = fild["hide"].astype(int) 
            fild = fild[fild["hide"]==0 ]
            list_from_df2 = fild["colId"].values.tolist()
            
            mfa5 = mfa4[list_from_column]
            mfa6 = mfa4[list_from_df2]
            mfa7 = pd.DataFrame(mfa6)
            mfa7.set_index(mfa6.iloc[:,0], inplace=True)
            
            
            
            
            
            st.write(mfa6)
            st.write(mfa7)
            first_column_name = mfa7.columns[0]
            #st.header(first_column_name)
            #, index=index
            
#df.iloc[:, column_index] selects a single column by its position.
#df.iloc[:, [column_index1, column_index2]] selects multiple columns by position.
#df.iloc[:, column_index1:column_index3] selects a range of columns by position.
            
            
            st.bar_chart(mfa6)
            st.area_chart(mfa6)
            st.line_chart(mfa6)
            st.pyplot(mfa6.plot.barh(stacked=True).figure)
            st.pyplot(mfa7.plot.bar(stacked=True).figure)
            st.pyplot(mfa7.plot.bar(rot=0).figure)
            #st.pyplot(mfa7.groupby(first_column_name).sum().plot(kind='pie', y='votes_of_each_class'))
            



else:
    
        st.warning("you need to upload a excel file.")




