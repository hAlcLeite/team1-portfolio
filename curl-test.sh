#!/bin/bash

set -e

BASE_URL="http://localhost:5000"
RANDOM_ID=$RANDOM
NAME="Kriti Test $RANDOM_ID"
EMAIL="kriti$RANDOM_ID@example.com"
CONTENT="Random timeline post $RANDOM_ID"

echo "Creating timeline post..."
POST_RESPONSE=$(curl --max-time 5 -s -X POST "$BASE_URL/api/timeline_post" \
  -d "name=$NAME" \
  -d "email=$EMAIL" \
  -d "content=$CONTENT")

echo "$POST_RESPONSE"

echo "Checking timeline posts..."
GET_RESPONSE=$(curl --max-time 5 -s "$BASE_URL/api/timeline_post")

echo "$GET_RESPONSE"

if echo "$GET_RESPONSE" | grep -q "$CONTENT"; then
  echo "PASS: timeline post was added and found"
  exit 0
else
  echo "FAIL: timeline post was not found"
  exit 1
fi
