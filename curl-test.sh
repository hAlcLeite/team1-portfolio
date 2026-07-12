#!/bin/bash

BASE_URL="http://localhost:5000/api/timeline_post"

echo "=========================================="
echo "  Timeline Post API - curl Test Script"
echo "=========================================="

# ── Step 1: GET all posts (should start empty or show existing) ──────────────
echo ""
echo "1) GET all timeline posts:"
curl --silent --request GET "$BASE_URL" | python3 -m json.tool 2>/dev/null || curl --silent --request GET "$BASE_URL"

# ── Step 2: POST a random timeline post ──────────────────────────────────────
echo ""
echo "2) POST a new timeline post:"
RANDOM_ID=$RANDOM
RESPONSE=$(curl --silent --request POST "$BASE_URL" \
  --data "name=Henrique Leite" \
  --data "email=henrique@mlh.io" \
  --data "content=Test post #$RANDOM_ID - Added by curl-test.sh at $(date)")

echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

# Extract the ID of the newly created post
POST_ID=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])" 2>/dev/null)

# ── Step 3: GET all posts again to confirm it was added ─────────────────────
echo ""
echo "3) GET all timeline posts (should include the new post):"
curl --silent --request GET "$BASE_URL" | python3 -m json.tool 2>/dev/null || curl --silent --request GET "$BASE_URL"

# ── Step 4: (Bonus) DELETE the test post we just created ────────────────────
if [ -n "$POST_ID" ]; then
  echo ""
  echo "4) BONUS - DELETE the test post (id=$POST_ID):"
  curl --silent --request DELETE "$BASE_URL/$POST_ID" | python3 -m json.tool 2>/dev/null || curl --silent --request DELETE "$BASE_URL/$POST_ID"

  echo ""
  echo "5) GET all timeline posts after deletion:"
  curl --silent --request GET "$BASE_URL" | python3 -m json.tool 2>/dev/null || curl --silent --request GET "$BASE_URL"
else
  echo ""
  echo "4) BONUS - Could not extract post ID for DELETE (python3 may not be available)"
  echo "   Manually run: curl --request DELETE $BASE_URL/<id>"
fi

echo ""
echo "=========================================="
echo "  Test complete!"
echo "=========================================="
