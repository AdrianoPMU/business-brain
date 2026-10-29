#!/usr/bin/env bash
# Installs the claude-seo skills and agents for this session.
# Cloud sessions don't load plugins from .claude/settings.json, so run this once per session:
#   bash scripts/install-seo.sh
# Pinned to a release tag; bump CLAUDE_SEO_TAG deliberately after reading the changelog.
set -euo pipefail

TAG="${CLAUDE_SEO_TAG:-v2.5.0}"

if [ -x "$HOME/.claude/skills/seo/scripts/claude-seo" ]; then
    echo "claude-seo already installed. Checking runtime..."
    "$HOME/.claude/skills/seo/scripts/claude-seo" doctor
    exit 0
fi

work="$(mktemp -d)"
trap 'rm -rf -- "$work"' EXIT
git clone --depth 1 --branch "$TAG" https://github.com/AgriciDaniel/claude-seo.git "$work/claude-seo"
CLAUDE_SEO_TAG="$TAG" bash "$work/claude-seo/install.sh"
