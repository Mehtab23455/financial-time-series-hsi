# Volatility Dynamics of the Hang Seng Index

This repository contains an empirical study of equity market volatility using ARCH/GARCH models. The project begins with a single-market analysis of the Hang Seng Index and is later extended to a comparative study with the Nikkei 225 to examine cross-market volatility persistence in Asia.


## Research Objective

The study investigates whether HSI returns exhibit volatility clustering and whether a GARCH framework can adequately model this behavior.

## Data

- Daily Hang Seng Index (^HSI)
- Source: Yahoo Finance
- Sample period: 2000–Present

## Methodology

- Log-return transformation
- Rolling volatility analysis
- ARCH-LM test for conditional heteroskedasticity
- GARCH(1,1) volatility modeling

## Key Findings

- Returns are stationary
- Strong volatility clustering is present
- ARCH effects are statistically significant
- GARCH(1,1) captures persistent volatility dynamics

## Repository Structure

