#!/bin/bash
echo "🔧 Starting development environment for Waks stack..."

# Rust projects
if [ -f "Cargo.toml" ]; then
    echo "🦀 Starting Rust development server..."
    cargo watch -x run -x test
    exit 0
fi

# TypeScript/Node.js projects
if [ -f "package.json" ] && [ -f "vite.config.ts" ]; then
    echo "🌐 Starting TypeScript dev server..."
    npm run dev
    exit 0
fi

# C/C++ projects with hot reload
if [ -f "CMakeLists.txt" ] && [ -f "scripts/dev-reload.sh" ]; then
    echo "🔧 Starting C++ with hot reload..."
    ./scripts/dev-reload.sh
    exit 0
fi

echo "⚠️  No Waks-stack development server detected"
echo "💡 Supported: Rust, TypeScript, C/C++ with hot reload"
echo "💡 Add your custom dev commands to scripts/dev.sh"
