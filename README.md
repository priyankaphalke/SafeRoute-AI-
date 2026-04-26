# 🛡 SafeRoute AI — Real-Time Adaptive Safety Navigation System

A production-quality hackathon project: safety-first navigation powered by 
multi-factor risk intelligence, real-time simulation, and an immersive dark UI.

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

The app opens at **http://localhost:8501**

---

## 📁 File Structure

```
saferoute_ai/
├── app.py              ← Full Streamlit application (~600 lines)
├── requirements.txt    ← Python dependencies
└── README.md           ← This file
```

---

## 🧠 Features

| Feature | Description |
|---|---|
| 👤 User Profile | Name, phone, 3 emergency contacts in sidebar |
| 📍 Location Detection | IP-based or simulated coordinates |
| 🔍 Route Analysis | Animated 7-step real-time simulation |
| 📊 Risk Engine | Multi-factor scoring (CCTV, lighting, crowd, user type) |
| 🗺 Safety Heatmap | Folium dark map with color-coded risk circles |
| 🔔 Predictive Alerts | Context-aware warnings along route |
| 🛡 Safety Tips | Risk-adaptive guidance |
| 👩 Women Safety Layer | Enhanced sensitivity + dedicated warnings |
| 🚨 SOS Dispatch | Simulated emergency alert with contacts |

---

## 🏙 Supported Cities

- **Mumbai** — 10 zones
- **Delhi** — 8 zones  
- **Bengaluru** — 6 zones
- **Pune** — 5 zones

---

## ⚙️ Risk Formula

```
risk = incident_score × 10
     + 15  (if Night)
     + 10  (if CCTV Low)
     − 10  (if CCTV High)
     + 8   (if Lighting Low)
     + 10  (if User = Woman)
     + 7   (if Night + Low Crowd)
     + 5   (if Mode = Fast)
     − 10  (if Mode = Safety First)
     
clamped to [0, 100]
```

---

## 🌐 API Usage

- **ipapi.co** — Free IP geolocation (no key needed, graceful fallback)
- All other data is **intelligently simulated** — no API keys required

---

## 🏆 Tech Stack

- `streamlit` — UI framework
- `folium` + `streamlit-folium` — Interactive maps
- `requests` — IP geolocation API call
- Pure Python — zero database, zero backend server

---

## 💡 Hackathon Tips

- Demo the **Night mode + Woman profile** combination for maximum impact
- Click zone circles on the map to view detailed risk breakdowns
- Use the **SOS button** to demonstrate the emergency dispatch simulation
- Show all 3 route options and highlight the recommended safe route
