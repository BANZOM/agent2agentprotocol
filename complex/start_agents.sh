#!/bin/bash
# Launch all remote friend agents for the A2A multi-framework demo.
# Start this first, then run: adk web complex/host_agent/host

set -e

# Always run from project root
cd "$(dirname "$0")/.."

# Load environment variables
if [ -f complex/.env ]; then
    export $(grep -v '^#' complex/.env | xargs)
fi

# Disable CrewAI telemetry (avoids SSL errors)
export CREWAI_DISABLE_TELEMETRY=true
export OTEL_SDK_DISABLED=true

export PYTHONPATH="$(pwd):$PYTHONPATH"

echo "Starting remote agents..."
echo "  Karley (ADK)       -> http://localhost:10001"
echo "  Nate   (LangGraph) -> http://localhost:10002"
echo "  Kait   (CrewAI)    -> http://localhost:10003"
echo ""

# Start all 3 remote agents in the background
python -m complex.karley_agent.karley &
PID_KARLEY=$!

python -m complex.nate_agent.nate &
PID_NATE=$!

python -m complex.kait_agent.kait &
PID_KAIT=$!

echo "All remote agents started. PIDs: karley=$PID_KARLEY nate=$PID_NATE kait=$PID_KAIT"
echo ""
echo "Now run the host agent in another terminal:"
echo "  source complex/.env && export AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_REGION_NAME && adk web complex/host_agent/host"
echo ""
echo "Press Ctrl+C to stop all agents."

# Wait and handle cleanup
trap "kill $PID_KARLEY $PID_NATE $PID_KAIT 2>/dev/null; echo 'All agents stopped.'" EXIT
wait
