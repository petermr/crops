import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)

def data_cleaning(input_path, output_path, unwanted_characters=['[]']):
    raw_analyis_output = pd.read_csv(input_path)
    filt = (raw_analyis_output["TPS_match"].isin(unwanted_characters))
    filtered_analysis=raw_analyis_output.loc[~filt]
    filtered_analysis.to_csv(output_path, encoding='utf-8')
    logging.info(f'cleaned output: {output_path}')

data_cleaning('citrus_full_search_result.csv', 'filtered_for_tps_citrus_results_sec.csv')