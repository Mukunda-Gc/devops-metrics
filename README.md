# Automated DevOps Productivity and Reliability Measurement using GitHub Actions

![Pipeline](https://img.shields.io/badge/CI%2FCD-Automated-success)
![Security Scan](https://img.shields.io/badge/Security-Checked-green)
![DORA Metrics](https://img.shields.io/badge/DORA-Monitored-blue)

This project automates the collection, visualization, and security validation of DevOps productivity metrics (DORA) using GitHub Actions and Python.

## 🚀 Features
- Automated CI/CD pipeline (Build → Test → Security Scan → Deploy)
- Automatic logging of deployments to metrics.csv
- DORA metrics calculation via Python
- Graph visualization of Deployment Frequency
- Real-time project badges (status indicators)

## ⚙️ Pipeline Overview
1. **Build** – Simulated build step
2. **Test** – Verifies basic functionality
3. **Security Scan** – Checks for vulnerabilities before deployment
4. **Deploy** – Copies and logs deployment
5. **Metrics Update** – Appends data to metrics.csv

## 📊 Python Analysis Scripts
- `calculate_metrics.py` → Calculates DORA metrics
- `visualize_metrics.py` → Generates charts for deployment frequency

## 🧰 Setup in VS Code (Windows)
1. Clone your GitHub repo.
2. Extract these files into the repo folder.
3. Open in VS Code → run the following once:
   ```bash
   git init
   git add .
   git commit -m "init: project scaffold"
   git branch -M main
   git remote add origin https://github.com/<your-username>/devops-metrics-demo.git
   git push -u origin main
   ```
4. Enable GitHub Actions → check the **Actions** tab.

## 🧪 Generate Data
To simulate multiple runs:
```bash
echo "<p>Version update</p>" >> index.html
git add index.html
git commit -m "feat: update version"
git push
```
To simulate a failed deploy:
```bash
git commit -m "test: simulate [fail]" --allow-empty
git push
```

## 📈 Visualize Results
Run:
```bash
python calculate_metrics.py
python visualize_metrics.py
```
Then include `deployment_frequency_chart.png` in your report.

## 🛡️ Security Integration
Each run now includes a **Security Scan (Simulated)** stage to validate code before deployment — aligning the project with DevSecOps principles.

## 📷 Recommended Report Screenshots
1. Actions tab showing multiple runs (green + red)
2. Security Scan stage log output
3. metrics.csv content on GitHub
4. Python DORA metrics output
5. Deployment frequency chart
6. README badges view

## 📚 References
- GitHub Actions Documentation – https://docs.github.com/actions
- DORA Metrics Guide – Google Cloud DevOps Research
