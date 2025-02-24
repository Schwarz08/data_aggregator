# data_aggregator
## Input:
### All input variables can be found under main.
### data_file_path: file path of csv data to be aggregated
### numeric_dict: dictionary of columns that requires numeric aggregation, it is also possible to downcast the precision
### agg_lvl_col: level of aggregation
### agg_dict: dictionary of columns that require aggregation. values of the dictionary are lists of aggregation function (sum, mean, etc.)
## Output:
### data_aggregator_output.csv: aggregated output data
