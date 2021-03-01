import urllib.request
import json
from datetime import date, timedelta
import datetime

d = date.today()
y = d.year
m = d.month
first = datetime.date(y , m ,1)
mda = d-first
md = mda.days

pin = []
for i in range(0, 82):
    pin.append(0)
kl = 0
for k in range(0, md+1):
    for j in range(0, 82):
        pin[j] = 0
           
    days_before = (d - timedelta(days=k)).isoformat()
    for p in range(0,20):
        url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/draw-id?page={}".format(days_before, days_before,p)
        r = urllib.request.urlopen(url)
        html = r.read()
        html = html.decode()
        data = json.loads(html, strict=False)
        first = data[0]
        last = data[-1]
        print(first)
        print(last)
        url2 = "https://api.opap.gr/draws/v3.0/1100/draw-id/{}/{}?page={}".format(first, last,p)
        r2 = urllib.request.urlopen(url2)
        html2 = r2.read()
        html2 = html2.decode()
        data2 = json.loads(html2, strict=False)
        for i in data2["content"]:
            t = i["winningNumbers"]["list"]
            t.sort()
            print(t)
            for w in range(0, 20):
                pin[t[w]+1] = pin[t[w]+1]+1
        print("\n")
        m = max(pin)
        x = pin.index(m)
        print(pin)
        print("\n")
        print("ημέρα: ", days_before, "σελίδα", p)
    print("ημέρα: ", days_before,"συχνοτερος αριθμός: ", x-1)

