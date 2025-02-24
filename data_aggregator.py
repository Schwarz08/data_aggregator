import pandas as pd
import time as timer

'''
Created by Jan Kyle Lewis T. Nolasco
'''

def aggregate_data(data, agg_lvl_col, agg_dict):
    #set up new dataframe for output
    data_agg=pd.DataFrame(data=data[agg_lvl_col].unique(), columns=[agg_lvl_col])

    #loop through columns to aggregate
    for col in agg_dict:
        #loop through aggfuncs
        for agg_func in agg_dict[col]:

            # special process for "count", "nunique", "list" aggregation, these need a new column to work
            if agg_func == "count":
                new_col = col + " [count]"
                data[new_col] = data[col]
                agg_calc = pd.pivot_table(data, values=new_col, index=agg_lvl_col,  aggfunc=agg_func)
            elif agg_func == "nunique":
                new_col = col + " [nunique]"
                data[new_col] = data[col]
                agg_calc = pd.pivot_table(data, values=new_col, index=agg_lvl_col, aggfunc=agg_func)
            elif agg_func == "list":
                new_col = col + " [list]"
                data[new_col] = data[col]
                agg_calc = pd.pivot_table(data.dropna(subset=[col]), values=new_col, index=agg_lvl_col,
                                      aggfunc=pd.unique)
            else:
                agg_calc = pd.pivot_table(data, values=col, index=agg_lvl_col,
                                               aggfunc=agg_func)
                agg_calc.rename(columns={col: col+" ["+agg_func+"]"}, inplace=True)

            #add calculated aggregation to output dataframe
            data_agg = data_agg.join(agg_calc, on=agg_lvl_col)

    return data_agg

def convert_to_numeric(data, numeric_dic):
    #loop through col_list to convert to numeric
    for col in numeric_dic:
        precision = numeric_dic[col]
        #print(col, precision)
        #check if there is a downcast precision specified
        if precision is None:
            data[col] = pd.to_numeric(data[col], errors='coerce')

        else:
            data[col] = pd.to_numeric(data[col], errors='coerce', downcast=precision)

    return data

def main():
    data_file_path = "sample_data.csv"
    data = pd.read_csv(data_file_path)

    numeric_dic = {
        "4G Payload (GB)": "float",
        "DL PRB Usage(%)": "float",
        "Average Users": "float"
    }

    #ensure all columns with aggregation that involves arithmetics are numeric, downcast to a precision if specified
    data = convert_to_numeric(data, numeric_dic)

    agg_dict={
        "4G Payload (GB)": ["sum"],
        "DL PRB Usage(%)": ["mean"],
        "Average Users": ["sum"],
        "eNodeB Name": ["list", "count", "nunique"],
        "Cell Name": ["list", "count", "nunique"]
    }

    data_agg = aggregate_data(data.copy(deep=True), "eNodeB Name", agg_dict)
    data_agg.to_csv("data_aggregator_output.csv", index=False)

if __name__ == '__main__':
    start=timer.time()
    main()
    end=timer.time()
    total_time=(end-start)/60
    print(f"Elapsed Time: {total_time} mins", )