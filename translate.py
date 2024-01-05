import requests

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
headers = {"Authorization": "Bearer {token}"}

def run(model, input):
    response = requests.post(f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/m2m100-1.2b", headers=headers, json=input)
    return response.json()


def trans(souce, target, text):
    jvalue = {
      "text": text,
      "source_lang": souce,
      "target_lang": target
    }
    output = run('@cf/meta/m2m100-1.2b', jvalue)
    return output
