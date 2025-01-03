import requests
import json
import os

url = os.environ.get('TARGET_URL')
ORIGIN_URL = os.environ.get("ORIGIN_URL")
REFERER_URL = os.environ.get("REFERER_URL")

payload = json.dumps({
  "output": "market-board-grid-container.children",
  "outputs": {
    "id": "market-board-grid-container",
    "property": "children"
  },
  "inputs": [
    {
      "id": "market-board-layouts-restore",
      "property": "data",
      "value": [
        {
          "w": 12,
          "h": 6,
          "x": 0,
          "y": 0,
          "i": "scope_graph",
          "moved": False,
          "static": False
        },
        {
          "w": 6,
          "h": 4,
          "x": 0,
          "y": 6,
          "i": "up_or_down_graph",
          "moved": False,
          "static": False
        },
        {
          "w": 6,
          "h": 4,
          "x": 6,
          "y": 6,
          "i": "agg_table",
          "moved": False,
          "static": False
        },
        {
          "w": 12,
          "h": 5,
          "x": 0,
          "y": 10,
          "i": "treemap",
          "moved": False,
          "static": False
        }
      ]
    }
  ],
  "changedPropIds": [
    "market-board-layouts-restore.data"
  ]
})

headers = {
  'accept': 'application/json',
  'accept-language': 'zh,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'cookie': 'sl-session=Xnyib1wdeWcfqqilNWwh3g==; Hm_lvt_77cc3540511b0ae5a479b7d7f0994547=1733414758,1735904241; HMACCOUNT=8144A39C4F4A22E9; Hm_lpvt_77cc3540511b0ae5a479b7d7f0994547=1735906918; session=.eJyrVspMSc0rySyp1EssLcmIL6ksSFWyyivNydFByGSmQIRqAZu4EWc.Z3fWUg.dnGBgW2aZwgaPYStmdMb6r2xngE; session=.eJyrVspMSc0rySyp1EssLcmIL6ksSFWyyivNydFByGSmQIRqAZu4EWc.Z3fXHA.FuMb2586X2komaVS7gHtc551DSM',
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

for i in range(100):
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
