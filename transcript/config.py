# load proxy

import os
import sys

# load proxy

HTTP_PROXY = os.getenv('HTTP_PROXY', None)
HTTPS_PROXY = os.getenv('HTTPS_PROXY', None)
