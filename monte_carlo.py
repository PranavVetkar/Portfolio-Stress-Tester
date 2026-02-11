import pandas as pd
import numpy as np

btc = pd.read_csv('btc_history.csv')['close'].pct_change().dropna()
eth = pd.read_csv('eth_history.csv')['close'].pct_change().dropna()

returns = pd.concat([btc, eth], axis=1).dropna()
mean_returns = returns.mean()
cov_matrix = returns.cov()

weights = np.array([1.0, 0.0]) 
n_simulations = 10000
days = 30
initial_investment = 1000

results = []
for _ in range(n_simulations):
    daily_returns = np.random.multivariate_normal(mean_returns, cov_matrix, days)
    portfolio_return = np.prod(1 + np.dot(daily_returns, weights))
    results.append(initial_investment * portfolio_return)

results = np.array(results)
var_95 = np.percentile(results, 5)
worst_1_percent = np.percentile(results, 1)

print(f"--- Stress Test Results (30 Days) ---")
print(f"Initial Investment: ${initial_investment}")
print(f"Average Ending Value: ${results.mean():,.2f}")
print(f"--- Risk Metrics ---")
print(f"95% Confidence VaR: ${initial_investment - var_95:,.2f}")
print(f"Worst 1% 'Black Swan' Loss: ${initial_investment - worst_1_percent:,.2f}")