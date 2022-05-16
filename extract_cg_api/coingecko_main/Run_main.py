from undo_pagination import *
from column_to_df_setup import *
import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy import create_engine



def dict_col_to_df(categ_data=0):
    scp_data = {
        'name':scp_name,
        'symbol':scp_symbol,
        'current_price':scp_current_price,
        '$market_cap':scp_market_cap,
        'market_cap_rank':scp_market_cap_rank,
        'all_time_high':scp_all_time_high
    }

    meme_data = {
        'name':meme_name,
        'symbol':meme_symbol,
        'current_price':meme_current_price,
        '$market_cap':meme_market_cap,
        'market_cap_rank':meme_market_cap_rank,
        'all_time_high':meme_all_time_high
    }

    gamefi_data = {
        'name':gamefi_name,
        'symbol':gamefi_symbol,
        'current_price':gamefi_current_price,
        '$market_cap':gamefi_market_cap,
        'market_cap_rank':gamefi_market_cap_rank,
        'all_time_high':gamefi_all_time_high
    }
    
    if categ_data == 1:
        global scp_df
        scp_df = pd.DataFrame(scp_data)
        
        
    elif categ_data == 2:
        global meme_df
        meme_df = pd.DataFrame(meme_data)
        
        
    elif categ_data == 3:
        global gamefi_df
        gamefi_df = pd.DataFrame(gamefi_data)
        
    
    else:
        raise ValueError('You must enter an integer that corresponds to the supported categories (1-3)')



def write_to_RDS():
    # Create engine object
    # Parameters <database>://<username>:<password>@<host>:<port>/<DBname>
    engine = create_engine()
    # Creates a live connection to our data
    connection = engine.connect()
    # Send dataframes to database
    scp_df.to_sql('smart_contract_platforms', connection, if_exists='replace', chunksize= 100, index = False)
    meme_df.to_sql('meme_tokens', connection, if_exists='replace', chunksize = 100, index = False)
    gamefi_df.to_sql('gaming_tokens', connection, if_exists='replace', chunksize = 100, index = False)
    # Close connection to database
    connection.close()

def main():
        exec_undo_pagination = undo_pagination()
        scp_columns = json_to_col(1)
        meme_columns = json_to_col(2)
        gaming_columns = json_to_col(3)
        create_scp_df = dict_col_to_df(1)
        create_meme_df = dict_col_to_df(2)
        create_game_df = dict_col_to_df(3)
        exec_write_RDS = write_to_RDS()

if __name__ == "__main__":
        main()