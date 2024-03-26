import streamlit as st
import pandas as pd

import streamlit as st

# Increase the maximum upload size to 100 MB




def main():
    st.title("CSV FILE  EXPLORER")
    
    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read CSV data
        df = pd.read_csv(uploaded_file,encoding='latin-1')
        
        # Display the uploaded data
        st.write("Uploaded data:")
        st.write(df)
        
        # Get unique rows in the DataFrame
        unique_rows = df.drop_duplicates().index.tolist()
        
        # Select a row to explore
        selected_row = st.selectbox("Select a row to explore", unique_rows)
        
        # Display information for the selected row
        st.write("Selected row:")
        st.write(df.iloc[selected_row])

if __name__ == "__main__":
    main()

### pipreqs  CSVreader.py(for requirement.txt
