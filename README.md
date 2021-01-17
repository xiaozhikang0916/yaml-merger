# Yaml Merger

A simple tool to merge 2 yaml files, to update config of clash running in remote NAS server without auto update option.

## To test

Firstly, clone this repo and build.

```bash
git clone ...
docker build . -t mergeyaml
```

Run following command:

```bash
docker run -v `pwd`/test:/app/data -e FROM_FILE="data/from.yml" -e TO_FILE="data/to.yaml" -e KEY_LIST="foo,bar" --rm mergeyaml
```

Then check `test/to.yaml` if all `old` values are replaced by `new` now and `do not change` values remain there.

## Parameters

Env Params|Used for
-|-
FROM_FILE|Configs to be merged from, may be a http link
TO_FILE|Configs to be merged to, like your local configs, should be writeable
KEY_LIST|Keys to be merged, keep empty to apply the default value `proxies,proxy-groups`, to keep your customized port and domain config
