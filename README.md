# ssdcoin-blockchain

SSDCoin Website: https://ssdcoin.top

Full Node Port: 30088

## How to staking

1. Query the staking balance:

   ```
   $ ssd staking info
   ...
   Staking balance:  0
   Staking address:  ssd1lnvsnstgtpg20c6pufryq6hv08jchj0vpvymq2zzm65lze3f87aq040ux3
   ...
   ```

2. Send coins to the staking:

   ```
   $ ssd staking send -a 1
   ```

   Wait for the transaction get confirmed, query staking balance again:

   ```
   $ ssd staking info
   ...
   Staking balance:  1
   Staking address:  ssd1lnvsnstgtpg20c6pufryq6hv08jchj0vpvymq2zzm65lze3f87aq040ux3
   ...
   ```

3. Withdraw coins from the staking address:

   ```
   $ ssd staking withdraw -a 1
   ```

   Do a transaction to transfer the coins from the staking address to now wallet receive address.