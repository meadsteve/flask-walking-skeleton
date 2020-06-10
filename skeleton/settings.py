import os

# This value must be set or there will be an error
REMOTE_SERVICE_URL = os.environ['REMOTE_SERVICE_URL']

# This value can be overridden by an environment variable but if
# it's not set the default will be used
HTTP_TIMEOUT = os.environ.get('HTTP_TIMEOUT', default=0.5)
