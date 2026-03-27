#!/bin/bash
echo "🚀 Setting up project for Waks stack..."

# Rust projects
if [ -f "Cargo.toml" ]; then
    echo "📦 Rust project detected"
    rustup update stable
    cargo fetch
    cargo install cargo-watch  # For development
    echo "✅ Rust environment ready"
fi

# C/C++ projects  
if [ -f "CMakeLists.txt" ] || [ -f "Makefile" ]; then
    echo "🔧 C/C++ project detected"
    sudo pacman -S --needed base-devel cmake gcc clang 2>/dev/null || true
    mkdir -p build
    echo "✅ C/C++ build system ready"
fi

# TypeScript/JavaScript projects
if [ -f "package.json" ]; then
    echo "🌐 TypeScript/Node.js project detected"
    npm install
    echo "✅ Node.js environment ready"
fi

# Python projects (for scripting/automation)
if [ -f "requirements.txt" ]; then
    echo "🐍 Python project detected"
    python -m pip install -r requirements.txt
    echo "✅ Python environment ready"
fi

# Lua projects (for Neovim/configs)
if [ -f "*.lua" ] || [ -d "lua/" ]; then
    echo "🧩 Lua project detected"
    # Lua specific setup if needed
    echo "✅ Lua environment ready"
fi

# Cross-language detection
if [ -f "Cargo.toml" ] && [ -f "CMakeLists.txt" ]; then
    echo "🔄 Cross-language (Rust + C/C++) project detected"
    echo "💡 Remember to set up FFI bindings"
fi

# Setup git hooks
cp .github/hooks/* .git/hooks/ 2>/dev/null || true
chmod +x .git/hooks/* 2>/dev/null || true

echo "✅ Project setup complete for Waks development stack!"
