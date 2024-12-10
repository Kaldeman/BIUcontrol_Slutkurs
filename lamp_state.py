#!/usr/bin/env python

import sys
import os
import json
import subprocess
import lamp_config

result = subprocess.run(['curl', '-X','GET','http://%s/api/%s/lights' % (lamp_config.ip, lamp_config.username)], stdout=subprocess.PIPE)
parsed = json.loads(result.stdout)
print(json.dumps(parsed, indent=4))
