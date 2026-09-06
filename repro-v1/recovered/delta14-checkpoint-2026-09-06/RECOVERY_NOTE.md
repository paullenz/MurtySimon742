# Partial source publication from a fully recovered checkpoint

This directory currently contains eight exact original source/status files, not the complete checkpoint. The original files are preserved without modifying their historical wording. In particular, CHECKPOINT_STATUS.json is the checkpoint of 6 September 2026 at 10:02 UTC, not the global current theorem ledger.

The complete received archive is delta14_checkpoint-2.zip, SHA-256 27d4a632dc8bc2262def45b0a3ea0650adb8fb5d7e831e19839d14a3f8af9dfe. Every one of its 773 manifest payloads was recovered and matched. Bulk archive and remaining payload publication are still pending. Do not interpret the existence of a replay driver as the presence or verification of its entire input corpus in this checkout.

See project/recovery/2026-09-06-upload-02.md at repository root for the fresh checks, original-container distinction, limitations and preservation state. The independent C++ source was compiled and passed four supplied regression examples; the historical 649 proofs were hash-checked but not freshly replayed in this intake. The graph-to-CNF and screening-certificate obligations remain unchanged.
