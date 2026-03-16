#!/usr/bin/env python3
"""Generate dark-themed project card SVGs matching portfolio site design."""

import os

projects = [
    {
        "file": "card-plw.svg",
        "name": "Property Linkware",
        "type": "Enterprise API / Data Infrastructure",
        "desc": "Universal property data infrastructure. 7-step permission system,",
        "desc2": "automated deduplication, immutable observations, 34-event webhooks.",
        "stats": [("170+", "ENDPOINTS"), ("33", "TABLES"), ("594", "TESTS"), ("87+", "SERVICES")],
        "stack": "NestJS · PostgreSQL · PostGIS · DDD + CQRS · Docker",
    },
    {
        "file": "card-helm.svg",
        "name": "Helm Intelligence",
        "type": "AI / Voice Agent Platform",
        "desc": "Autonomous voice agent improvement. Analyzes transcripts, detects",
        "desc2": "failure patterns, generates fixes with multi-model routing.",
        "stats": [("4.3K", "FILES"), ("6", "PIPELINE STAGES")],
        "stack": "Fastify · BullMQ · Redis · Claude AI · Drizzle",
    },
    {
        "file": "card-codex.svg",
        "name": "Codex Audit",
        "type": "AI Code Analysis Engine",
        "desc": "M&A-grade technical due diligence in days. 6-stage pipeline with",
        "desc2": "RAG risk scoring. $100 in API costs replaces $150K+ engagements.",
        "stats": [("510", "FILES"), ("6", "ANALYSIS STAGES")],
        "stack": "NestJS · Next.js · Claude API · LRU Cache",
    },
    {
        "file": "card-greenwood.svg",
        "name": "Greenwood Hall",
        "type": "Full-Stack SaaS",
        "desc": "Event booking with Stripe payments, automated email, analytics,",
        "desc2": "E2E tests, load testing for concurrent booking flows.",
        "stats": [("937", "FILES"), ("E2E", "TESTED")],
        "stack": "Next.js · Prisma · Stripe · Playwright",
    },
    {
        "file": "card-outreach.svg",
        "name": "Outreach Engine",
        "type": "Lead Intelligence Platform",
        "desc": "Automated B2B lead pipeline. Multi-source ingestion, quality scoring,",
        "desc2": "website analysis, market signal detection, Slack alerts.",
        "stats": [("4.2K", "FILES"), ("Auto", "SCORING")],
        "stack": "Fastify · Neon · Apollo.io · Cron",
    },
    {
        "file": "card-mcc.svg",
        "name": "Mobile Command Center",
        "type": "React Native / Agent Control",
        "desc": "Mobile app for remotely controlling AI agents. WebSocket relay wraps",
        "desc2": "Claude Agent SDK. QR pairing, real-time task management.",
        "stats": [("iOS", "+ ANDROID"), ("WS", "REAL-TIME")],
        "stack": "React Native · Node.js · WebSocket · Claude SDK",
    },
]

def gen_card(p):
    stats_x_start = 60
    stats_svg = ""
    for i, (val, label) in enumerate(p["stats"]):
        x = stats_x_start + i * 140
        stats_svg += f'  <text x="{x}" y="195" fill="#fafafa" font-family="\'Segoe UI\', sans-serif" font-size="22" font-weight="500" letter-spacing="-0.5">{val}</text>\n'
        stats_svg += f'  <text x="{x}" y="215" fill="#666666" font-family="\'Segoe UI\', sans-serif" font-size="10" letter-spacing="1.5">{label}</text>\n'

    return f'''<svg width="580" height="280" viewBox="0 0 580 280" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="580" height="280" rx="12" fill="#111114"/>
  <rect x="0.5" y="0.5" width="579" height="279" rx="11.5" stroke="#333333" stroke-opacity="0.5"/>
  <text x="60" y="55" fill="#fafafa" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="28" font-weight="300" letter-spacing="-1">{p["name"]}</text>
  <text x="60" y="80" fill="#666666" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="13" letter-spacing="0.5">{p["type"]}</text>
  <text x="60" y="120" fill="#999999" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="14" letter-spacing="0.2">{p["desc"]}</text>
  <text x="60" y="140" fill="#999999" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="14" letter-spacing="0.2">{p["desc2"]}</text>
  <line x1="60" y1="165" x2="520" y2="165" stroke="#333333" stroke-width="1"/>
{stats_svg}
  <text x="60" y="258" fill="#444444" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" letter-spacing="0.3">{p["stack"]}</text>
</svg>'''

dir_path = os.path.dirname(os.path.abspath(__file__))
for p in projects:
    path = os.path.join(dir_path, p["file"])
    with open(path, "w") as f:
        f.write(gen_card(p))
    print(f"Generated {p['file']}")

print("Done!")
