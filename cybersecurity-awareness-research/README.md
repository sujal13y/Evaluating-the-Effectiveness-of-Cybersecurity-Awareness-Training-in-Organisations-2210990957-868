# Cybersecurity Awareness Training — Research Paper Code
**Evaluating the Effectiveness of Cybersecurity Awareness Training in Organisations**  
*Sujal, Vidhi Anand — Chitkara University, Punjab, India*

---

## Project File Structure

```
cybersecurity-awareness-research/
│
├── README.md                           ← You are here
│
├── scripts/
│   ├── generate_all_figures.py         ← Generates all 5 paper figures (Fig. 1–5)
│   └── statistical_analysis.py        ← Reproduces all stats: t-tests, ANOVA, Cohen's d
│
└── outputs/                            ← Auto-created when scripts run
    ├── fig1_pre_post_metrics.png       ← Fig. 1: Pre vs Post — 5 behaviour metrics
    ├── fig2_phishing_click_rate.png    ← Fig. 2: Phishing click rate over 6 months
    ├── fig3_delivery_method.png        ← Fig. 3: Training method effectiveness scores
    ├── fig4_security_incidents.png     ← Fig. 4: Quarterly security incident reduction
    └── fig5_score_distribution.png    ← Fig. 5: Employee awareness score distribution
```

---

## Steps to Generate Everything

### Step 1 — Install Python
Make sure you have Python 3.10 or newer installed. Check by running:

```bash
python --version
```

If not installed, download from [python.org](https://python.org)

---

### Step 2 — Create the Project Folder

```bash
mkdir cybersecurity-awareness-research
cd cybersecurity-awareness-research
mkdir scripts outputs
```

---

### Step 3 — Place the Files
Copy these 3 files you downloaded into the correct folders:

* `scripts/generate_all_figures.py` → goes inside the `scripts/` folder
* `scripts/statistical_analysis.py` → goes inside the `scripts/` folder
* `README.md` → goes in the root folder

Your folder should look like this:
```
cybersecurity-awareness-research/
├── README.md
├── scripts/
│   ├── generate_all_figures.py
│   └── statistical_analysis.py
└── outputs/
```

---

### Step 4 — Install Dependencies

```bash
pip install matplotlib numpy scipy pandas
```

✅ This installs all 4 required libraries: **matplotlib**, **numpy**, **scipy**, **pandas**

---

### Step 5 — Generate All 5 Figures

```bash
python scripts/generate_all_figures.py
```

✅ This creates 5 publication-ready PNG figures inside `outputs/`:

* `fig1_pre_post_metrics.png`
* `fig2_phishing_click_rate.png`
* `fig3_delivery_method_effectiveness.png`
* `fig4_security_incidents.png`
* `fig5_score_distribution.png`

Expected terminal output:
```
Fig 1 saved
Fig 2 saved
Fig 3 saved
Fig 4 saved
Fig 5 saved

All 5 figures generated successfully!
```

---

### Step 6 — Run the Statistical Analysis

```bash
python scripts/statistical_analysis.py
```

✅ This prints all tables and statistics directly in your terminal — Table I (paired t-tests + Cohen's d), One-Way ANOVA, Bonferroni post-hoc comparisons, Table II (incident reduction), phishing click-rate trajectory, and score distribution summary.

Expected terminal output:
```
=================================================================
TABLE I — Pre vs. Post-Training Performance Summary
=================================================================
...
One-Way ANOVA — Training Delivery Method Effectiveness
...
TABLE II — Security Incident Classification Before and After Training
...
Phishing Click Rate — Longitudinal Trajectory
...
Employee Awareness Score Distribution Summary (n=300)
...
✓ All statistical analyses complete.
```

---

## What Each Figure Shows

| Figure | File | Section in Paper | Key Finding |
|--------|------|-----------------|-------------|
| Fig. 1 | `fig1_pre_post_metrics.png`    | Section IV-A | All 5 metrics improved significantly post-training |
| Fig. 2 | `fig2_phishing_click_rate.png` | Section IV-B | Click rate dropped from 52% → 17% over 6 months |
| Fig. 3 | `fig3_delivery_method.png`     | Section IV-C | Simulated phishing (89%) and gamification (86%) top-ranked |
| Fig. 4 | `fig4_security_incidents.png`  | Section IV-D | Incidents fell 67% from pre- to post-training period |
| Fig. 5 | `fig5_score_distribution.png`  | Section IV-E | High-risk employees reduced from 38% → 6% |

---

## Statistical Methods Used

| Method                | Applied To                              | Library        |
|-----------------------|-----------------------------------------|----------------|
| Paired-samples t-test | Pre vs. post scores (5 metrics)         | `scipy.stats`  |
| Cohen's d             | Effect size for each metric             | Manual formula |
| One-Way ANOVA         | Effectiveness across 5 training methods | `scipy.stats`  |
| Bonferroni correction | Post-hoc pairwise comparisons           | `scipy.stats`  |
| Gaussian KDE          | Smooth distribution curve in Fig. 5     | `scipy.stats`  |

Significance level: **α = 0.05** (as stated in Section III-D of the paper)

---

## Authors

| Name        | Email                         | Institution                        |
|-------------|-------------------------------|------------------------------------|
| Sujal       | sujal868.be22@chitkara.edu.in | Chitkara University, Punjab, India |
| Vidhi Anand | vidhi957.be22@chitkara.edu.in | Chitkara University, Punjab, India |

---

## Acknowledgements

The authors acknowledge the faculty of the Department of Computer Science and Engineering, Chitkara University Institute of Engineering and Technology, and the open-source communities behind Python, SciPy, Matplotlib, NumPy, and Gophish.
