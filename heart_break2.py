import threading
import requests
import json
import os

url = os.environ.get('TARGET_URL2')
ORIGIN_URL = os.environ.get("ORIGIN_URL")
REFERER_URL = os.environ.get("REFERER_URL")


payload = json.dumps({
  "output": "..graph.figure...grid-result-detail-table.data...grid-eval-text.children..",
  "outputs": [
    {
      "id": "graph",
      "property": "figure"
    },
    {
      "id": "grid-result-detail-table",
      "property": "data"
    },
    {
      "id": "grid-eval-text",
      "property": "children"
    }
  ],
  "inputs": [
    {
      "id": "grid-button",
      "property": "nClicks",
      "value": 2
    }
  ],
  "changedPropIds": [
    "grid-button.nClicks"
  ],
  "state": [
    {
      "id": "grid-code",
      "property": "value",
      "value": "128143"
    },
    {
      "id": "date-picker-range",
      "property": "start_date",
      "value": "2021-08-15"
    },
    {
      "id": "date-picker-range",
      "property": "end_date",
      "value": "2022-08-15"
    },
    {
      "id": "grid-count",
      "property": "value",
      "value": 20
    },
    {
      "id": "grid-type",
      "property": "value",
      "value": "line"
    },
    {
      "id": "grid-c-rate",
      "property": "value",
      "value": 0.00005
    },
    {
      "id": "stop-on-top",
      "property": "value"
    },
    {
      "id": "grid-range",
      "property": "value",
      "value": [
        100,
        140
      ]
    }
  ]
})
headers = {
  'accept': 'application/json',
  'accept-language': 'zh,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'cookie': 'sl-session=Xnyib1wdeWcfqqilNWwh3g==; Hm_lvt_77cc3540511b0ae5a479b7d7f0994547=1733414758,1735904241; HMACCOUNT=8144A39C4F4A22E9; Hm_lpvt_77cc3540511b0ae5a479b7d7f0994547=1735906918; session=.eJyrVspMSc0rySyp1EssLcmIL6ksSFWyyivNydFByGSmQIRqAZu4EWc.Z3fsqQ.NUeLqedmtGwo-_trvaEisBQip80; session=.eJyrVspMSc0rySyp1EssLcmIL6ksSFWyyivNydFByGSmQIRqAZu4EWc.Z3fXHA.FuMb2586X2komaVS7gHtc551DSM',
  'origin': ORIGIN_URL,
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': REFERER_URL,
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'x-csrftoken': 'undefined'
}


def send_request():
    try:
        response = requests.request(
            "POST", url, headers=headers, data=payload, timeout=10)
        print(response.text)
    except Exception as e:
        print(e)


thread_list = []
for i in range(100):
    t = threading.Thread(target=send_request)
    t.start()
    thread_list.append(t)


for t in thread_list:
    t.join()
    
print("done")
