import requests

BEARER_TOKEN = 
ZONE_ID = 

BASE_URL = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"

WHITELIST = ["www.is404.net", "api.is404.net"]


def get_records(dns_record_type: str):
    resp = requests.get(
        f"{BASE_URL}?type={dns_record_type}",
        headers={"Authorization": f"Bearer {BEARER_TOKEN}"},
    )
    record_ids = []
    for record in resp.json()["result"]:
        if record["name"] not in WHITELIST:
            record_ids.append(record["id"])
    return record_ids


def delete_record(record_id):
    resp = requests.delete(
        f"{BASE_URL}/{record_id}",
        headers={"Authorization": f"Bearer {BEARER_TOKEN}"},
    )
    print(resp.status_code, record_id)


if __name__ == "__main__":
    records = get_records("A")
    for record in records:
        delete_record(record)
    records = get_records("CNAME")
    for record in records:
        delete_record(record)
