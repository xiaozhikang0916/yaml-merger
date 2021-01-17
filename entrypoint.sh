#! /bin/bash
KEY_LIST=${KEY_LIST:-"proxies,proxy-groups"}

cd /app
python3 merge_yaml.py $FROM_FILE $TO_FILE $KEY_LIST