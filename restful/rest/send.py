import requests

headers = {}

headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3NjgyNzg0LCJqdGkiOiJkMDY0Yjg5N2M3Y2U0MmJiOTZlMDcwZmIxMTI1OGMyNyIsInVzZXJfaWQiOjF9.UAGISc6jQtgJeXxIHBxhbnD1MwQfGbiwNbRUAW8sN5Y'

r = requests.get('http://127.0.0.1:8080/users', headers=headers)

print(r.text)