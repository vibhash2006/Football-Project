# Football Analytics & World Cup 2026 Prediction
 
An end-to-end football analytics pipeline built from scratch — covering data engineering, unsupervised player profiling, and a Monte Carlo World Cup 2026 simulation.
 
---
 
## Overview
 
This project builds a **player intelligence and match prediction system** across 16 leagues and 3 seasons (2023/24 — 2025/26). The pipeline classifies players into tactical archetypes using unsupervised learning, constructs team strength vectors from those profiles, and simulates the 2026 FIFA World Cup using a trained match prediction model.
 
The project is structured in two phases:
 
- **Phase 1 — Player Profiling:** Scraping, cleaning, feature engineering, EWMA baselines, and K-Means clustering to produce tactical archetypes for every outfield player and goalkeeper across 16 leagues
- **Phase 2 — World Cup Prediction:** Aggregating player profiles into national team vectors, training a goal difference prediction model on 2025/26 league data, and simulating the full 48-team tournament 10,000 times via Monte Carlo
---
 
## Pipeline
 
```
Raw Data (Sofascore via ScraperFC)
        ↓
Data Cleaning & Two-Pass Merge System
        ↓
Feature Engineering (per90, ratios, efficiency metrics)
        ↓
EWMA 3-Season Baseline (α = 0.5, raw counts first)
        ↓
Global Z-Score Standardisation (16 leagues pooled)
        ↓
PCA + K-Means Clustering (per position, 75% variance floor)
        ↓
Tactical Archetype Assignment
        ↓
Minutes-Weighted Team Feature Vectors
        ↓
Match Prediction Model (XGBoost, goal difference target)
        ↓
Monte Carlo World Cup Simulation (10,000 runs)
```
 
---
 
## Data
 
**Sources:**
- [Sofascore](https://www.sofascore.com/) via [ScraperFC](https://github.com/ztandrews/ScraperFC) — 70+ player stats per season
- [football-data.org](https://www.football-data.org/) — match results for model training
**Coverage:**
 
| Tier | Leagues |
|------|---------|
| Big 5 | Premier League, La Liga, Bundesliga, Serie A, Ligue 1 |
| Secondary European | Championship, Eredivisie, Primeira Liga, Süper Lig |
| Second Divisions | La Liga 2, 2. Bundesliga, Serie B, Ligue 2 |
| Other | Saudi Pro League, MLS, Argentina Liga Profesional de Fútbol|
 
3 seasons × 16 leagues × all positions — approximately **8,000+ player-season records**
 
---
 
## Player Archetypes
 
Clustering performed separately per position group using PCA-reduced K-Means. Components retained at 75% explained variance floor. K selected by silhouette score combined with football-domain validation.
 
### Attackers (K=3, PCA=13)
| Cluster | Archetype |
|---------|-----------|
| 0 | Ball-Carrying Forward |
| 1 | Physical Center-Forward |
| 2 | Finisher |
| 3 | Creative Forward |
 
### Midfielders (K=4, PCA=16)
| Cluster | Archetype |
|---------|-----------|
| 0 | Deep Lying Playmaker |
| 1 | Box-to-Box / Press Runner |
| 2 | Advanced Playmaker |
| 3 | Defensive Midfielder |
 
### Defenders (K=5, PCA=19)
| Cluster | Archetype |
|---------|-----------|
| 0 | Traditional / Defensive CB |
| 1 | Attacking Fullback |
| 2 | Aerial CB |
| 3 | Defensive Fullback |
| 4 | Ball-Playing CB |
 
### Goalkeepers
| Cluster | Archetype |
|---------|-----------|
| 0 | Sweeper Keeper |
| 1 | Line Savers |
| 2 | Box Commmanders |

 
## EWMA Baseline System
 
Players with multiple seasons receive an Exponentially Weighted Moving Average baseline that prioritises recent form:
 
```
α = 0.5
Season weights (3 seasons): ~57% recent, ~29% prior, ~14% oldest
```
 
**Key design decisions:**
- EWMA applied to **raw counts first** — per90s and ratios derived after
- Seasons aligned by **recency rank** rather than calendar label (handles MLS/Argentina schedule mismatch)
- Bias-corrected initialisation for 1 and 2 season players
- Parallel unweighted 3-season average maintained for stability comparison
---
 
## World Cup Simulation
 
### Team Feature Construction
For each national team, player EWMA baselines are aggregated using **rank-based importance weights** rather than raw minutes to prevent individual dominant club performers from inflating national team vectors:
 
```
Starter rank 1 → weight 1.00
Starter rank 2 → weight 0.95
...
Bench rank 1  → weight 0.60
Bench rank 2  → weight 0.55
...floor at 0.20
```
 
League quality applied as a multiplier before aggregation:
 
```python
taxed_values = clipped_values * league_coefficients
```
 
### Match Prediction Model
- **Target:** Goal difference (regression)
- **Training data:** 8 leagues × 2025/26 season ≈ 2,800 matches
- **Key feature:** Have flipped Home and Away for 50% matches to eliminate Home bias
- **Randomness:** Training residuals sampled during simulation to capture unexplained match variance
### Simulation Results (10,000 runs)
 
| Team | Win % | Runner-Up % | Semi % |
|------|-------|-------------|--------|
| Argentina | 11.50 | 8.54 | 17.14 |
| Portugal | 10.72 | 8.01 | 16.32 |
| Brazil | 10.33 | 8.07 | 16.17 |
| England | 10.28 | 8.23 | 16.44 |
| Germany | 7.72 | 6.92 | 13.63 |
| France | 7.61 | 6.93 | 14.04 |
| Spain | 7.34 | 6.75 | 13.57 |
 
---
 
## Known Limitations
 
### Current Limitations
- League coefficient multiplication compresses z-scores toward the mean, creating a systematic bias toward balanced team profiles over elite-in-one-area teams
- Club statistical profiles cannot fully capture international cohesion, tournament experience, or tactical differences between club and national team roles
- South American / African domestic league players missing from database — replaced by position average fallback
- January transfer window creates squad assignment noise within the training season

---
 
## Project Structure
 
```
Football-Project/
├── notebooks/
│   ├── data_collection/      # Sofascore scraping
│   ├── data_engineering/     # Cleaning, merging, feature engineering
│   ├── modelling/            # EWMA, clustering per position
│   └── world_cup/            # Team features, simulation
├── src/
│   ├── build_team_features.py
│   ├── calc_weighted_group.py
│   ├── ewma_players.py
│   └── league_coefficients.py
├── models/                   # Saved model files
└── .gitignore
```
 
---
 
## Tech Stack
 
| Area | Tools |
|------|-------|
| Data Collection | ScraperFC, Requests |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn (PCA, KMeans, StandardScaler), XGBoost, Catboost, Lightgbm |
| Simulation | NumPy Monte Carlo |
| Environment | Python 3.12, Jupyter Notebooks |
 
---
 
## Setup
 
```bash
git clone https://github.com/vibhash2006/Football-Project.git
cd Football-Project
pip install -r requirements.txt
```
 
**Key dependencies:**
```
scraperfc
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
```
 
---
 
## Author
 
**Vibhash Agarwal** — built as an independent research project combining football domain knowledge with data science methodology.
 
[GitHub](https://github.com/vibhash2006) 
 
---
 
*Data sourced from Sofascore and football-data.org. This project is for research and educational purposes only.*
