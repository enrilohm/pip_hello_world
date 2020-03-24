#!/bin/bash
set -e

REPO_NAME=$(basename ${PWD})
PRIVATE=true

echo "creating repo ${REPO_NAME} on github"
JSON_STRING=$( jq -n \
                  --arg rn "$REPO_NAME" \
                  --arg p "$PRIVATE" \
                  --arg tl "$TARGET_LOCATION" \
                  '{name: $rn, private: $p,}' )
curl -H "Authorization: token 936635fa11ddd190a1e30960716a7fa7210dd7ba" \
--data "${JSON_STRING}" \
https://api.github.com/user/repos

git init
git add -A
git commit -m "first commit"
git remote add origin git@github.com:enrilohm/${REPO_NAME}.git
git push -u origin master
