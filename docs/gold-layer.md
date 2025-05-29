# L-2 Gold Stability

This document outlines how the "Gold" principle applies to the L-2 Structured Reasoning layer.

## Goal
Maintain an immutable core reasoning engine while tracking any drift across updates.

## Metrics for Invariance
- **Regression Test Suite**: run a fixed set of logic queries and check outputs remain unchanged.
- **Proof Hashes**: store SHA-256 hashes of serialized reasoning graphs.
- **Functional Accuracy**: verify results on known problems stay stable.
- **Resource Baseline**: record CPU and memory usage for the test suite.
- **Drift Index**: compare embeddings of outputs to previous "Gold" runs.
- **Versioned Checkpoints**: sign and store the code hash with each stable release.

## Workflow
1. After passing all tests, create a new entry in `GOLD_CHECKPOINT.yml` with the commit hash and test hashes.
2. CI runs the metrics on each commit and compares with the latest checkpoint.
3. If metrics deviate beyond thresholds, flag the commit for review.
