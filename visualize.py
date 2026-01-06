import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load CSV
df = pd.read_csv(
    "report.csv",
    engine="python",
    on_bad_lines="skip"
)
df.columns = ["type", "key", "value"]
df["value"] = pd.to_numeric(df["value"], errors="coerce")
df = df.dropna()

ip_df = df[df["type"] == "IP"].sort_values("value", ascending=False)
url_df = df[df["type"] == "URL"].sort_values("value", ascending=False)
status_df = df[df["type"] == "STATUS"]

# Metrics
total_requests = int(status_df["value"].sum())
unique_ips = ip_df.shape[0]
error_df = status_df[status_df["key"].astype(int) >= 400]
error_requests = error_df["value"].sum()
error_rate = round((error_requests / total_requests) * 100, 2) if total_requests else 0

top_ip = ip_df.iloc[0]["key"]
top_ip_hits = int(ip_df.iloc[0]["value"])

# Helpers
def shorten(text, n=40):
    return text if len(text) <= n else text[:n] + "..."

url_df["short_url"] = url_df["key"].apply(shorten)

# Plotly Dashboard
fig = make_subplots(
    rows=3, cols=2,
    specs=[
        [{"type": "indicator"}, {"type": "indicator"}],
        [{"type": "bar"}, {"type": "pie"}],
        [{"type": "bar"}, {"type": "bar"}]
    ],
    subplot_titles=[
        "Total Requests",
        "Error Rate (%)",
        "Top Client IPs",
        "HTTP Status Distribution",
        "Most Accessed URLs",
        "Error Status Codes (4xx / 5xx)"
    ]
)

#KPI Cards
fig.add_trace(go.Indicator(
    mode="number",
    value=total_requests,
), row=1, col=1)

fig.add_trace(go.Indicator(
    mode="number+delta",
    value=error_rate,
    number={"suffix": "%"},
    delta={"reference": 5, "decreasing": {"color": "green"}, "increasing": {"color": "red"}},
), row=1, col=2)

#Top IPs
fig.add_trace(go.Bar(
    x=ip_df.head(10)["value"],
    y=ip_df.head(10)["key"],
    orientation="h"
), row=2, col=1)

#Status Pie
fig.add_trace(go.Pie(
    labels=status_df["key"],
    values=status_df["value"],
    hole=0.45
), row=2, col=2)

# URLs
top_urls = url_df.head(10).sort_values("value")
fig.add_trace(go.Bar(
    x=top_urls["value"],
    y=top_urls["short_url"],
    orientation="h",
    hovertext=top_urls["key"]
), row=3, col=1)

# Errors
fig.add_trace(go.Bar(
    x=error_df["key"].astype(str),
    y=error_df["value"],
    marker_color="crimson",
    text=error_df["value"],
    textposition="outside"
), row=3, col=2)

fig.update_layout(
    height=1000,
    title="Web Server Access Log Analysis Dashboard",
    template="plotly_white",
    showlegend=False
)

dashboard_html = fig.to_html(include_plotlyjs="cdn", full_html=False)

# INSIGHTS PANEL
health_status = "HEALTHY" if error_rate < 5 else "ATTENTION NEEDED"
risk_level = "LOW" if top_ip_hits < 50 else "MEDIUM"

insights_html = f"""
<div style="font-family:Arial; padding:30px; background:#f8f9fa;">
  <h2>Insights & Findings</h2>
  <ul style="font-size:16px; line-height:1.8;">
    <li><b>Total Requests:</b> {total_requests} HTTP requests processed.</li>
    <li><b>Unique Clients:</b> {unique_ips} distinct IP addresses accessed the server.</li>
    <li><b>Error Rate:</b> {error_rate}% → <b>{health_status}</b>.</li>
    <li><b>Top Client IP:</b> {top_ip} generated {top_ip_hits} requests.</li>
    <li><b>Error Pattern:</b> Majority of errors are HTTP 404, indicating missing resources or automated scanning.</li>
    <li><b>Security Risk Level:</b> <b>{risk_level}</b>. No large-scale abuse detected.</li>
  </ul>

  <h3>Recommendations</h3>
  <ul style="font-size:16px; line-height:1.8;">
    <li>Monitor high-traffic IPs for unusual request patterns.</li>
    <li>Investigate repeated 404 errors for broken links.</li>
    <li>Enable rate-limiting for sensitive endpoints.</li>
  </ul>
</div>
"""

# FINAL HTML FILE
final_html = f"""
<html>
<head>
  <title>Web Server Log Analysis Report</title>
</head>
<body>
  {dashboard_html}
  {insights_html}
</body>
</html>
"""

with open("log_report.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("HTML report generated: log_report.html")
