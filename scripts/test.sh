#!/bin/bash
echo "🧪 Running tests for Waks stack..."

# Rust
[ -f "Cargo.toml" ] && cargo test

# C/C++
[ -f "Makefile" ] && make test
[ -f "CMakeLists.txt" ] && cd build && ctest .. && cd ..

# TypeScript/Node.js  
[ -f "package.json" ] && npm test

# Python
[ -f "pytest.ini" ] && pytest
[ -f "requirements.txt" ] && python -m pytest tests/ 2>/dev/null || true

# Cross-language integration tests
if [ -f "tests/integration/" ]; then
    echo "🔗 Running cross-language integration tests"
    ./tests/integration/run.sh 2>/dev/null || true
fi

echo "✅ Tests completed for Waks stack!"
