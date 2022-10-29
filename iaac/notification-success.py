import requests
import json
import os

url = os.environ.get("WEBHOOK_SLACK_NOTIFICATION_ANDROID")
buildUrl=os.environ.get("BUILD_URL")
LinkAPK=str(buildUrl)+"artifact/app/build/outputs/apk/debug/app-debug.apk"

payload = json.dumps({
  "attachments": [
    {
      "mrkdwn_in": [
        "text"
      ],
      "color": "#36a64f",
      "title": "Android",
      "title-link": "Notif",
      "thumb_url": "",
      "footer": "Devops",
      "footer_icon": "",
      "ts": "1641337164",
      "fields": [
        {
          "title": "Download APK",
          "value": LinkAPK,
          "short": False
        }
      ]
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

