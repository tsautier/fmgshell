"""
Test file for quickly play with Python in general
"""

import json

#SWAGGER_FILE="fmg_jsonrpc_api/swagger/dvmdb.json"
SWAGGER_FILE="fmg_jsonrpc_api/swagger/cdb-obj74.json"

if __name__ == "__main__":
    with open(SWAGGER_FILE, "r") as f:
        content = json.load(f)

for key in content["tags"]:
    print(key["name"])