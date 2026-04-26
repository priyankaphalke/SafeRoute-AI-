import streamlit as st
import folium
from streamlit_folium import st_folium
import time
import random
import math
import json
from datetime import datetime
import requests


def send_alert():
    url = "https://phalkepm.app.n8n.cloud/webhook-test/emergency-alert"

    data = {
        "location": "Pune",
        "risk": 85,
        "phone": 8010320616
    }

    requests.post(url, json=data)  

if st.button("🚨 Emergency Alert"):
    send_alert()
    st.success("Alert sent!")
    
# ─── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SafeRoute AI",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CUSTOM CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&family=Exo+2:wght@300;400;600;800&display=swap');

:root {
    --bg-primary: #0a0e1a;
    --bg-secondary: #0f1628;
    --bg-card: #131c2e;
    --bg-card-hover: #1a2540;
    --accent-blue: #00d4ff;
    --accent-cyan: #00ffcc;
    --accent-red: #ff3b5c;
    --accent-orange: #ff8c00;
    --accent-green: #00ff88;
    --accent-purple: #8b5cf6;
    --text-primary: #e8f0fe;
    --text-secondary: #8899aa;
    --text-muted: #4a5568;
    --border-subtle: rgba(0, 212, 255, 0.12);
    --border-glow: rgba(0, 212, 255, 0.4);
    --shadow-card: 0 4px 24px rgba(0, 0, 0, 0.4);
    --glow-blue: 0 0 20px rgba(0, 212, 255, 0.3);
    --glow-red: 0 0 20px rgba(255, 59, 92, 0.4);
    --glow-green: 0 0 20px rgba(0, 255, 136, 0.3);
}

html, body, [class*="css"] {
    font-family: 'Exo 2', sans-serif;
    background-color: var(--bg-primary);
    color: var(--text-primary);
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem; padding-bottom: 2rem; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0e1a 0%, #0d1422 100%);
    border-right: 1px solid var(--border-subtle);
}
section[data-testid="stSidebar"] .block-container { padding-top: 1.5rem; }

/* Headers */
h1, h2, h3 { font-family: 'Rajdhani', sans-serif; font-weight: 700; }
h1 { font-size: 2.6rem !important; letter-spacing: 2px; }
h2 { font-size: 1.5rem !important; letter-spacing: 1px; }

/* Cards */
.sr-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-card);
    transition: all 0.3s ease;
}
.sr-card:hover {
    border-color: var(--border-glow);
    box-shadow: var(--shadow-card), var(--glow-blue);
}

/* Hero Banner */
.hero-banner {
    background: linear-gradient(135deg, #0f1628 0%, #131c2e 40%, #0d1a33 100%);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 40%, rgba(0, 212, 255, 0.06) 0%, transparent 50%),
                radial-gradient(circle at 70% 60%, rgba(0, 255, 136, 0.04) 0%, transparent 50%);
    pointer-events: none;
}
.hero-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--accent-cyan) 0%, var(--accent-blue) 50%, var(--accent-purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 3px;
    margin: 0;
    line-height: 1.1;
}
.hero-subtitle {
    color: var(--text-secondary);
    font-size: 0.95rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 0.4rem;
    font-family: 'Share Tech Mono', monospace;
}
.hero-badge {
    display: inline-block;
    background: rgba(0, 212, 255, 0.1);
    border: 1px solid rgba(0, 212, 255, 0.3);
    color: var(--accent-cyan);
    padding: 0.2rem 0.8rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-family: 'Share Tech Mono', monospace;
    letter-spacing: 1px;
    margin-top: 0.8rem;
}

/* Metric Cards */
.metric-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.metric-value {
    font-family: 'Share Tech Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1;
}
.metric-label {
    color: var(--text-secondary);
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 0.4rem;
}
.metric-card.danger { border-color: rgba(255, 59, 92, 0.4); }
.metric-card.danger .metric-value { color: var(--accent-red); }
.metric-card.warning { border-color: rgba(255, 140, 0, 0.4); }
.metric-card.warning .metric-value { color: var(--accent-orange); }
.metric-card.safe { border-color: rgba(0, 255, 136, 0.4); }
.metric-card.safe .metric-value { color: var(--accent-green); }
.metric-card.info { border-color: rgba(0, 212, 255, 0.4); }
.metric-card.info .metric-value { color: var(--accent-blue); }

/* Route Cards */
.route-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 0.8rem;
    cursor: pointer;
    transition: all 0.25s ease;
    position: relative;
}
.route-card.recommended {
    border-color: var(--accent-green);
    box-shadow: var(--glow-green);
    background: linear-gradient(135deg, #131c2e 0%, #0d2219 100%);
}
.route-card.fast { border-color: rgba(255, 59, 92, 0.5); }
.route-card.balanced { border-color: rgba(255, 140, 0, 0.5); }
.route-badge {
    position: absolute;
    top: 0.8rem;
    right: 1rem;
    font-size: 0.65rem;
    font-family: 'Share Tech Mono', monospace;
    letter-spacing: 1px;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    text-transform: uppercase;
}
.badge-recommended { background: rgba(0, 255, 136, 0.15); color: var(--accent-green); border: 1px solid rgba(0, 255, 136, 0.3); }
.badge-fast { background: rgba(255, 59, 92, 0.15); color: var(--accent-red); border: 1px solid rgba(255, 59, 92, 0.3); }
.badge-balanced { background: rgba(255, 140, 0, 0.15); color: var(--accent-orange); border: 1px solid rgba(255, 140, 0, 0.3); }

/* Alert Cards */
.alert-high {
    background: rgba(255, 59, 92, 0.08);
    border: 1px solid rgba(255, 59, 92, 0.3);
    border-left: 3px solid var(--accent-red);
    border-radius: 8px;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.6rem;
    color: #ffb3be;
    font-size: 0.88rem;
}
.alert-medium {
    background: rgba(255, 140, 0, 0.08);
    border: 1px solid rgba(255, 140, 0, 0.3);
    border-left: 3px solid var(--accent-orange);
    border-radius: 8px;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.6rem;
    color: #ffd9a0;
    font-size: 0.88rem;
}
.alert-low {
    background: rgba(0, 255, 136, 0.06);
    border: 1px solid rgba(0, 255, 136, 0.25);
    border-left: 3px solid var(--accent-green);
    border-radius: 8px;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.6rem;
    color: #a0ffd5;
    font-size: 0.88rem;
}

/* Scanning animation */
.scan-text {
    font-family: 'Share Tech Mono', monospace;
    color: var(--accent-cyan);
    font-size: 0.85rem;
    padding: 0.4rem 0;
}

/* Risk Bar */
.risk-bar-container {
    background: rgba(255,255,255,0.05);
    border-radius: 6px;
    height: 8px;
    overflow: hidden;
    margin-top: 0.5rem;
}
.risk-bar-fill {
    height: 100%;
    border-radius: 6px;
    transition: width 1s ease;
}

/* Section Divider */
.section-divider {
    border: none;
    border-top: 1px solid var(--border-subtle);
    margin: 1.5rem 0;
}

/* Sidebar section header */
.sidebar-section {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--accent-cyan);
    border-bottom: 1px solid var(--border-subtle);
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
}

/* Emergency Button */
.emergency-pulse {
    animation: pulse-red 2s infinite;
}
@keyframes pulse-red {
    0%, 100% { box-shadow: 0 0 0 0 rgba(255, 59, 92, 0.6); }
    50% { box-shadow: 0 0 0 12px rgba(255, 59, 92, 0); }
}

/* Status indicators */
.status-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 6px;
}
.status-live { background: var(--accent-green); box-shadow: 0 0 6px var(--accent-green); animation: blink 1.5s infinite; }
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

/* Streamlit overrides */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.15), rgba(0, 255, 204, 0.1));
    border: 1px solid rgba(0, 212, 255, 0.4);
    color: var(--accent-cyan);
    font-family: 'Rajdhani', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 1.5px;
    padding: 0.6rem 1.5rem;
    border-radius: 8px;
    text-transform: uppercase;
    transition: all 0.25s ease;
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.25), rgba(0, 255, 204, 0.18));
    border-color: var(--accent-cyan);
    box-shadow: var(--glow-blue);
    transform: translateY(-1px);
}
.stSelectbox label, .stTextInput label, .stRadio label {
    color: var(--text-secondary) !important;
    font-size: 0.8rem !important;
    font-family: 'Share Tech Mono', monospace !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}
div[data-baseweb="select"] > div {
    background: var(--bg-card) !important;
    border-color: var(--border-subtle) !important;
    color: var(--text-primary) !important;
}
.stTextInput > div > div > input {
    background: var(--bg-card) !important;
    border-color: var(--border-subtle) !important;
    color: var(--text-primary) !important;
    font-family: 'Exo 2', sans-serif !important;
}
.stRadio > div > div > label {
    color: var(--text-primary) !important;
    font-size: 0.9rem !important;
    font-family: 'Exo 2', sans-serif !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
}
.stSlider > div > div > div { background: var(--accent-blue) !important; }

/* Weather widget */
.weather-widget {
    background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(139,92,246,0.06));
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.8rem;
}

/* Coordinate display */
.coord-display {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.82rem;
    color: var(--accent-cyan);
    background: rgba(0, 212, 255, 0.06);
    border: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 6px;
    padding: 0.5rem 1rem;
    display: inline-block;
    letter-spacing: 0.5px;
}

/* Tabs override */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-secondary) !important;
    border-bottom: 1px solid var(--border-subtle) !important;
    gap: 0.5rem;
}
.stTabs [data-baseweb="tab"] {
    color: var(--text-secondary) !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 1px !important;
}
.stTabs [aria-selected="true"] {
    color: var(--accent-cyan) !important;
    border-bottom: 2px solid var(--accent-cyan) !important;
}
</style>
""", unsafe_allow_html=True)

# ─── DATA ENGINE ─────────────────────────────────────────────────────────────────
CITY_ZONES = {
    "Mumbai": {
        "center": (19.0760, 72.8777),
        "zones": [
            {"name": "Dharavi", "lat": 19.0430, "lon": 72.8540, "cctv": "Low", "incident_score": 7.5, "lighting": "Low", "crowd": "High"},
            {"name": "Kurla", "lat": 19.0726, "lon": 72.8793, "cctv": "Medium", "incident_score": 6.0, "lighting": "Medium", "crowd": "High"},
            {"name": "Govandi", "lat": 19.0590, "lon": 72.9180, "cctv": "Low", "incident_score": 8.0, "lighting": "Low", "crowd": "Low"},
            {"name": "Bandra", "lat": 19.0596, "lon": 72.8295, "cctv": "High", "incident_score": 2.5, "lighting": "High", "crowd": "Medium"},
            {"name": "Worli", "lat": 19.0176, "lon": 72.8146, "cctv": "High", "incident_score": 2.0, "lighting": "High", "crowd": "Medium"},
            {"name": "Dadar", "lat": 19.0178, "lon": 72.8478, "cctv": "Medium", "incident_score": 4.5, "lighting": "Medium", "crowd": "High"},
            {"name": "Malad", "lat": 19.1874, "lon": 72.8489, "cctv": "Medium", "incident_score": 5.0, "lighting": "Medium", "crowd": "Medium"},
            {"name": "Andheri East", "lat": 19.1136, "lon": 72.8697, "cctv": "Medium", "incident_score": 4.0, "lighting": "Medium", "crowd": "High"},
            {"name": "Colaba", "lat": 18.9067, "lon": 72.8147, "cctv": "High", "incident_score": 3.0, "lighting": "High", "crowd": "High"},
            {"name": "Vikhroli", "lat": 19.1048, "lon": 72.9244, "cctv": "Low", "incident_score": 6.5, "lighting": "Low", "crowd": "Medium"},
        ]
    },
    "Delhi": {
        "center": (28.6139, 77.2090),
        "zones": [
            {"name": "Paharganj", "lat": 28.6448, "lon": 77.2167, "cctv": "Medium", "incident_score": 7.0, "lighting": "Low", "crowd": "High"},
            {"name": "Sadar Bazaar", "lat": 28.6576, "lon": 77.2126, "cctv": "Low", "incident_score": 7.5, "lighting": "Low", "crowd": "High"},
            {"name": "Connaught Place", "lat": 28.6315, "lon": 77.2167, "cctv": "High", "incident_score": 2.5, "lighting": "High", "crowd": "High"},
            {"name": "Lajpat Nagar", "lat": 28.5700, "lon": 77.2418, "cctv": "Medium", "incident_score": 4.5, "lighting": "Medium", "crowd": "High"},
            {"name": "Rohini", "lat": 28.7495, "lon": 77.0788, "cctv": "Medium", "incident_score": 5.5, "lighting": "Medium", "crowd": "Medium"},
            {"name": "Dwarka", "lat": 28.5921, "lon": 77.0460, "cctv": "High", "incident_score": 3.0, "lighting": "High", "crowd": "Medium"},
            {"name": "Okhla", "lat": 28.5414, "lon": 77.2867, "cctv": "Low", "incident_score": 7.8, "lighting": "Low", "crowd": "Low"},
            {"name": "Karol Bagh", "lat": 28.6518, "lon": 77.1901, "cctv": "Medium", "incident_score": 5.0, "lighting": "Medium", "crowd": "High"},
        ]
    },
    "Bengaluru": {
        "center": (12.9716, 77.5946),
        "zones": [
            {"name": "Whitefield", "lat": 12.9698, "lon": 77.7500, "cctv": "High", "incident_score": 3.5, "lighting": "High", "crowd": "Medium"},
            {"name": "Marathahalli", "lat": 12.9591, "lon": 77.6972, "cctv": "Medium", "incident_score": 4.5, "lighting": "Medium", "crowd": "High"},
            {"name": "BTM Layout", "lat": 12.9165, "lon": 77.6101, "cctv": "Medium", "incident_score": 5.0, "lighting": "Medium", "crowd": "High"},
            {"name": "Shivajinagar", "lat": 12.9855, "lon": 77.5995, "cctv": "High", "incident_score": 2.5, "lighting": "High", "crowd": "High"},
            {"name": "Koramangala", "lat": 12.9279, "lon": 77.6271, "cctv": "High", "incident_score": 2.0, "lighting": "High", "crowd": "High"},
            {"name": "Yelahanka", "lat": 13.1005, "lon": 77.5940, "cctv": "Low", "incident_score": 6.5, "lighting": "Low", "crowd": "Low"},
        ]
    },
    "Pune": {
        "center": (18.5204, 73.8567),
        "zones": [
            {"name": "Koregaon Park", "lat": 18.5362, "lon": 73.8940, "cctv": "High", "incident_score": 2.5, "lighting": "High", "crowd": "Medium"},
            {"name": "Khadki", "lat": 18.5653, "lon": 73.8496, "cctv": "Medium", "incident_score": 5.5, "lighting": "Medium", "crowd": "Medium"},
            {"name": "Yerwada", "lat": 18.5508, "lon": 73.9032, "cctv": "Low", "incident_score": 7.0, "lighting": "Low", "crowd": "Low"},
            {"name": "Shivajinagar", "lat": 18.5308, "lon": 73.8475, "cctv": "High", "incident_score": 3.0, "lighting": "High", "crowd": "High"},
            {"name": "Hadapsar", "lat": 18.5018, "lon": 73.9260, "cctv": "Medium", "incident_score": 5.0, "lighting": "Medium", "crowd": "Medium"},
        ]
    }
}

# ─── RISK ENGINE ─────────────────────────────────────────────────────────────────
def calculate_risk_score(zone: dict, time_of_day: str, user_type: str, mode: str) -> int:
    score = zone["incident_score"] * 10
    if time_of_day == "Night": score += 15
    if zone["cctv"] == "Low": score += 10
    if zone["cctv"] == "High": score -= 10
    if user_type == "Woman": score += 10
    if mode == "Fast": score += 5
    if mode == "Safety First": score -= 10
    if zone["lighting"] == "Low": score += 8
    if zone["crowd"] == "Low" and time_of_day == "Night": score += 7
    return max(0, min(100, int(score)))

def risk_color(score: int) -> str:
    if score >= 65: return "#ff3b5c"
    elif score >= 35: return "#ff8c00"
    else: return "#00ff88"

def risk_label(score: int) -> str:
    if score >= 65: return "HIGH RISK"
    elif score >= 35: return "MODERATE"
    else: return "SAFE"

def risk_class(score: int) -> str:
    if score >= 65: return "danger"
    elif score >= 35: return "warning"
    else: return "safe"

# ─── ROUTE ENGINE ────────────────────────────────────────────────────────────────
def generate_routes(start: str, destination: str, city: str, time_of_day: str, user_type: str) -> list:
    zones = CITY_ZONES[city]["zones"]
    
    def avg_risk(zone_names):
        selected = [z for z in zones if any(n in z["name"] for n in zone_names)]
        if not selected:
            selected = random.sample(zones, min(3, len(zones)))
        risks = [calculate_risk_score(z, time_of_day, user_type, "Balanced") for z in selected]
        return int(sum(risks) / len(risks)) if risks else 50

    r = random.Random(hash(start + destination + city))
    base_dist = r.uniform(3.5, 18.0)

    route_a_risk = min(95, avg_risk([z["name"] for z in sorted(zones, key=lambda x: x["incident_score"], reverse=True)[:3]]) + r.randint(-5, 5))
    route_b_risk = min(80, avg_risk([z["name"] for z in sorted(zones, key=lambda x: x["incident_score"])][2:5]) + r.randint(-5, 5))
    route_c_risk = max(5, avg_risk([z["name"] for z in sorted(zones, key=lambda x: x["incident_score"])[:3]]) + r.randint(-5, 5))

    routes = [
        {
            "id": "A",
            "label": "Route A — Fastest",
            "type": "fast",
            "distance": round(base_dist * 0.82, 1),
            "duration": f"{int(base_dist * 0.82 * 3.2)} min",
            "risk": route_a_risk,
            "via": "Highway / Main Road",
            "cctv_coverage": "Low–Medium",
            "checkpoints": ["Busy junction", "Market area", "Industrial stretch"],
        },
        {
            "id": "B",
            "label": "Route B — Balanced",
            "type": "balanced",
            "distance": round(base_dist, 1),
            "duration": f"{int(base_dist * 3.8)} min",
            "risk": route_b_risk,
            "via": "City Roads + Partial Highway",
            "cctv_coverage": "Medium",
            "checkpoints": ["Residential area", "Commercial zone", "Lit boulevard"],
        },
        {
            "id": "C",
            "label": "Route C — Safest",
            "type": "safe",
            "distance": round(base_dist * 1.22, 1),
            "duration": f"{int(base_dist * 1.22 * 4.5)} min",
            "risk": route_c_risk,
            "via": "Inner Roads + Safe Zones",
            "cctv_coverage": "High",
            "checkpoints": ["Police outpost nearby", "Well-lit road", "Residential corridor"],
        },
    ]
    return routes

# ─── MAP BUILDER ─────────────────────────────────────────────────────────────────
def build_map(city: str, time_of_day: str, user_type: str, mode: str, dest_name: str = ""):
    data = CITY_ZONES[city]
    center = data["center"]
    zones = data["zones"]

    m = folium.Map(
        location=center,
        zoom_start=12,
        tiles="CartoDB dark_matter",
        prefer_canvas=True,
    )

    # User location marker
    folium.Marker(
        location=center,
        popup=folium.Popup(f"<b>📍 You are here</b><br>{city}", max_width=180),
        tooltip="Your Location",
        icon=folium.Icon(color="blue", icon="user", prefix="fa"),
    ).add_to(m)

    # Destination marker (approximate offset)
    if dest_name:
        dest_offset = (center[0] + random.uniform(0.02, 0.06), center[1] + random.uniform(0.03, 0.07))
        folium.Marker(
            location=dest_offset,
            popup=folium.Popup(f"<b>🎯 Destination</b><br>{dest_name}", max_width=180),
            tooltip=f"Destination: {dest_name}",
            icon=folium.Icon(color="red", icon="flag", prefix="fa"),
        ).add_to(m)

    # Zone circles
    for zone in zones:
        score = calculate_risk_score(zone, time_of_day, user_type, mode)
        color = risk_color(score)
        label = risk_label(score)

        folium.CircleMarker(
            location=(zone["lat"], zone["lon"]),
            radius=max(18, score // 3.5),
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.28,
            weight=1.5,
            popup=folium.Popup(
                f"""<div style='font-family:monospace;font-size:12px;'>
                <b>{zone['name']}</b><br>
                ⚠️ Risk: <b>{score}/100</b> ({label})<br>
                📹 CCTV: {zone['cctv']}<br>
                💡 Lighting: {zone['lighting']}<br>
                👥 Crowd: {zone['crowd']}<br>
                📊 Incidents: {zone['incident_score']}/10
                </div>""",
                max_width=200,
            ),
            tooltip=f"{zone['name']}: {score}/100 — {label}",
        ).add_to(m)

        # Risk label
        folium.Marker(
            location=(zone["lat"], zone["lon"]),
            icon=folium.DivIcon(
                html=f'<div style="font-size:9px;font-weight:700;color:{color};font-family:monospace;white-space:nowrap;">{zone["name"][:12]}</div>',
                icon_size=(100, 20),
                icon_anchor=(50, -10),
            )
        ).add_to(m)

    # Legend
    legend_html = """
    <div style="position:fixed;bottom:30px;left:15px;background:rgba(10,14,26,0.92);
         border:1px solid rgba(0,212,255,0.3);border-radius:10px;padding:12px 16px;
         font-family:monospace;font-size:11px;color:#e8f0fe;z-index:999;backdrop-filter:blur(8px);">
        <div style="margin-bottom:8px;font-weight:700;color:#00d4ff;letter-spacing:1px;">RISK LEGEND</div>
        <div><span style="color:#ff3b5c">●</span> High Risk (65–100)</div>
        <div><span style="color:#ff8c00">●</span> Moderate (35–64)</div>
        <div><span style="color:#00ff88">●</span> Safe (0–34)</div>
        <div style="margin-top:8px;color:#8899aa">Click circles for details</div>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    return m

# ─── ALERT ENGINE ────────────────────────────────────────────────────────────────
def generate_alerts(city: str, time_of_day: str, user_type: str) -> list:
    zones = CITY_ZONES[city]["zones"]
    alerts = []
    high_zones = [z for z in zones if z["incident_score"] >= 6.5]
    medium_zones = [z for z in zones if 4.0 <= z["incident_score"] < 6.5]

    r = random.Random(hash(city + time_of_day))
    distances = [120, 200, 350, 500, 750]

    for zone in high_zones[:2]:
        d = r.choice(distances)
        msgs = [
            f"⚠️ {d}m ahead: Low CCTV + {zone['lighting']} lighting in {zone['name']}",
            f"🔴 Entering high-risk corridor near {zone['name']} — exercise extreme caution",
        ]
        if time_of_day == "Night":
            msgs.append(f"🌙 Night alert: Poorly lit stretch near {zone['name']}")
        alerts.append({"level": "high", "msg": r.choice(msgs)})

    if user_type == "Woman":
        alerts.append({"level": "high", "msg": "👩 Women Safety Alert: Isolated zone detected on preferred path"})
        alerts.append({"level": "high", "msg": "👩 Recommendation: Prefer Route C — maximum CCTV coverage"})

    for zone in medium_zones[:2]:
        d = r.choice(distances)
        alerts.append({"level": "medium", "msg": f"🟡 {d}m: Moderate crowd dispersal zone — stay alert near {zone['name']}"})

    alerts.append({"level": "low", "msg": "✅ Police patrol reported active on Route C corridor"})
    alerts.append({"level": "low", "msg": "📡 Emergency response station 1.2 km from your path"})

    return alerts[:7]

# ─── SAFETY TIPS ─────────────────────────────────────────────────────────────────
def get_safety_tips(avg_risk: int, time_of_day: str, user_type: str) -> list:
    tips = []
    if avg_risk >= 65:
        tips += [
            "🚨 Share your live location with emergency contacts before starting",
            "🔦 Carry a charged phone + portable power bank",
            "🚕 Consider cab/auto instead of walking this route",
            "👥 Travel in groups whenever possible",
        ]
    elif avg_risk >= 35:
        tips += [
            "📱 Keep emergency numbers saved and accessible",
            "💡 Stick to well-lit roads and busy areas",
            "⏰ Avoid unnecessary detours or stops",
        ]
    else:
        tips += [
            "✅ Route appears relatively safe — stay aware of surroundings",
            "📍 Periodically share location with a trusted contact",
        ]

    if time_of_day == "Night":
        tips.append("🌙 Night travel: prefer busy, lit roads over shortcuts")
    if user_type == "Woman":
        tips.append("🛡 Keep Kavach/Himmat app or equivalent safety app active")
        tips.append("📞 Inform a contact before boarding public transport")
    if user_type == "Student":
        tips.append("🎒 Keep college emergency helpline on speed dial")

    return tips

# ─── SESSION STATE INIT ──────────────────────────────────────────────────────────
def init_session():
    defaults = {
        "user_name": "",
        "user_phone": "",
        "emergency_contact_1": "",
        "emergency_contact_2": "",
        "emergency_contact_3": "",
        "current_lat": 19.0760,
        "current_lon": 72.8777,
        "location_detected": False,
        "analysis_done": False,
        "routes": [],
        "alerts": [],
        "avg_risk": 0,
        "selected_city": "Mumbai",
        "emergency_sent": False,
        "weather_data": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()

# ─── SIDEBAR ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="hero-title" style="font-size:1.6rem;">🛡 SafeRoute AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle" style="font-size:0.65rem;">ADAPTIVE SAFETY NAVIGATION</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown('<div class="sidebar-section">👤 USER PROFILE</div>', unsafe_allow_html=True)
    st.session_state.user_name = st.text_input("Full Name", value=st.session_state.user_name, placeholder="Enter your name")
    st.session_state.user_phone = st.text_input("Phone Number", value=st.session_state.user_phone, placeholder="+91 XXXXX XXXXX")

    st.markdown('<div class="sidebar-section">🚨 EMERGENCY CONTACTS</div>', unsafe_allow_html=True)
    st.session_state.emergency_contact_1 = st.text_input("Contact 1", value=st.session_state.emergency_contact_1, placeholder="Name — Phone")
    st.session_state.emergency_contact_2 = st.text_input("Contact 2", value=st.session_state.emergency_contact_2, placeholder="Name — Phone")
    st.session_state.emergency_contact_3 = st.text_input("Contact 3", value=st.session_state.emergency_contact_3, placeholder="Name — Phone")

    st.markdown("---")
    st.markdown('<div class="sidebar-section">📍 CURRENT LOCATION</div>', unsafe_allow_html=True)

    if st.button("📍 Detect My Location"):
        with st.spinner("Detecting..."):
            try:
                resp = requests.get("https://ipapi.co/json/", timeout=5)
                if resp.status_code == 200:
                    data = resp.json()
                    st.session_state.current_lat = data.get("latitude", 19.0760)
                    st.session_state.current_lon = data.get("longitude", 72.8777)
                    st.session_state.location_detected = True
                    detected_city = data.get("city", "Mumbai")
                    for city in CITY_ZONES:
                        if city.lower() in detected_city.lower():
                            st.session_state.selected_city = city
                    st.success(f"📍 {data.get('city', 'Location detected')}")
                else:
                    raise Exception("API error")
            except:
                st.session_state.current_lat = 19.0760
                st.session_state.current_lon = 72.8777
                st.session_state.location_detected = True
                st.info("📍 Using default: Mumbai")

    if st.session_state.location_detected:
        st.markdown(f'<div class="coord-display">📡 {st.session_state.current_lat:.4f}°N, {st.session_state.current_lon:.4f}°E</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Emergency SOS
    st.markdown('<div class="sidebar-section">🚨 EMERGENCY SOS</div>', unsafe_allow_html=True)
    if st.button("🚨 SEND EMERGENCY ALERT", key="sos_btn"):
        st.session_state.emergency_sent = True

    if st.session_state.emergency_sent:
        contacts = [c for c in [st.session_state.emergency_contact_1,
                                  st.session_state.emergency_contact_2,
                                  st.session_state.emergency_contact_3] if c.strip()]
        name = st.session_state.user_name or "Anonymous"
        st.markdown(f"""
        <div style="background:rgba(255,59,92,0.12);border:1px solid rgba(255,59,92,0.4);
             border-radius:8px;padding:0.9rem;margin-top:0.5rem;">
            <div style="color:#ff3b5c;font-weight:700;font-size:0.8rem;letter-spacing:1px;">🚨 ALERT DISPATCHED</div>
            <div style="color:#ffb3be;font-size:0.78rem;margin-top:0.4rem;">
                <b>User:</b> {name}<br>
                <b>Location:</b> {st.session_state.current_lat:.4f}, {st.session_state.current_lon:.4f}<br>
                <b>Contacts Notified:</b> {len(contacts) if contacts else 0}<br>
                <b>Time:</b> {datetime.now().strftime('%H:%M:%S')}
            </div>
        </div>
        """, unsafe_allow_html=True)
        if contacts:
            for c in contacts:
                st.markdown(f'<div style="color:#8899aa;font-size:0.75rem;padding:0.2rem 0;">✓ {c}</div>', unsafe_allow_html=True)


# ─── MAIN CONTENT ────────────────────────────────────────────────────────────────
# Hero Banner
st.markdown("""
<div class="hero-banner">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;">
        <div>
            <div class="hero-title">SAFEROUTE AI</div>
            <div class="hero-subtitle">Real-Time Adaptive Safety Navigation System</div>
            <div class="hero-badge"><span class="status-dot status-live"></span>LIVE INTELLIGENCE ACTIVE</div>
        </div>
        <div style="text-align:right;color:#8899aa;font-size:0.8rem;font-family:'Share Tech Mono',monospace;">
            <div>🕒 {}</div>
            <div style="margin-top:0.3rem;">📡 System Online</div>
            <div style="margin-top:0.3rem;color:#00ff88;">✓ AI Engine Ready</div>
        </div>
    </div>
</div>
""".format(datetime.now().strftime("%d %b %Y  %H:%M")), unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Navigation & Analysis", "🗺 Safety Map", "🔔 Alerts & Tips", "ℹ System Info"])

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 1 — NAVIGATION & ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════════
with tab1:
    col_left, col_right = st.columns([1, 1.15], gap="large")

    with col_left:
        st.markdown('<div class="sr-card">', unsafe_allow_html=True)
        st.markdown("### 📍 Navigation Input")

        city = st.selectbox("🏙 Select City", list(CITY_ZONES.keys()), index=list(CITY_ZONES.keys()).index(st.session_state.selected_city))
        st.session_state.selected_city = city

        start = st.text_input("🚀 Start Location", placeholder=f"e.g. {CITY_ZONES[city]['zones'][3]['name']}")
        destination = st.text_input("🎯 Destination", placeholder=f"e.g. {CITY_ZONES[city]['zones'][0]['name']}")

        col_t, col_u = st.columns(2)
        with col_t:
            time_of_day = st.selectbox("🕐 Time", ["Day", "Night"])
        with col_u:
            user_type = st.selectbox("👤 Profile", ["Traveler", "Student", "Woman"])

        mode = st.radio("🛡 Safety Mode", ["Fast", "Balanced", "Safety First"], index=1, horizontal=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🔍 ANALYZE ROUTE", key="analyze_btn"):
            if not start or not destination:
                st.warning("⚠️ Please enter both Start and Destination.")
            else:
                progress_bar = st.progress(0)
                status_area = st.empty()

                steps = [
                    (15, "📡 Fetching live safety data from city sensors..."),
                    (30, "📹 Evaluating CCTV coverage across route segments..."),
                    (50, "📊 Analyzing historical incident patterns..."),
                    (65, "🌐 Cross-referencing crowd density data..."),
                    (80, "🧠 AI risk model computing optimal paths..."),
                    (92, "🛡 Applying user safety profile weights..."),
                    (100, "✅ Analysis complete — routes generated"),
                ]
                for prog, msg in steps:
                    progress_bar.progress(prog)
                    status_area.markdown(f'<div class="scan-text">› {msg}</div>', unsafe_allow_html=True)
                    time.sleep(0.45)

                progress_bar.empty()
                status_area.empty()

                zones = CITY_ZONES[city]["zones"]
                zone_risks = [calculate_risk_score(z, time_of_day, user_type, mode) for z in zones]
                st.session_state.avg_risk = int(sum(zone_risks) / len(zone_risks))
                st.session_state.routes = generate_routes(start, destination, city, time_of_day, user_type)
                st.session_state.alerts = generate_alerts(city, time_of_day, user_type)
                st.session_state.analysis_done = True
                st.session_state.emergency_sent = False
                st.rerun()

    with col_right:
        if st.session_state.analysis_done:
            # Risk Metrics
            zones = CITY_ZONES[city]["zones"]
            zone_risks = [calculate_risk_score(z, time_of_day, user_type, mode) for z in zones]
            high_count = sum(1 for r in zone_risks if r >= 65)
            med_count = sum(1 for r in zone_risks if 35 <= r < 65)
            safe_count = sum(1 for r in zone_risks if r < 35)
            avg = st.session_state.avg_risk

            st.markdown("### 📊 Risk Intelligence")
            mc1, mc2, mc3, mc4 = st.columns(4)
            rc = risk_class(avg)
            with mc1:
                st.markdown(f'<div class="metric-card {rc}"><div class="metric-value">{avg}</div><div class="metric-label">Avg Risk Score</div></div>', unsafe_allow_html=True)
            with mc2:
                st.markdown(f'<div class="metric-card danger"><div class="metric-value">{high_count}</div><div class="metric-label">High Risk Zones</div></div>', unsafe_allow_html=True)
            with mc3:
                st.markdown(f'<div class="metric-card warning"><div class="metric-value">{med_count}</div><div class="metric-label">Moderate Zones</div></div>', unsafe_allow_html=True)
            with mc4:
                st.markdown(f'<div class="metric-card safe"><div class="metric-value">{safe_count}</div><div class="metric-label">Safe Zones</div></div>', unsafe_allow_html=True)

            # Risk bar
            color = risk_color(avg)
            st.markdown(f"""
            <div style="margin:0.8rem 0 1.2rem;">
                <div style="display:flex;justify-content:space-between;font-size:0.75rem;color:#8899aa;font-family:'Share Tech Mono',monospace;margin-bottom:4px;">
                    <span>CITY RISK LEVEL</span>
                    <span style="color:{color};">{risk_label(avg)}</span>
                </div>
                <div class="risk-bar-container">
                    <div class="risk-bar-fill" style="width:{avg}%;background:linear-gradient(90deg,{color}88,{color});"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Routes
            st.markdown("### 🗺 Route Options")
            routes = st.session_state.routes
            rec_route = min(routes, key=lambda r: r["risk"])

            for route in routes:
                is_rec = route["id"] == rec_route["id"]
                card_class = "route-card recommended" if is_rec else f"route-card {route['type']}"
                badge_class = "badge-recommended" if is_rec else ("badge-fast" if route["type"] == "fast" else "badge-balanced")
                badge_text = "★ RECOMMENDED" if is_rec else route["type"].upper()
                risk_col = risk_color(route["risk"])
                risk_lbl = risk_label(route["risk"])

                st.markdown(f"""
                <div class="{card_class}">
                    <span class="route-badge {badge_class}">{badge_text}</span>
                    <div style="font-family:'Rajdhani',sans-serif;font-size:1.1rem;font-weight:700;margin-bottom:0.6rem;">{route['label']}</div>
                    <div style="display:flex;gap:1.5rem;flex-wrap:wrap;">
                        <div><span style="color:#8899aa;font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;">Distance</span><br><span style="font-family:'Share Tech Mono',monospace;color:#e8f0fe;">{route['distance']} km</span></div>
                        <div><span style="color:#8899aa;font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;">Duration</span><br><span style="font-family:'Share Tech Mono',monospace;color:#e8f0fe;">{route['duration']}</span></div>
                        <div><span style="color:#8899aa;font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;">Risk Score</span><br><span style="font-family:'Share Tech Mono',monospace;color:{risk_col};">{route['risk']}/100 — {risk_lbl}</span></div>
                        <div><span style="color:#8899aa;font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;">CCTV</span><br><span style="font-family:'Share Tech Mono',monospace;color:#e8f0fe;">{route['cctv_coverage']}</span></div>
                    </div>
                    <div style="margin-top:0.7rem;font-size:0.78rem;color:#8899aa;">
                        <span>Via: {route['via']}</span>
                        <span style="margin-left:1rem;">Checkpoints: {' → '.join(route['checkpoints'])}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="sr-card" style="text-align:center;padding:3rem 2rem;">
                <div style="font-size:3rem;margin-bottom:1rem;">🛡</div>
                <div style="font-family:'Rajdhani',sans-serif;font-size:1.3rem;font-weight:700;color:#00d4ff;margin-bottom:0.8rem;">
                    AI NAVIGATION ENGINE READY
                </div>
                <div style="color:#8899aa;font-size:0.88rem;line-height:1.6;">
                    Enter your start location and destination<br>
                    to activate the real-time risk analysis engine.<br><br>
                    The system will evaluate CCTV coverage,<br>
                    incident patterns, lighting levels, and more<br>
                    to recommend the safest route for you.
                </div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 2 — SAFETY MAP
# ══════════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("### 🗺 Real-Time Safety Heatmap")

    map_col, info_col = st.columns([2, 1], gap="large")

    with map_col:
        city_sel = st.session_state.selected_city
        tod_for_map = "Night" if st.session_state.analysis_done and "time_of_day" in dir() else "Day"
        ut_for_map = "Traveler"
        mode_for_map = "Balanced"

        dest_label = ""
        if st.session_state.analysis_done:
            try:
                dest_label = destination
            except:
                dest_label = ""

        m = build_map(city_sel, tod_for_map, ut_for_map, mode_for_map, dest_label)
        map_data = st_folium(m, width=None, height=520, returned_objects=[])

    with info_col:
        st.markdown("#### 📋 Zone Risk Table")
        zones = CITY_ZONES[city_sel]["zones"]
        for zone in sorted(zones, key=lambda z: z["incident_score"], reverse=True):
            score = calculate_risk_score(zone, "Day", "Traveler", "Balanced")
            color = risk_color(score)
            label = risk_label(score)
            st.markdown(f"""
            <div style="background:var(--bg-card);border:1px solid var(--border-subtle);
                 border-left:3px solid {color};border-radius:8px;
                 padding:0.65rem 1rem;margin-bottom:0.5rem;">
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <div style="font-weight:600;font-size:0.88rem;">{zone['name']}</div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.78rem;color:{color};">{score}</div>
                </div>
                <div style="font-size:0.72rem;color:#8899aa;margin-top:0.3rem;">
                    📹 {zone['cctv']} | 💡 {zone['lighting']} | 👥 {zone['crowd']}
                </div>
                <div class="risk-bar-container" style="margin-top:0.4rem;">
                    <div class="risk-bar-fill" style="width:{score}%;background:{color}88;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 3 — ALERTS & TIPS
# ══════════════════════════════════════════════════════════════════════════════════
with tab3:
    if st.session_state.analysis_done:
        alerts_col, tips_col = st.columns(2, gap="large")

        with alerts_col:
            st.markdown("### 🔔 Predictive Alerts")
            st.markdown(f'<div style="font-family:\'Share Tech Mono\',monospace;font-size:0.75rem;color:#8899aa;margin-bottom:1rem;">{len(st.session_state.alerts)} alerts detected along route corridor</div>', unsafe_allow_html=True)
            for alert in st.session_state.alerts:
                css_class = f"alert-{alert['level']}"
                st.markdown(f'<div class="{css_class}">{alert["msg"]}</div>', unsafe_allow_html=True)

        with tips_col:
            st.markdown("### 🛡 Safety Guidance")
            avg = st.session_state.avg_risk
            color = risk_color(avg)
            st.markdown(f"""
            <div style="background:rgba({','.join(str(int(color.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.08);
                 border:1px solid {color}44;border-radius:10px;padding:1rem 1.2rem;margin-bottom:1rem;">
                <div style="font-family:'Rajdhani',sans-serif;font-size:1.1rem;font-weight:700;color:{color};">
                    Risk Level: {risk_label(avg)} ({avg}/100)
                </div>
                <div style="color:#8899aa;font-size:0.8rem;margin-top:0.3rem;">
                    Based on your route profile, time, and user type
                </div>
            </div>
            """, unsafe_allow_html=True)

            tips = get_safety_tips(avg, time_of_day if 'time_of_day' in dir() else "Day",
                                   user_type if 'user_type' in dir() else "Traveler")
            for tip in tips:
                st.markdown(f"""
                <div style="background:var(--bg-card);border:1px solid var(--border-subtle);
                     border-radius:8px;padding:0.75rem 1rem;margin-bottom:0.5rem;
                     font-size:0.87rem;line-height:1.5;">
                    {tip}
                </div>
                """, unsafe_allow_html=True)

            # Women safety layer
            if 'user_type' in dir() and user_type == "Woman":
                st.markdown("""
                <div style="background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.4);
                     border-radius:10px;padding:1rem 1.2rem;margin-top:1rem;">
                    <div style="color:#a78bfa;font-family:'Rajdhani',sans-serif;font-weight:700;font-size:1rem;margin-bottom:0.5rem;">
                        👩 WOMEN SAFETY LAYER ACTIVE
                    </div>
                    <div style="color:#c4b5fd;font-size:0.82rem;line-height:1.6;">
                        • Enhanced risk sensitivity applied to all zones<br>
                        • Route C strongly recommended — highest CCTV coverage<br>
                        • Emergency helpline: <b>1091</b> (Women Helpline)<br>
                        • Nirbhaya Fund-supported patrol zones marked on map
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="sr-card" style="text-align:center;padding:3rem;">
            <div style="font-size:2.5rem;margin-bottom:1rem;">🔔</div>
            <div style="font-family:'Rajdhani',sans-serif;font-size:1.2rem;color:#8899aa;">
                Run a route analysis to see predictive alerts and safety tips
            </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 4 — SYSTEM INFO
# ══════════════════════════════════════════════════════════════════════════════════
with tab4:
    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown("### ⚙️ System Architecture")
        st.markdown("""
        <div class="sr-card">
            <div style="font-family:'Share Tech Mono',monospace;font-size:0.82rem;line-height:2;color:#8899aa;">
                <div><span style="color:#00d4ff;">MODULE</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:#00ff88;">STATUS</span></div>
                <hr style="border-color:rgba(0,212,255,0.1);">
                <div>Risk Engine v2.1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:#00ff88;">● ONLINE</span></div>
                <div>Route Optimizer &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:#00ff88;">● ONLINE</span></div>
                <div>Heatmap Generator &nbsp;&nbsp;&nbsp;&nbsp; <span style="color:#00ff88;">● ONLINE</span></div>
                <div>Alert Engine &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:#00ff88;">● ONLINE</span></div>
                <div>IP Geolocation API &nbsp;&nbsp;&nbsp;&nbsp; <span style="color:#00d4ff;">◌ ON DEMAND</span></div>
                <div>Weather Integration &nbsp;&nbsp;&nbsp; <span style="color:#00d4ff;">◌ ON DEMAND</span></div>
                <div>SOS Dispatch Sim &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:#00ff88;">● ARMED</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🧠 Risk Model Parameters")
        st.markdown("""
        <div class="sr-card">
            <table style="width:100%;font-size:0.82rem;font-family:'Share Tech Mono',monospace;color:#8899aa;border-collapse:collapse;">
                <tr style="color:#00d4ff;border-bottom:1px solid rgba(0,212,255,0.2);">
                    <th style="text-align:left;padding:0.3rem 0;">Factor</th>
                    <th style="text-align:right;">Weight</th>
                </tr>
                <tr><td>Incident Score</td><td style="text-align:right;color:#e8f0fe;">×10</td></tr>
                <tr><td>Night Time</td><td style="text-align:right;color:#ff8c00;">+15</td></tr>
                <tr><td>Low CCTV</td><td style="text-align:right;color:#ff8c00;">+10</td></tr>
                <tr><td>High CCTV</td><td style="text-align:right;color:#00ff88;">−10</td></tr>
                <tr><td>Low Lighting</td><td style="text-align:right;color:#ff8c00;">+8</td></tr>
                <tr><td>Woman Profile</td><td style="text-align:right;color:#a78bfa;">+10</td></tr>
                <tr><td>Fast Mode</td><td style="text-align:right;color:#ff3b5c;">+5</td></tr>
                <tr><td>Safety First Mode</td><td style="text-align:right;color:#00ff88;">−10</td></tr>
                <tr><td>Night + Low Crowd</td><td style="text-align:right;color:#ff8c00;">+7</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("### 📡 Data Coverage")
        st.markdown("""
        <div class="sr-card">
            <div style="color:#8899aa;font-size:0.85rem;line-height:2;">
                <div>🏙 <b style="color:#e8f0fe;">4 Cities</b> — Mumbai, Delhi, Bengaluru, Pune</div>
                <div>📍 <b style="color:#e8f0fe;">30+ Zones</b> — Geo-tagged risk profiles</div>
                <div>📹 <b style="color:#e8f0fe;">Multi-factor CCTV</b> — Low / Medium / High</div>
                <div>📊 <b style="color:#e8f0fe;">Incident Database</b> — Historical pattern scores</div>
                <div>💡 <b style="color:#e8f0fe;">Lighting Intelligence</b> — Street-level granularity</div>
                <div>👥 <b style="color:#e8f0fe;">Crowd Dynamics</b> — Time-adjusted models</div>
                <div>🚨 <b style="color:#e8f0fe;">Emergency Layer</b> — SOS contact dispatch</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🔑 Emergency Contacts")
        st.markdown("""
        <div class="sr-card">
            <div style="font-family:'Share Tech Mono',monospace;font-size:0.82rem;line-height:2;color:#8899aa;">
                <div><span style="color:#ff3b5c;">🚨 Police Emergency</span> &nbsp; 100</div>
                <div><span style="color:#ff8c00;">🚑 Ambulance</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 108</div>
                <div><span style="color:#a78bfa;">👩 Women Helpline</span> &nbsp;&nbsp; 1091</div>
                <div><span style="color:#00d4ff;">🛡 Nirbhaya Line</span> &nbsp;&nbsp;&nbsp;&nbsp; 181</div>
                <div><span style="color:#00ff88;">🚒 Fire Brigade</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 101</div>
                <div><span style="color:#e8f0fe;">📞 Unified Emergency</span> &nbsp; 112</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🏆 About SafeRoute AI")
        st.markdown("""
        <div class="sr-card">
            <div style="color:#8899aa;font-size:0.84rem;line-height:1.7;">
                SafeRoute AI is a hackathon project demonstrating how
                <span style="color:#00d4ff;">multi-factor risk intelligence</span> can be layered
                onto navigation to protect vulnerable populations.<br><br>
                Built with <b style="color:#e8f0fe;">Python + Streamlit + Folium</b>,
                the system simulates a real-world safety platform with:
                extensible data pipelines, a modular risk engine,
                and a production-grade UI designed for
                <span style="color:#00ff88;">clarity, speed, and trust</span>.
            </div>
        </div>
        """, unsafe_allow_html=True)
