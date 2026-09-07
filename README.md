<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Bol-F/Bol-F/main/assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Bol-F/Bol-F/main/assets/hero-light.svg">
  <img alt="Firdavs Baliyev — Python Backend Developer and Applied AI/ML" src="https://raw.githubusercontent.com/Bol-F/Bol-F/main/assets/hero-light.svg" width="100%">
</picture>

<p align="center">
  <a href="mailto:bolievfirdavs0@gmail.com"><img src="https://img.shields.io/badge/Email-bolievfirdavs0%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://www.linkedin.com/in/%D1%84%D0%B8%D1%80%D0%B4%D0%B0%D0%B2%D1%81-%D0%B1%D0%BE%D0%BB%D0%B8%D0%B5%D0%B2-a430253a8/"><img src="https://img.shields.io/badge/LinkedIn-Firdavs_Baliyev-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://t.me/Bol_F"><img src="https://img.shields.io/badge/Telegram-%40Bol__F-229ED9?style=flat-square&logo=telegram&logoColor=white" alt="Telegram"></a>
</p>

<p align="center">
  <b>Backend systems · data workflows · applied AI/ML · production delivery</b>
</p>

---

## About me

I am a **Python backend developer** focused on building reliable APIs, data-driven applications and practical AI/ML products.

My strongest area is backend engineering with **Django and Django REST Framework**, supported by hands-on work with PostgreSQL, Redis, Celery, Docker, automated testing and CI/CD. I also work with applied machine learning, especially **NLP, classification, anomaly detection and model delivery**.

What I enjoy most is taking a project beyond the prototype stage — designing the API and data model, building the backend, evaluating the model, adding tests, documenting the system and making it deployable.

- 📍 Tashkent, Uzbekistan
- 🎓 Cybersecurity student at **TUIT**, 2024–2028
- 💼 Experience in freelance backend/full-stack development
- 🧠 Building with **scikit-learn, PyTorch, Hugging Face and MLflow**
- 🏆 ICPC Uzbekistan Regional — **Honorable Mention**

---

## Featured projects

### 🌍 [TradeGraph AI](https://github.com/Bol-F/trade-ai)
**International-trade intelligence platform** for exploring bilateral trade data through country and product profiles, maps, concentration indicators, anomaly signals, forecasts and supplier recommendations.

**What is inside**
- BACI-compatible CSV/ZIP validation and transformation with **Polars + PyArrow**
- partitioned Parquet processing and resumable **PostgreSQL** ingestion
- Django REST Framework API with authentication, roles and saved analyses
- **Redis + Celery** for caching and background jobs
- Isolation Forest anomaly detection and forecasting workflows
- metrics, structured logs, tests, type checking and Docker Compose
- production-oriented security controls for authentication, uploads and external downloads

`Python` `Django REST Framework` `PostgreSQL` `Polars` `PyArrow` `Redis` `Celery` `scikit-learn` `Next.js` `Docker`

---

### 🧠 [PulseNLP](https://github.com/Bol-F/NLP-classifier)
**Three-class sentiment analysis platform** for classifying English text as negative, neutral or positive, with reproducible training and a production-style inference API.

**What is inside**
- seven-source data pipeline using DynaSent, TweetEval, GoEmotions, Yelp, Amazon Reviews and SST-5
- calibrated **scikit-learn** ensemble and a **PyTorch / Hugging Face Transformer** path
- batch inference, model metadata, throttling and OpenAPI/Swagger docs
- difficult-case evaluation for negation, sarcasm, contrast and mixed sentiment
- Next.js interface with Analyzer, Analytics, History and Model views

**Measured evaluation:** 17,922 test examples · **63.63% accuracy** · **63.33% macro F1** · **0.85% ECE**

`Python` `Django 5` `DRF` `scikit-learn` `PyTorch` `Transformers` `Next.js` `TypeScript`

---

### 📊 [Telecom Customer Churn MLOps](https://github.com/Bol-F/boraq-task2)
**End-to-end ML delivery project** that trains, compares, tracks, validates and serves customer-churn models.

**What is inside**
- reproducible preprocessing and model training pipeline
- Logistic Regression and Random Forest comparison
- **MLflow** experiment tracking and artifact management
- model-quality gate before promotion
- scheduled guarded retraining through GitHub Actions
- Django REST Framework prediction API
- Dockerized backend and deployed Next.js frontend

**Approved model:** Logistic Regression v1.0.0  
**ROC-AUC:** 0.8417 · **PR-AUC:** 0.6327 · **F1:** 0.6136

<p>
  <a href="https://boraq-task2.vercel.app"><b>Live demo ↗</b></a>
  &nbsp;·&nbsp;
  <a href="https://telecom-churn-api-q92o.onrender.com/api/docs/"><b>API docs ↗</b></a>
</p>

`Python` `scikit-learn` `MLflow` `Django REST Framework` `pytest` `Docker` `GitHub Actions` `Next.js`

---

### 🌸 [Bloom & Petal](https://github.com/Bol-F/flower-shop)
**Full-stack flower marketplace** with customer ordering flows and internal staff operations.

**What is inside**
- catalog, search/filtering, cart, checkout and order history
- JWT authentication and relational domain modeling
- stock validation and payment-status workflows
- reviews, support messages and notification logging
- staff dashboard and Django admin operations
- automated tests, Docker, GitHub Actions and cloud deployment

<p>
  <a href="https://flower-store-theta.vercel.app"><b>Live demo ↗</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Bol-F/flower-shop"><b>Source code ↗</b></a>
</p>

`Python` `Django REST Framework` `PostgreSQL` `Supabase` `Redis` `Celery` `Next.js` `TypeScript` `Docker`

---

## Tech stack

<table>
  <tr>
    <td><b>Backend</b></td>
    <td>Python · Django · Django REST Framework · REST APIs · Celery · JWT · OAuth2 concepts</td>
  </tr>
  <tr>
    <td><b>Data</b></td>
    <td>PostgreSQL · SQL · Redis · Supabase · Polars · PyArrow · pandas</td>
  </tr>
  <tr>
    <td><b>AI / ML</b></td>
    <td>scikit-learn · PyTorch · Hugging Face Transformers · MLflow · NLP · anomaly detection · model evaluation</td>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td>React · Next.js · TypeScript · JavaScript · Tailwind CSS</td>
  </tr>
  <tr>
    <td><b>Quality</b></td>
    <td>pytest · unittest · Ruff · mypy · OpenAPI / Swagger · Postman · Playwright · Vitest</td>
  </tr>
  <tr>
    <td><b>Delivery</b></td>
    <td>Docker · Docker Compose · GitHub Actions · CI/CD · Linux · Render · Vercel · PythonAnywhere</td>
  </tr>
</table>

---

## Experience & education

### Freelance Backend / Full-Stack Developer
Building REST APIs, authentication systems, database-backed applications, frontend integrations and deployment workflows with Python/Django-based stacks.

### Programming Instructor — Megaschool
**Sep 2025 – Jun 2026 · Tashkent**

Taught Python and programming fundamentals, prepared practical exercises, reviewed student work and provided individual support.

### Tashkent University of Information Technologies
**Bachelor's Degree in Cybersecurity · 2024–2028**

---

## Highlights

- 🧩 **ICPC Uzbekistan Regional Contest 2025** — Honorable Mention
- 🌱 **Cursor Hackathon Tashkent 2026** — Backend Developer, Team Qabila; Smart Farm MVP
- 🛰️ **ActInSpace Uzbekistan 2026** — ML/CV concept using Sentinel-1/2 and LiDAR data
- 🐍 **Backend Developer — Ustudy** — Python, OOP, databases, algorithms and data structures
- 🤖 **BePro AI/ML (Boraq)** — preprocessing, supervised ML, evaluation, anomaly detection and neural-network fundamentals

---

## Languages

**Uzbek** — Native · **Russian** — Fluent · **English** — Advanced

---

## Contribution activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Bol-F/Bol-F/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Bol-F/Bol-F/output/github-contribution-grid-snake.svg">
    <img alt="GitHub contribution activity" src="https://raw.githubusercontent.com/Bol-F/Bol-F/output/github-contribution-grid-snake.svg">
  </picture>
</p>

<p align="center"><sub>Automatically refreshed with GitHub Actions.</sub></p>

---

<p align="center">
  <b>Open to Python backend, backend-heavy full-stack and applied AI/ML opportunities.</b><br><br>
  <a href="mailto:bolievfirdavs0@gmail.com">Email</a> ·
  <a href="https://www.linkedin.com/in/%D1%84%D0%B8%D1%80%D0%B4%D0%B0%D0%B2%D1%81-%D0%B1%D0%BE%D0%BB%D0%B8%D0%B5%D0%B2-a430253a8/">LinkedIn</a> ·
  <a href="https://t.me/Bol_F">Telegram</a>
</p>
