#!/bin/bash
# lyra.sh - Script to manage Lyra AI Agent server and Ollama model

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/lyra.pid"
MODEL_NAME="gemma3:4b-it-q4_K_M"

start_server() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null; then
            echo "Lyra AI Agent server is already running (PID: $PID)"
            return 1
        else
            # Remove stale PID file
            rm "$PID_FILE"
        fi
    fi
    
    echo "Starting Ollama model: $MODEL_NAME..."
    # Start the model in background
    ollama run $MODEL_NAME &>/dev/null &
    sleep 3  # Give the model time to load
    
    echo "Starting Lyra AI Agent server..."
    cd "$SCRIPT_DIR/backend" || exit 1
    poetry run python main.py &
    SERVER_PID=$!
    echo $SERVER_PID > "$PID_FILE"
    echo "Server started with PID $SERVER_PID"
    echo "Access the GUI at http://localhost:5252"
    echo "Model $MODEL_NAME is loaded and ready"
}

stop_server() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null; then
            echo "Stopping Lyra AI Agent server (PID: $PID)..."
            kill "$PID"
        else
            echo "Server process not found."
        fi
        rm "$PID_FILE"
    else
        echo "No PID file found. Checking for running processes..."
        # Try to find and kill any running processes
        pkill -f "poetry run python main.py" 2>/dev/null
    fi
    
    echo "Stopping Ollama model: $MODEL_NAME..."
    ollama stop $MODEL_NAME 2>/dev/null
    
    echo "Server and model stopped"
}

status_server() {
    echo "=== Lyra AI Agent Status ==="
    
    # Check server status
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null; then
            echo "✓ Lyra AI Agent server is running (PID: $PID)"
        else
            echo "✗ Lyra AI Agent server is not running (stale PID file)"
        fi
    else
        # Check for any running processes
        if pgrep -f "poetry run python main.py" > /dev/null; then
            echo "✓ Lyra AI Agent server is running (PID unknown)"
        else
            echo "✗ Lyra AI Agent server is not running"
        fi
    fi
    
    # Check model status
    echo ""
    echo "=== Ollama Model Status ==="
    if ollama ps | grep -q "$MODEL_NAME"; then
        echo "✓ Ollama model $MODEL_NAME is loaded"
        echo "Model details:"
        ollama ps | grep "$MODEL_NAME"
    else
        echo "✗ Ollama model $MODEL_NAME is not loaded"
    fi
}

restart_server() {
    stop_server
    sleep 2
    start_server
}

case "$1" in
    start)
        start_server
        ;;
    stop)
        stop_server
        ;;
    restart)
        restart_server
        ;;
    status)
        status_server
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac