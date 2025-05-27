
# GLD Arbitrage Monitor

This is a real-time web-based arbitrage monitor for comparing SPDR Gold Shares (GLD) against spot gold price (GOLD futures).

## Features

- Live GLD and GOLD price retrieval via Yahoo Finance
- Real-time calculation of theoretical GLD price
- Arbitrage opportunity signal when the difference exceeds ±1%
- Auto-refresh every 5 minutes
- Docker-ready for easy cloud deployment

## Deployment (Railway/Docker)

1. Upload this project to your GitHub
2. Go to https://railway.app and create a new project
3. Select "Deploy from GitHub Repo"
4. Railway will automatically detect the Dockerfile and deploy your Flask app
