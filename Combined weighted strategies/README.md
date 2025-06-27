
This is a basic demonstration on how combining different return streams or strategies optimally can minimize volatility (ideally without sacrificing return). The same cross sectional reversal strategy is used on six large cap US stocks; namely (ticker symbol is used), 'AAPL', 'TSLA', 'NVDA', 'META', 'AMZN', and 'GOOG'. 

A 20 day moving average is calculated for return data beginning from '2020-01-01' and ending in '2023-01-01'. It is important to note that the 'Close' price was the column of interest that was obtained using yahoo finance. Each ticker is then ranked, demeaned, and normalized after the moving average is computed. Finally the computed signal is shifted forward in time to avoid look ahead bias, and the backtested strategy returns are computed. 

Each individual sharpe ratio for each ticker was nothing too interesting with only tesla having a relatively high sharpe of around 0.8.

I then proceeded to look to combine the individual strategies to reduce risk while hopefully having a higher return. The 'ideal' weights were generated using the mean-variance optimization formula and the combined portfolio was generated. As expected, it produced a sharpe ratio of around 1.4 which is higher than any of the individual strategies.

I then moved on to evaluate more performance metrics. By regressing this portfolio against a benchmark (I used SPY in this instance) I am able to see what my alpha value is (if it even exists) and the statistical significance of it, by checking its corresponding p value. A daily alpha of 0.0002% with a p value of 0.01 was obtained. This is statistically significant and shows an annuallized alpha of around 5%. 

Furthermore the maxdraw down duration of -0.036 was obtained that shows that our strategy has a low drawdown which is very good!

To conclude, this was a basic project to showcase how diversification can be beneficial and how optimal weights for combining different strategies are calculated and implemented.
