# 🧪 Portfolio Stress Tester (Monte Carlo Simulation)

A Python-based **portfolio risk simulation engine** that uses Monte Carlo methods to model how a crypto portfolio might behave under thousands of possible future market scenarios.

This project focuses on **risk quantification, downside exposure, and tail-risk analysis** rather than price prediction.

---

## 🚀 What This Project Does

- Loads historical BTC & ETH price data
- Converts prices into daily returns
- Models return distribution & covariance
- Simulates thousands of future price paths
- Projects portfolio value over time
- Computes risk metrics like:
  - Value at Risk (VaR)
  - Tail loss (Black Swan scenarios)

---

## 🧠 Why Monte Carlo Simulation?

Markets are uncertain and path-dependent.

Monte Carlo helps answer:

> “What range of outcomes could my portfolio realistically face?”

Instead of one forecast, you get **thousands of probabilistic scenarios**.

---

## ⚙️ Simulation Pipeline

### 1️⃣ Data Preparation

Historical prices are converted to returns:
- returns = pct_change(close)

Assets used:

- BTC
- ETH

---

### 2️⃣ Statistical Modeling

The simulation builds:

- Mean returns vector
- Covariance matrix

Then samples future returns using:
- np.random.multivariate_normal()

This preserves correlation between assets.

---

### 3️⃣ Portfolio Allocation

Example weights:
- BTC → 100%
- ETH → 0%

---

### 📦 Installation
1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Portfolio-Stress-Tester.git
cd Portfolio-Stress-Tester