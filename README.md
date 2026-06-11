# Blackjack Strategy Simulation


A large-scale Monte Carlo simulation and data science analysis of Blackjack strategies.



<!-- Replace the line below with your actual demo video once uploaded -->
<!-- 🎬 [Watch Demo Video](https://your-video-link-here.com) -->

Overview

This project simulates 2.5 billion Blackjack hands across 1,176 unique strategy configurations to answer one question: is there a statistically optimal way to play Blackjack?

Each configuration combines a gameplay strategy, betting system, card counting method, and starting balance — run across 26,000 simulated players per combination.


Key Numbers

StatValueUnique configurations1,176Players per configuration26,000Total shoes simulated~30 millionTotal hands simulated~2.5 billionSimulation runtime~9 hours

What Was Simulated

Gameplay Strategies

StrategyDescriptionrandomHit or stand randomly (baseline)stand14–stand19Stand when hand total ≥ X, hit otherwise

Betting Systems

TypeDescription5, 10, 15, 20, 30Flat bet (fixed amount each hand)5p–30pPercentage bet (X% of current balance)maMartingale (double bet after each loss)fullAll-in every handcard_countingBet size driven by Hi-Lo count

Card Counting


Hi-Lo system — adjusts decisions and betting based on running deck count
Tested on/off across all strategy combinations


Starting Balances

$50, $100, $250, $500, $1,000, $5,000, $10,000


Key Findings

1. Card Counting Works

Counting cards adds roughly +30% average win rate across all configurations — the single biggest factor in the dataset.

2. Stand16 is the Optimal Strategy

Among all gameplay strategies, stand16 (hit on ≤15, stand on ≥16) performs best. Combined with card counting it reaches ~94% win rate.

3. Starting Balance Matters — But Plateaus

Win rate improves with starting balance but flattens after ~$1,000. More capital does not linearly equal more edge.

4. Martingale: High Return, Hidden Risk

Martingale achieves the highest average win rates but exposes players to catastrophic loss streaks. It works well with large starting balances; it destroys small ones.

5. Hand Win Rate ≠ Balance Win Rate

A player can lose 64% of hands and still keep 97% of their money. Bet sizing dominates — not how often you win.

6. Extreme Outliers Exist

Over 2.5 billion hands: someone turned $100 → $66,870 (66,870% return) using 30% percentage betting. The highest raw balance reached was $4.3 million from a $10,000 start.


Analysis Notebook

The full analysis is in Blackjack_Report.ipynb, covering 8 tests:

TestQuestion1Does card counting work?2Which gameplay strategy is best?3Does starting balance affect win rate?4Who goes broke, and why?5What is the single best configuration per balance?6Fixed vs percentage vs Martingale bets — deep dive7Hand win rate vs balance win rate8Maximum possible gains — high risk, high reward


How to Run

bash# Install dependencies
pip install pandas numpy matplotlib

# Run the analysis notebook
jupyter notebook Blackjack_Report.ipynb


Dataset Columns

ColumnDescriptionshoesNumber of simulated sessionstotal_handsTotal hands playedinitial_balanceStarting bankrollstrategyGameplay strategy usedcard_countingCounting method (hilo / dont)bettingBetting system usedwins[num]Total winning handslosses[num]Total losing handsties[num]Total push/tie handswin_rate[num]%% of hands wonwin_rate[balance]%% of players ending above 0medianMedian final balancestdStandard deviation of final balancesmin_balanceLowest final balance recordedmax_balanceHighest final balance recordedsharpe_likeRisk-adjusted return scorebrokesNumber of players who hit $0broke_rate%% of players who went bankruptprofit_count[num]Players ending above initial balanceprofit_rate%% of players who profitedperformance[sec]Simulation runtime


Tech Stack


Python — simulation engine and analysis
pandas — data manipulation
NumPy — numerical operations
Matplotlib — all visualizations
Jupyter — analysis notebook



Built as a personal data science project combining Monte Carlo simulation, statistical analysis, and Python data tools.
