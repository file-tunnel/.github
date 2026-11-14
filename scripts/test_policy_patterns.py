#!/usr/bin/env python3
"""Adversarial, token-free controls for the organization baseline scanner."""
from __future__ import annotations

import runpy
from pathlib import Path

namespace = runpy.run_path(str(Path(__file__).with_name("validate_baseline.py")))
uses = namespace["USES_PATTERN"]
secrets = namespace["SECRET_PATTERNS"]

assert uses.search("    - uses: actions/checkout@v4").group(1) == "actions/checkout@v4"
assert uses.search("        uses: owner/repo@abc123 # comment").group(1) == "owner/repo@abc123"
assert uses.search("    uses: ./.github/workflows/local.yml").group(1) == "./.github/workflows/local.yml"
assert uses.search("      run: echo no-action") is None

# Assemble a synthetic credential at runtime so this test contains no token
# literal that the scanner would incorrectly treat as a leaked secret.
synthetic_header = "authorization" + ":" + " Bearer " + "T" * 24
assert any(pattern.search(synthetic_header) for pattern in secrets)
assert not any(pattern.search("authorization: Bearer REDACTED") for pattern in secrets)
print("policy-patterns: accepted adversarial regex self-tests")
