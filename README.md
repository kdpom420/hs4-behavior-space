# Behavioral State Space Analysis of HS4 Trade Goods Using UN Comtrade


K.D. Pom   
**Date:** 2026-05-11  
**DOI:** [10.5281/zenodo.20115524](http://doi.org/10.5281/zenodo.20115524)  

## Overview

This repository contains an exploratory analysis of international trade behavior using HS4-level export data from the United Nations Comtrade database.

Instead of treating HS codes as static product categories, this work interprets each HS4 product as a behavioral state vector constructed from trade dynamics such as growth, volatility, country expansion, and persistence.

Using dimensionality reduction and unsupervised clustering techniques, the analysis explores whether global trade goods form an interpretable behavioral state space and whether products exhibit temporal topology drift over time.

The project particularly focuses on identifying potential “postal-friendly” trade goods associated with small-scale, repeatable, cross-border e-commerce and international postal flows.

---

# Dataset

Source:

- United Nations Comtrade Database

Data level:

- HS4 export statistics
- Multi-country trade records
- Multi-year aggregated observations

Main variables used:

- Export net weight
- Growth metrics
- Country diversity
- Volatility measures
- Unit-value proxy indicators
- Temporal persistence metrics

---

# Feature Engineering

For each HS4 product, a behavioral feature vector was constructed using:

- Trade volume scale
- Volatility
- Recent growth rate
- Growth persistence
- Country spread/diversity
- Unit-value proxy

This transforms:

HS Code → Behavioral Vector

rather than treating HS codes only as categorical identifiers.

---

# Methods

## PCA (Principal Component Analysis)

Used to identify dominant axes of trade behavior.

Main findings:

- PC1 primarily represented:
  - scale
  - country expansion
  - persistent growth

- PC2 primarily represented:
  - recent rapid growth behavior

The first two principal components explained approximately 71.6% of total variance.

---

## KMeans Clustering

HS4 products were grouped into behavioral clusters.

Observed clusters included:

- Postal-friendly core goods
- High-value expansion goods
- Apparel growth/volatile goods
- Low-growth niche goods
- Premium anomaly goods

Representative postal-friendly products included:

- Cosmetics
- Processed foods
- Books
- Plastic consumer goods
- Medical consumables
- Hair products
- Packaging materials

---

## UMAP Embedding

UMAP revealed more dynamic manifold-like structures compared to PCA.

Observed patterns included:

- Cosmetics, food, consumer goods, and electronics occupying dense postal/e-commerce-friendly regions
- Apparel categories forming elongated continuous manifolds
- Premium apparel products appearing as isolated anomaly regions

This suggests that trade products may exhibit topology-like behavioral organization beyond conventional HS categorization.

---

# Drift and Trajectory Analysis

Yearly embeddings were tracked to construct temporal trajectories for HS products.

This analysis explored:

- behavioral stability
- structural drift
- oscillation patterns
- possible regime transitions

Examples:

- Cosmetics showed post-shock stabilization behavior
- Plastic consumer goods showed gradual structural drift
- Infant apparel showed unstable oscillatory behavior
- Printed media products suggested structural transition dynamics

Drift length was interpreted as:

> “total behavioral movement within trade state space”

rather than simple export growth alone.

---

# Interpretation

The analysis suggests that:

- international trade goods may occupy structured behavioral regions
- some product groups exhibit stable long-term trade states
- other products exhibit strong topology drift associated with market change, platform expansion, or structural transformation

The identified “postal-friendly” region appears to be associated with:

- small physical size
- repeat consumption
- broad country expansion
- stable growth persistence

---

# Limitations

This work is exploratory and observational in nature.

Limitations include:

- HS4 aggregation constraints
- absence of causal inference
- dependence on feature construction choices
- embedding method sensitivity
- incomplete representation of logistics channels

The analysis should therefore be interpreted as exploratory behavioral topology research rather than definitive economic modeling.

---

# Future Work

Potential extensions include:

- country-level trade state centroids
- temporal regime-shift detection
- graph/topological analysis
- trajectory animation
- integration with logistics and postal datasets
- higher-resolution HS6 analysis

---

# Keywords

- UN Comtrade
- HS4
- Behavioral State Space
- Trade Topology
- UMAP
- PCA
- Trade Drift
- International Postal Trade
- Behavioral Embedding
- Economic Complexity

---

# License

CC BY 4.0

---

# Citation

If you use or reference this work, please cite the associated Zenodo DOI record.