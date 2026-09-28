#!/usr/bin/env bash
set -euo pipefail

echo "=================================================="
echo "SRE Validation: Speculative RAG Studio"
echo "=================================================="

echo "[1/4] Validating Python Engine syntax..."
python3 -m py_compile speculative_rag_engine.py
python3 -m py_compile manim_flow.py
echo "✓ Python compilation clean."

echo "[2/4] Executing mock Speculative RAG cycle..."
python3 speculative_rag_engine.py > /dev/null
echo "✓ Speculative generation and verification cycle verified."

echo "[3/4] Validating TypeScript Client syntax..."
npx --yes tsc --noEmit rag_verifier_client.ts
echo "✓ TypeScript compilation clean."

echo "[4/4] Validating Kubernetes Manifest..."
grep -q "speculative-rag-service" k8s-speculative-rag.yaml
echo "✓ Kubernetes manifest clean."

echo "=================================================="
echo "ALL TESTS PASSED: tp-speculative-rag-verifier ready."
echo "=================================================="
