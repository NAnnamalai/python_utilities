import os
import uuid

print os.urandom(24).encode('hex')

print os.urandom(16).encode('hex')

print os.urandom(12).encode('hex')

print uuid.uuid4().hex


