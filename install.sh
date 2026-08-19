#!/usr/bin/env bash
#
# Antigravity Skills Installer
# Installs custom skills into ~/.gemini/config/skills/
#

set -e

SKILLS_DIR="$HOME/.gemini/config/skills"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Installing Antigravity Skills..."
mkdir -p "$SKILLS_DIR"

if [ -d "$SCRIPT_DIR/skills" ]; then
    for skill_path in "$SCRIPT_DIR/skills"/*; do
        if [ -d "$skill_path" ]; then
            skill_name="$(basename "$skill_path")"
            echo "📦 Installing skill: $skill_name -> $SKILLS_DIR/$skill_name"
            rm -rf "$SKILLS_DIR/$skill_name"
            cp -r "$skill_path" "$SKILLS_DIR/"
        fi
    done
    echo "✨ All skills have been successfully installed to $SKILLS_DIR"
    echo "💡 Restart Antigravity or start a new conversation to start using them!"
else
    echo "❌ Error: 'skills' directory not found in $SCRIPT_DIR"
    exit 1
fi
