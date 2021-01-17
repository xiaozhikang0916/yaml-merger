#!/usr/bin/env python3

import yaml, sys, requests

def loadYaml(stream):
    try:
        return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

def loadYamlFile(path):
    with open(path, 'r', encoding='utf8') as f:
        return loadYaml(f)

def loadYamlHttp(url):
    with requests.get(url, stream=True) as r:
        return loadYaml(r.content)

def mergeYaml(fromConf, toConf, keyList):
    for k in keyList:
        print("Copying config of key {}".format(k))
        toConf[k] = fromConf[k]

if __name__ == "__main__":
    args = sys.argv
    print(args)
    fromPath = args[1]
    toPath = args[2]
    if (len(args) > 3):
        keyList = args[3].split(',')
    else:
        keyList = ["proxies", "proxy-groups"]
    print("Merge config of keys {} from {} to {}".format(keyList, fromPath, toPath))
    if (fromPath.startswith("http")):
        fromConf = loadYamlHttp(fromPath)
    else:
        fromConf = loadYamlFile(fromPath)

    toConf = loadYamlFile(toPath)
    mergeYaml(fromConf, toConf, keyList)
    
    with open(toPath, 'w', encoding='utf8') as outfile:
        yaml.dump(toConf, outfile, default_flow_style=False, allow_unicode=True)