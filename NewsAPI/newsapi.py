#!/usr/bin/env python3
""" Get information from Newsapi https://newsapi.org"""

import json
import requests

newsapi_URL = "https://newsapi.org/v2/top-headlines?sources=techcrunch"

def get_newsapikey():
    with open("/home/student/newsapi_key") as newsapikeyfile:
            return newsapikeyfile.read().rstrip("\n")


def newslookup(newsapikey):
    try:

        api = f"{newsapi_URL}&apikey={newsapikey}"
        resp = requests.get(api)

        return resp.json()

    except:
        return False


def main():

    apikey = get_newsapikey()

    resp = newslookup(apikey)

    if resp:
        resp = resp.get("articles")
        #print(resp)
        print("News Title")
        i = 0
        for data in resp:
            i = i + 1
            print(str(i) + ") " + data.get("title"))
        print("")
        num = input("Which news you want to read more in contents? Please type in the number >> ")
        print("")
        print(resp[int(num) - 1]["content"])

    else:
        print("Result return in error")

if __name__ == "__main__":
    main()



