import requests as r
import time


def main():
    with open('accounts.txt', 'r') as file:
        accounts = file.read().split('\n')

    for account in accounts:
        res = r.post(url="https://hook.us1.make.com/as22p9q6fmnemmxku4cq927jwplsyi92", json={"EMAIL": account, "PAGE_AND_SECTION": "https://forms.leapwallet.io/leap-cosmos#cosmos-emailcapture-1"})
        print(f"{account} registered")
        time.sleep(1)


if __name__ == "__main__":
    main()
