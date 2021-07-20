import json
import urllib.request
# r = urllib.request.urlopen('https://httpbin.org/get')
# text = r.read()
# print(r.status, r.reason)
# obj = json.loads(text)
#
# print(obj)
#
# print(r.headers)
# for k, v in  r.headers._headers:
#     print('%s: %s' % (k, v))
#
# ua = 'Mozilla/5.0'
# req = urllib.request.Request('http://httpbin.org/user-agent')
# req.add_header('User-Agent', ua)
# r = urllib.request.urlopen(req)
# resp = json.load(r)
#
#
# print(resp)
# print("user-agent", resp["user-agent"])



# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='http://httpbin.org/basic-auth/1/1',
                          user='1',
                          passwd='1')
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)
r = urllib.request.urlopen('http://httpbin.org')
print(r.read().decode('utf-8'))



