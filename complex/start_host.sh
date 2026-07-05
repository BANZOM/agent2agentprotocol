#!/bin/bash
# Start the host agent (Banzo) via adk web.
# Run this AFTER starting remote agents with start_agents.sh

set -e

cd "$(dirname "$0")/.."

# Load environment variables
if [ -f complex/.env ]; then
    export $(grep -v '^#' complex/.env | xargs)
fi

export PYTHONPATH="$(pwd):$PYTHONPATH"

echo "Starting Banzo (host agent) via adk web..."
echo "  UI: http://localhost:8000"
echo ""

adk web complex/host_agent/host
