from undo_pagination import *

# SCP Columns
scp_name = []
scp_symbol = []
scp_current_price = []
scp_market_cap = []
scp_market_cap_rank = []
scp_all_time_high = []

# Meme Columns
meme_name = []
meme_symbol = []
meme_current_price = []
meme_market_cap = []
meme_market_cap_rank = []
meme_all_time_high = []

# Gamefi Columns
gamefi_name = []
gamefi_symbol = []
gamefi_current_price = []
gamefi_market_cap = []
gamefi_market_cap_rank = []
gamefi_all_time_high = []

def json_to_col(cg_category=0):
    
    if cg_category == 1: 

        for coin in scp_json:
            
            scp_name.append(coin['name'])
            scp_symbol.append(coin['symbol'])
            scp_current_price.append(coin['current_price'])
            scp_market_cap.append(coin['market_cap'])
            scp_market_cap_rank.append(coin['market_cap_rank'])
            scp_all_time_high.append(coin['ath'])
            
    elif cg_category == 2:
    
        for coin in meme_json:
            
            meme_name.append(coin['name'])
            meme_symbol.append(coin['symbol'])
            meme_current_price.append(coin['current_price'])
            meme_market_cap.append(coin['market_cap'])
            meme_market_cap_rank.append(coin['market_cap_rank'])
            meme_all_time_high.append(coin['ath'])

    elif cg_category == 3:
        
        for coin in gamefi_json:
            
            gamefi_name.append(coin['name'])
            gamefi_symbol.append(coin['symbol'])
            gamefi_current_price.append(coin['current_price'])
            gamefi_market_cap.append(coin['market_cap'])
            gamefi_market_cap_rank.append(coin['market_cap_rank'])
            gamefi_all_time_high.append(coin['ath'])

    else:
        raise ValueError('You must enter an integer that corresponds to the supported categories (1-3)')
