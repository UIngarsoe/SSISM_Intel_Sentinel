# SSISM Integrity & Verification Guide

**Version:** 1.0  
**Last Updated:** 22 May 2026

---

## Purpose

To ensure maximum credibility, transparency, and auditability of all SSISM analyses through cryptographic verification and immutable records.

---

## SSISM Verification Standard

Every published SSISM document must include:

1. **GitHub Immutable Commit Hash**
2. **SHA-256 Hash** of the file content
3. **Verification Command** (one-liner for Termux or any system)

---

## How to Verify a Document

### Standard Verification Command:

```bash
curl -L -o [filename].md https://raw.githubusercontent.com/UIngarsoe/SSISM_Intel_Sentinel/[commit-hash]/dossier/[filename].md && sha256sum [filename].md
