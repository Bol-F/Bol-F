<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Bol-F/Bol-F/main/assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Bol-F/Bol-F/main/assets/hero-light.svg">
  <img alt="Firdavs Baliyev — Python Backend Developer" src="https://raw.githubusercontent.com/Bol-F/Bol-F/main/assets/hero-light.svg" width="100%">
</picture>

<p align="center">
  <a href="mailto:bolievfirdavs0@gmail.com"><img src="https://img.shields.io/badge/Email-bolievfirdavs0%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://www.linkedin.com/in/%D1%84%D0%B8%D1%80%D0%B4%D0%B0%D0%B2%D1%81-%D0%B1%D0%BE%D0%BB%D0%B8%D0%B5%D0%B2-a430253a8/"><img src="https://img.shields.io/badge/LinkedIn-Firdavs_Baliyev-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://t.me/Bol_F"><img src="https://img.shields.io/badge/Telegram-%40Bol__F-229ED9?style=flat-square&logo=telegram&logoColor=white" alt="Telegram"></a>
</p>

## Professional Summary

Python backend developer focused on building **reliable APIs, data-intensive applications and production-oriented AI/ML systems**. My strongest area is backend engineering with Django and Django REST Framework, supported by practical experience with PostgreSQL, Redis, Celery, Docker, automated testing and CI/CD.

I also build applied machine-learning projects that cover more than model training: **data preparation, experiment tracking, evaluation, model serving, API integration and deployment**. My current portfolio includes international-trade analytics, NLP sentiment analysis, telecom churn prediction and a full-stack e-commerce platform.

I am currently pursuing a **Bachelor's Degree in Cybersecurity at Tashkent University of Information Technologies (TUIT), 2024–2028**.

---

## Engineering Profile

| Area | Practical focus |
| --- | --- |
| **Backend Engineering** | Python, Django, Django REST Framework, REST APIs, authentication, permissions, asynchronous/background workflows |
| **Data Systems** | PostgreSQL, SQL, Redis, Supabase, Polars, PyArrow, structured ingestion and validation workflows |
| **Applied AI / ML** | scikit-learn, PyTorch, Hugging Face Transformers, classification, NLP, anomaly detection, model evaluation |
| **MLOps / Delivery** | MLflow, model serving, quality gates, Docker, GitHub Actions, scheduled retraining workflows |
| **Frontend Integration** | Next.js, React, TypeScript, Tailwind CSS, API-driven frontend/backend integration |
| **Quality & Operations** | pytest, unittest, Ruff, mypy, OpenAPI/Swagger, structured logging, environment-based configuration |

---

## Selected Engineering Work

### TradeGraph AI
**Repository:** [Bol-F/trade-ai](https://github.com/Bol-F/trade-ai)

Self-hosted international-trade intelligence platform for exploring bilateral trade data, country and product profiles, concentration/exposure indicators, anomaly signals, forecasts and explainable supplier recommendations.

- **Data pipeline:** BACI-compatible CSV/ZIP input → validation and transformation with Polars → partitioned Parquet → PostgreSQL ingestion.
- **Backend:** Django REST Framework API, secure authentication, user/admin roles, saved analyses and administrative data-health views.
- **Data infrastructure:** PostgreSQL, Redis, Celery and S3-compatible object storage through MinIO.
- **Machine learning:** Isolation Forest anomaly detection, baseline/Ridge/gradient-boosting forecasting and explainable supplier ranking logic.
- **Engineering quality:** metrics, structured logs, API documentation, automated tests, Ruff, mypy, Vitest, Playwright and Docker Compose.
- **Security:** CSRF protection, HTTP-only JWT cookies, input validation, archive limits, SSRF-resistant external downloads and production configuration checks.

**Stack:** `Python` · `Django` · `DRF` · `PostgreSQL` · `Polars` · `PyArrow` · `Redis` · `Celery` · `scikit-learn` · `Next.js` · `TypeScript` · `Docker`

---

### PulseNLP — Sentiment Analysis Platform
**Repository:** [Bol-F/NLP-classifier](https://github.com/Bol-F/NLP-classifier)

Three-class NLP system that classifies English text as **negative, neutral or positive**, exposes prediction probabilities and serves the model through a production-style web application and API.

- **Training data:** reproducible seven-source preparation pipeline using DynaSent, TweetEval, GoEmotions, Yelp, Amazon Reviews and SST-5.
- **Models:** calibrated multi-domain scikit-learn ensemble plus a PyTorch / Hugging Face Transformer training and serving path.
- **Evaluation:** the current ensemble is evaluated on **17,922 untouched test examples**, with **63.63% accuracy**, **63.33% macro F1** and **0.85% expected calibration error**.
- **Robustness work:** separate difficult-case suite for negation, contrast, sarcasm, mixed sentiment, understatement and implicit sentiment.
- **Serving:** Django REST Framework, batch inference, model metadata, stable error responses, throttling and OpenAPI/Swagger documentation.
- **Frontend:** Next.js / React interface with Analyzer, Analytics, History and Model views.

**Stack:** `Python` · `Django 5` · `DRF` · `scikit-learn` · `PyTorch` · `Transformers` · `Next.js` · `React` · `TypeScript` · `OpenAPI`

---

### Telecom Customer Churn MLOps
**Repository:** [Bol-F/boraq-task2](https://github.com/Bol-F/boraq-task2)  
**Live:** [Frontend](https://boraq-task2.vercel.app) · [API documentation](https://telecom-churn-api-q92o.onrender.com/api/docs/)

End-to-end machine-learning delivery project that validates data, trains candidate models, tracks experiments, applies quality gates and serves an approved model through an API.

- **Dataset:** 7,043 customer records with 19 model features.
- **Training:** reproducible preprocessing and comparison of balanced Logistic Regression and Random Forest pipelines.
- **Experiment tracking:** MLflow experiment and artifact tracking.
- **Approved model:** Logistic Regression `v1.0.0`.
- **Measured performance:** **ROC-AUC 0.8417**, **PR-AUC 0.6327**, **F1 0.6136**.
- **Model governance:** quality-gated promotion, approved model metadata and guarded scheduled retraining.
- **Delivery:** Django REST Framework API, Next.js frontend, Docker, pytest, GitHub Actions CI and Render/Vercel deployment.

**Stack:** `Python` · `scikit-learn` · `MLflow` · `Django REST Framework` · `pytest` · `Docker` · `GitHub Actions` · `Next.js`

---

### Bloom & Petal — Full-Stack Marketplace
**Repository:** [Bol-F/flower-shop](https://github.com/Bol-F/flower-shop)  
**Live:** [flower-store-theta.vercel.app](https://flower-store-theta.vercel.app)

Full-stack flower marketplace with customer ordering flows and internal staff operations.

- **Customer flows:** catalog, search/filtering, cart, checkout, order history, reviews and support messages.
- **Backend design:** Django REST APIs, relational domain models, custom user/auth flows and JWT authentication.
- **Business rules:** stock validation, order creation, payment-status workflows and notification logging.
- **Payments:** safe fake/test payment provider with abstractions prepared for future real-provider integration.
- **Operations:** staff dashboard, inventory alerts, support replies and Django admin.
- **Delivery:** PostgreSQL/Supabase, automated tests, Docker, GitHub Actions, Render backend and Vercel frontend.

**Stack:** `Python` · `Django REST Framework` · `PostgreSQL` · `Supabase` · `Redis` · `Celery` · `Next.js` · `TypeScript` · `Docker`

---

## Technology Matrix

| Domain | Technologies |
| --- | --- |
| **Languages** | Python, JavaScript, TypeScript, SQL |
| **Backend** | Django, Django REST Framework, Django ORM, Celery, REST API design |
| **Authentication / Access** | JWT, OAuth2 concepts, role-based access control, permissions |
| **Databases / Storage** | PostgreSQL, Supabase, SQLite, Redis, MinIO / S3-compatible storage |
| **Data Processing** | pandas, Polars, PyArrow |
| **Machine Learning** | scikit-learn, PyTorch, Hugging Face Transformers, MLflow |
| **Frontend** | React, Next.js, TypeScript, Tailwind CSS |
| **Testing / API** | pytest, unittest, Postman, Swagger / OpenAPI, Playwright, Vitest |
| **DevOps / Delivery** | Docker, Docker Compose, GitHub Actions, CI/CD, Linux CLI, Render, Vercel, PythonAnywhere |
| **Engineering Practices** | Git/GitHub, branches and pull requests, environment variables, linting, type checking, documentation |

---

## Engineering Approach

I try to treat portfolio projects as engineering systems rather than isolated demos:

1. **Define the data and API contracts** before adding application logic.
2. **Keep business logic testable** and separate from transport/UI concerns.
3. **Validate inputs and configuration** instead of relying on implicit assumptions.
4. **Measure ML quality** with explicit metrics and preserve model metadata.
5. **Automate checks** with tests, linting/type checks and CI where appropriate.
6. **Design for reproducibility** with dependency locking, environment configuration and documented setup.
7. **Ship working interfaces** so backend and ML work can be evaluated end to end.

---

## Experience

### Freelance Backend / Full-Stack Developer
Built backend and full-stack web applications using Python, Django and Django REST Framework. Worked with REST APIs, authentication and permissions, PostgreSQL data modeling, frontend integration, API documentation, testing and deployment workflows.

### Programming Instructor — Megaschool
**Sep 2025 – Jun 2026 · Tashkent**

Taught programming and IT fundamentals, with emphasis on Python, algorithms and practical problem solving. Prepared exercises, reviewed student work, tracked progress and provided individual support.

---

## Education

**Tashkent University of Information Technologies named after Muhammad al-Khwarizmi**  
Bachelor's Degree in Cybersecurity · **2024–2028** · Tashkent, Uzbekistan

---

## Competitions, Hackathons & Training

- **ICPC Uzbekistan Regional Contest 2025** — Honorable Mention in team-based algorithmic problem solving.
- **Cursor Hackathon Tashkent 2026** — Backend Developer, Team Qabila; contributed backend logic and APIs for a Smart Farm MVP.
- **ActInSpace Uzbekistan 2026** — worked on an ML/CV concept using Sentinel-1/2 and LiDAR data for green-zone analysis.
- **Backend Developer Training — Ustudy** — Python, OOP, databases, algorithms and data structures.
- **BePro AI/ML (Boraq)** — data preprocessing, supervised ML, model comparison/evaluation, anomaly detection, dimensionality reduction and neural-network fundamentals.

---

## Languages

| Language | Level |
| --- | --- |
| Uzbek | Native |
| Russian | Fluent |
| English | Advanced |

---

## Contribution Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Bol-F/Bol-F/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Bol-F/Bol-F/output/github-contribution-grid-snake.svg">
    <img alt="GitHub contribution activity" src="https://raw.githubusercontent.com/Bol-F/Bol-F/output/github-contribution-grid-snake.svg">
  </picture>
</p>

<p align="center"><sub>Generated automatically through GitHub Actions.</sub></p>

---

## Contact

I am interested in **Python backend, backend-heavy full-stack and applied AI/ML engineering opportunities**.

- Email: **bolievfirdavs0@gmail.com**
- LinkedIn: [Firdavs Baliyev](https://www.linkedin.com/in/%D1%84%D0%B8%D1%80%D0%B4%D0%B0%D0%B2%D1%81-%D0%B1%D0%BE%D0%BB%D0%B8%D0%B5%D0%B2-a430253a8/)
- Telegram: [@Bol_F](https://t.me/Bol_F)
- GitHub: [github.com/Bol-F](https://github.com/Bol-F)
