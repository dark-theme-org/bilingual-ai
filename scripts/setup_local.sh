#!/bin/bash

# install_claude
# Installs the Claude CLI if not already present. Checks for an existing `claude`
# binary and skips installation if found. Downloads and runs the official installer
# from claude.ai; logs success or failure and continues execution regardless of the outcome.
function install_claude() {
  echo "LOG::[INFO] Installing Claude..."

  if command -v claude &>/dev/null; then
    echo "LOG::[INFO] Claude is already installed! Skipping installation."
    return 0
  fi

  if curl -fsSL https://claude.ai/install.sh | bash; then
    echo "LOG::[INFO] Successfully installed Claude!"
  else
    echo "LOG::[ERROR] Failed to install Claude!"
    echo "LOG::[ERROR] Will continue without Claude installation."
  fi
}

install_claude
