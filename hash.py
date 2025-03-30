hash.py > ...
  import hashlib
  for i in range(10000):
|     print(i,hashlib.sha256(bytes(i)).hexdigest())
