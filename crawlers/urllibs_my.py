import json
import urllib.request
r = urllib.request.urlopen('https://httpbin.org/get')
text = r.read()
print(r.status, r.reason)
obj = json.loads(text)

print(obj)

print(r.headers)
for k, v in  r.headers._headers:
    print('%s: %s' % (k, v))