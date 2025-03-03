# data_aggregator
## Input:
### All input variables can be found under main.
* data_file_path: File path of csv data to be aggregated
* numeric_dict: Dictionary of columns that requires numeric aggregation, it is also possible to downcast the precision
* agg_lvl_col: Level of aggregation
* agg_dict: Dictionary of columns that require aggregation. Values of the dictionary are lists of aggregation function (sum, mean, etc.)
## Output:
Aggregated output data will be saved as data_aggregator_output.
