from datetime import datetime

def create_job_alert(title, organization, category, official_link):
message = f"""
🚨 MK AI JOB ALERT 🚨

📢 भर्ती: {title}
🏢 विभाग/कंपनी: {organization}
🌍 श्रेणी: {category}

🔗 आधिकारिक लिंक: {official_link}

⚠️ आवेदन करने से पहले आधिकारिक नोटिफिकेशन जरूर पढ़ें।
🕒 अलर्ट तैयार: {datetime.now().strftime('%d-%m-%Y %H:%M')}
"""
return message

if name == "main":
alert = create_job_alert(
title="उदाहरण भर्ती",
organization="उदाहरण विभाग",
category="सरकारी नौकरी",
official_link="https://example.com"
)
print(alert)
