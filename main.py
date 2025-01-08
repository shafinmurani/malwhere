import numpy as np
import streamlit as st
import pandas as pd
from malware_scanner import MalwareScanner

# Streamlit app

# Streamlit app main function
def main():
    st.title("MalWHERE?")

    # File upload widget
    uploaded_files = st.file_uploader("Upload Files", type=["zip", "exe", "pdf", "txt","png","jpg","doc","doc"], accept_multiple_files=True)

    if uploaded_files:        
            # Get scan results
            malwareScanner = MalwareScanner()
            scan_results = malwareScanner.scan_files(uploaded_files)
            print(scan_results)
            # Prepare the results for the table
            data = []
            for file_name, (status, signature,hash) in scan_results.items():
                data.append({
                    'File Name': file_name,
                    'Status': status,
                    'Signature': signature,
                    "SHA256": hash
                })
            
            # Convert the data to a pandas DataFrame for table display
            df = pd.DataFrame(data)
            
            # Display the results in a table
            st.dataframe(df)
    


if __name__ == "__main__":
    main()
