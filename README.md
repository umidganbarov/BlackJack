# 🃏 Blackjack Strategy Simulation

> A large-scale Monte Carlo simulation and data science analysis of Blackjack strategies.

<!-- 🎬 [Watch Demo Video](https://your-video-link-here.com) -->

---

## 🎰 Overview

This project simulates **2.5 billion Blackjack hands** across 1,176 unique strategy configurations to answer one question: *is there a statistically optimal way to play Blackjack?*

| Stat | Value |
|---|---|
| 🎮 Unique configurations | 1,176 |
| 👥 Players per configuration | 26,000 |
| 🃏 Total hands simulated | ~2.5 billion |
| ⏱️ Simulation runtime | ~9 hours |

---

## 🗂️ Project Structure

```
blackjack-simulation/
├── blackjack_engine.py     # Core game logic
├── simulator.py            # Mass simulation runner
├── RESULTS.csv             # Dataset (1,176 rows × 21 columns)
├── Blackjack_Report.ipynb  # Full analysis notebook
└── README.md
```

---

## 🎲 What Was Simulated

- **Strategies:** `random`, `stand14` through `stand19`
- **Betting:** flat (5–30), percentage (5p–30p), Martingale, all-in, card counting
- **Card counting:** Hi-Lo system on/off
- **Starting balances:** $50 · $100 · $250 · $500 · $1,000 · $5,000 · $10,000

---

## 💡 Key Findings

- 🃏 **Card counting adds ~+30% win rate** — the single biggest factor
- ✅ **`stand16` is the best strategy** — hits ~94% win rate with counting
- 💰 **Starting balance matters but plateaus** after ~$1,000
- ⚠️ **Martingale is deceptive** — great returns, catastrophic when it fails
- 📊 **Hand win rate ≠ balance win rate** — a player lost 64% of hands yet kept 97% of their money
- 🚀 **Biggest outlier:** $100 → $66,870 (66,870% return) via 30% percentage betting

---

## 📓 Analysis

Full analysis in [`Blackjack_Report.ipynb`](Blackjack_Report.ipynb) — 8 tests covering card counting, strategy comparison, risk, betting systems, and extreme outcomes.

---

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib jupyter
jupyter notebook Blackjack_Report.ipynb
```

---

## 🛠️ Tech Stack

**Python** · **pandas** · **NumPy** · **Matplotlib** · **Jupyter**

---

*Personal data science project — Monte Carlo simulation meets casino strategy.*
