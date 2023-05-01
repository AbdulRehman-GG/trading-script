# trading-script

This script first connects to the Alpaca API using your API key and secret key. It then defines a execute_strategy() function, where you can define your specific trading strategy based on market data.

Inside the execute_strategy() function, the script gets the current account information and checks if the market is open. If the market is closed, the function returns without executing the trading strategy.

Next, the script gets the latest price data for your target stock using the get_barset() method from the Alpaca API. You can customize the symbol variable to specify your target stock. Finally, the script executes your trading strategy based on the latest price data.

The script runs continuously in a loop using the while True statement. Each time the loop runs, it calls the execute_strategy() function. You can modify the code to include additional logic for stopping the script or modifying the trading strategy based on various conditions.

# Credits
Developed by AbdulRehman#8377

(Open for Help Contact me on Discord)
