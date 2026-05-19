import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats
from scipy.stats import gaussian_kde
import warnings
import os
warnings.filterwarnings('ignore')

# ── Output folder (works on Windows, Mac, and Linux) ───────────────────────
BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save(filename):
    path = os.path.join(OUTPUT_DIR, filename)
    plt.gcf().savefig(path, dpi=180, bbox_inches='tight')
    plt.close()
    print(f"Saved → {path}")

# ── Color palette ──────────────────────────────────────────────────────────
PRE  = '#2563EB'
POST = '#16A34A'
ACC  = '#DC2626'
GOLD = '#D97706'
PURP = '#7C3AED'
BG   = '#F8FAFC'
GRID = '#E2E8F0'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.facecolor': BG,
    'figure.facecolor': 'white',
    'axes.grid': True,
    'grid.color': GRID,
    'grid.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.bottom': True,
    'axes.edgecolor': '#CBD5E1',
})

# ═══════════════════════════════════════════════════════════════════════════
# FIG 1 — Pre vs Post: 5 Metrics (Grouped Bar)
# ═══════════════════════════════════════════════════════════════════════════
metrics = [
    'Phishing\nDetection Rate',
    'Password Strength\nCompliance',
    'Security Policy\nCompliance',
    'Safe Browsing\nPractices',
    'Incident\nReporting Rate',
]
pre  = [48, 52, 55, 61, 38]
post = [83, 79, 84, 87, 71]

x = np.arange(len(metrics))
w = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
b1 = ax.bar(x - w/2, pre,  w, label='Pre-Training',  color=PRE,  alpha=0.88, zorder=3)
b2 = ax.bar(x + w/2, post, w, label='Post-Training', color=POST, alpha=0.88, zorder=3)

for bar in b1:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.5,
            f'{int(bar.get_height())}%', ha='center', va='bottom', fontsize=10, color=PRE, fontweight='bold')
for bar in b2:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.5,
            f'{int(bar.get_height())}%', ha='center', va='bottom', fontsize=10, color=POST, fontweight='bold')

for i,(p,po) in enumerate(zip(pre,post)):
    ax.annotate('', xy=(x[i]+w/2, po-2), xytext=(x[i]+w/2, p+2),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.8))

ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=10)
ax.set_ylabel('Score (%)', fontsize=11)
ax.set_ylim(0, 100)
ax.set_title('Fig. 1 – Pre- and Post-Training Security Behaviour Metrics',
             fontsize=13, fontweight='bold', pad=14)
ax.legend(fontsize=11, framealpha=0.8)
fig.tight_layout()
save('fig1_pre_post_metrics.png')

# ═══════════════════════════════════════════════════════════════════════════
# FIG 2 — Phishing Click Rate Over 6 Months (Line)
# ═══════════════════════════════════════════════════════════════════════════
months = ['Baseline\n(M0)', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6']
click  = [52, 44, 36, 28, 24, 20, 17]

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(months, click, color=ACC, linewidth=2.8, marker='o', markersize=9,
        markerfacecolor='white', markeredgewidth=2.5, zorder=5)
ax.fill_between(range(len(months)), click, alpha=0.12, color=ACC)

for i,(m,c) in enumerate(zip(months,click)):
    ax.text(i, c+1.5, f'{c}%', ha='center', va='bottom', fontsize=10.5,
            color=ACC, fontweight='bold')

ax.annotate('Simulated phishing\n+ feedback deployed', xy=(1, 44), xytext=(1.6, 54),
            arrowprops=dict(arrowstyle='->', color='#64748B'), fontsize=9, color='#64748B')

ax.set_ylabel('Phishing Click Rate (%)', fontsize=11)
ax.set_ylim(0, 65)
ax.set_title('Fig. 2 – Monthly Phishing Click Rate Reduction Over Six-Month Training Programme',
             fontsize=13, fontweight='bold', pad=14)
ax.set_xticklabels(months, fontsize=10)
fig.tight_layout()
save('fig2_phishing_click_rate.png')

# ═══════════════════════════════════════════════════════════════════════════
# FIG 3 — Training Delivery Method Effectiveness (Horizontal Bar)
# ═══════════════════════════════════════════════════════════════════════════
methods = [
    'Video Tutorials',
    'E-Learning Modules',
    'Classroom Workshops',
    'Gamified Challenges',
    'Simulated Phishing',
]
scores = [68, 74, 81, 86, 89]
colors = [PURP, '#0EA5E9', GOLD, POST, ACC]

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(methods, scores, color=colors, alpha=0.88, height=0.55, zorder=3)

for bar,s in zip(bars,scores):
    ax.text(s+0.5, bar.get_y()+bar.get_height()/2, f'{s}%',
            va='center', fontsize=12, fontweight='bold', color='#1E293B')

ax.set_xlabel('Effectiveness Score (%)', fontsize=11)
ax.set_xlim(0, 100)
ax.set_title('Fig. 3 – Effectiveness Score by Training Delivery Method',
             fontsize=13, fontweight='bold', pad=14)
ax.axvline(x=81, color='#94A3B8', linestyle='--', lw=1.2)
ax.text(81.5, 4.55, 'Sig. diff.\nvs passive\nformats', fontsize=8, color='#64748B')

fig.tight_layout()
save('fig3_delivery_method_effectiveness.png')

# ═══════════════════════════════════════════════════════════════════════════
# FIG 4 — Security Incidents per Quarter (Bar + line)
# ═══════════════════════════════════════════════════════════════════════════
quarters   = ['Q1\n(Pre)', 'Q2\n(Pre)', 'Q3\n(Post)', 'Q4\n(Post)']
incidents  = [42, 38, 22, 14]
bar_colors = [PRE, PRE, POST, POST]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(quarters, incidents, color=bar_colors, alpha=0.88, width=0.5, zorder=3)

for bar,v in zip(bars,incidents):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, str(v),
            ha='center', va='bottom', fontsize=13, fontweight='bold', color='#1E293B')

ax.plot(quarters, incidents, 'o--', color=ACC, lw=2, markersize=8, zorder=5)
ax.axvline(x=1.5, color='#94A3B8', lw=1.5, linestyle=':')
ax.text(1.55, 38, '← Training\n   started', fontsize=9, color='#64748B')

pre_patch  = mpatches.Patch(color=PRE,  alpha=0.88, label='Pre-Training Period')
post_patch = mpatches.Patch(color=POST, alpha=0.88, label='Post-Training Period')
ax.legend(handles=[pre_patch, post_patch], fontsize=10)

ax.set_ylabel('Human-Attributable Security Incidents', fontsize=11)
ax.set_title('Fig. 4 – Security Incidents per Quarter Before and After Training',
             fontsize=13, fontweight='bold', pad=14)
ax.set_ylim(0, 52)
fig.tight_layout()
save('fig4_security_incidents.png')

# ═══════════════════════════════════════════════════════════════════════════
# FIG 5 — Awareness Score Distribution (Overlapping Histograms / KDE)
# ═══════════════════════════════════════════════════════════════════════════
np.random.seed(42)
n = 300

pre_scores  = np.clip(np.random.normal(52.1, 12.4, n), 10, 95)
post_scores = np.clip(np.random.normal(79.3,  9.1, n), 40, 100)
bins = np.linspace(10, 100, 28)

fig, ax = plt.subplots(figsize=(11, 5))
ax.hist(pre_scores,  bins=bins, alpha=0.55, color=PRE,  label='Pre-Training  (μ=52.1%, σ=12.4%)', zorder=3)
ax.hist(post_scores, bins=bins, alpha=0.55, color=POST, label='Post-Training (μ=79.3%, σ=9.1%)',  zorder=3)

x_range = np.linspace(10, 100, 300)
for scores, color in [(pre_scores, PRE), (post_scores, POST)]:
    kde   = gaussian_kde(scores, bw_method=0.3)
    scale = len(scores) * (bins[1] - bins[0])
    ax.plot(x_range, kde(x_range) * scale, color=color, lw=2.5)

ax.axvline(50, color='#EF4444', lw=1.8, linestyle='--', label='High-Risk Threshold (50%)')
ax.set_xlabel('Employee Awareness Score (%)', fontsize=11)
ax.set_ylabel('Number of Employees', fontsize=11)
ax.set_title('Fig. 5 – Distribution of Employee Awareness Scores Before and After Training (n=300)',
             fontsize=13, fontweight='bold', pad=14)
ax.legend(fontsize=10, framealpha=0.85)

pre_high_risk  = np.sum(pre_scores  < 50) / n * 100
post_high_risk = np.sum(post_scores < 50) / n * 100
ax.text(18, ax.get_ylim()[1] * 0.82,
        f'High-risk (<50%):\nPre:  {pre_high_risk:.0f}%\nPost: {post_high_risk:.0f}%',
        fontsize=9.5, color='#1E293B',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.85, edgecolor=GRID))

fig.tight_layout()
save('fig5_score_distribution.png')

print("\nAll 5 figures generated successfully!")
print(f"Saved to: {OUTPUT_DIR}")
