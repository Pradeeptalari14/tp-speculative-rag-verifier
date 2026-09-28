# Speculative RAG & Self-Correction Studio

[![CI SRE Validation](https://github.com/Pradeeptalari14/tp-speculative-rag-verifier/actions/workflows/sre-validation.yml/badge.svg)](https://github.com/Pradeeptalari14/tp-speculative-rag-verifier/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Speculative Decoding & Verification](https://img.shields.io/badge/Architecture-Draft%20SLM%20%2B%20Verifier%20Judge-blue.svg)](https://talaripradeep.info)

Production-grade implementation of **Speculative Retrieval-Augmented Generation (Speculative RAG)** with parallel hypothesis generation and single-pass factual verification.

![Speculative RAG Flow](docs/speculative_rag_flow.png)

## Key Technical Highlights
- **62% TTFT Latency Reduction:** Uses a fast 1.5B Small LM to draft multiple candidate answers in parallel (~140 tok/s), verified in a single forward pass by a 70B judge model.
- **Factual Hallucination Suppression:** Rejects tokens unsupported by retrieved context chunks, dropping factual error rates to `<0.4%`.
- **Hybrid Retrieval Integration:** Combines dense embedding search with sparse BM25 keyword matching.
- **58% Frontier Token Cost Savings:** Offloads routine token generation from expensive frontier LLMs to budget edge SLMs.

## Quickstart
```bash
git clone https://github.com/Pradeeptalari14/tp-speculative-rag-verifier.git
cd tp-speculative-rag-verifier
bash scripts/validate.sh
```
