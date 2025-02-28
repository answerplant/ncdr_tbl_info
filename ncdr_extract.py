# ARP, Answer Digital, 2024-07-12

"""
Load NCDR database information file https://github.com/nhsengland/NCDR-reference-library/blob/v0.7.9/data/csvs/1/vw_Export_Standard_DB_Structure.csv
Read lines matching pattern, split them by '¬'
Map them to dataframe with column headers specified in the first line of the file.

"DatabaseId"¬"Database"¬"SchemaID"¬"Schema"¬"Table/ViewID"¬"Table/View"¬"Table or View"¬"Name"¬"Description"¬"Date_Range"¬"Data_Start"¬"Data_End"¬"Link"¬"Link Type"¬"Data_Sharing"¬"Data_Source"¬"DatSchem"
"1"¬"NHSE_111"¬"0"¬""¬"0"¬""¬"N/A"¬"NHS 111 data"¬"


"""

import pandas as pd

DATA = 'data\\vw_Export_Standard_DB_Structure.csv'

data_lists = []

with open(DATA, "r") as f:
    #translation = {"\"": None}
    for line in f:
        #print(line)
        if line.startswith("\""):
            #tbl_info = line.translate(translation)
            tbl_info = line.split("¬")
            tbl_info =  [t.strip('\"') for t in tbl_info]
            data_lists.append(tbl_info)

print(data_lists[0])

ncdr_df = pd.DataFrame(data_lists[1:], columns = ['DatabaseId', 'Database', 'SchemaID', 'Schema', 'Table/ViewID', 'Table/View', 'Table or View', 'Name', 'Description', 'Date_Range', 'Data_Start', 'Data_End', 'Link', 'Link Type', 'Data_Sharing', 'Data_Source', 'DatSchem']) 
#print(ncdr_df.info())
ncdr_df.head()

db_list = ncdr_df['Database'].unique()
print(db_list)
#ncdr_df.to_csv("NCDR_DB_Summary.csv")
