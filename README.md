# Portfolio Optimization with Iterative Risk Filtering

Mean Variance portfolio optimizer with a custom multivariate facto-concentration filter,  tested out-of-sample across multiple market regimes.

## Overview
Standard mean variance optimization overfits upon historical data, due to it concentrating weight in past winners assuming inputs are 100% accurate. For example
when one stock has a much higher historical return than others, the optimizer puts as much weight here as the constraint allows, without considering outside confounding factors which may be behind the best stock. It optimizes on this noise, which is an issue I sought to minimize. 

To fix this I created a iterative risk filter that picks out multi stock factor concentration. In cases where several stocks load on the same underlying factors and as a result dominate our portfolio, the optimizer detects this and adds a dynamic group-weight cap as an added constraints and re-runs. This loops until the portfolio passes the filter. Out-of-sample backtesting across four train/test splits shows the filter outperformed the unfiltered optimizer in all four windows, with an average Sharpe improvement of +0.26.


## Methodology

- **Universe**: 10 stocks (8 tech-heavy + JPM + KO) and 7 sector ETFs as factor proxies
- **Expected returns**: Historical mean annualized returns from training window
- **Covariance**: Sample covariance, annualized
- **Optimizer**: SLSQP Sharpe maximization with per-stock cap of 15%
- **Risk filter**: Flags groups of stocks that all correlate ≥ 0.70 with the same ETF, correlate ≥ 0.60 with each other, and combined exceed 40% of portfolio weight
- **Iterative constraint generation**: When the filter flags a concentration, a group-weight cap is added and the optimizer re-runs until the portfolio passes

## Results

Walk-forward backtests across 4 train/test splits (2023-2025):

| Split | Unfiltered Sharpe | Filtered Sharpe | Improvement |
|-------|-------------------|-----------------|-------------|
| 2023-01 | 1.46 | 1.55 | +0.08 |
| 2023-07 | 0.68 | 1.05 | +0.37 |
| 2024-01 | 0.62 | 0.95 | +0.33 |
| 2024-07 | 0.27 | 0.52 | +0.24 |

The filter outperformed in **4 of 4 out-of-sample windows**, with an average Sharpe improvement of **+0.26**.


## Key insight

In-sample, the filter costs essentially zero Sharpe (0.002). Out-of-sample, it adds 0.26 on average. Thereby we can see filter is preventing overfitting, as the benefit only is visible when future is different from historical data. 


## Limitations

- Single-factor risk model 
- Sample covariance 
- Universe is hand-picked from known tech-heavy stocks
- 4 discrete test windows, not full rolling walk-forward.
- No transaction costs or slippage modeling.
