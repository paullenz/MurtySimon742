# Manual binary upload instructions for paullenz/MurtySimon25

The repository is configured with Git LFS for `*.zip`, `*.gz`, `*.drup`, `*.drat`, and `*.lrat`.

## Recommended destination paths

Copy the ZIP evidence files into:

    repro-v1/evidence/archives/

Copy the Audit-v5 PDF and DOCX into:

    repro-v1/evidence/reports/

The exact reproducibility release ZIP may be stored at:

    releases/erdos742_n25_reproducibility_v1.zip

## Because several archives exceed 100 MiB

Use a local clone plus Git LFS (or GitHub Desktop with Git LFS support), not GitHub's browser uploader.

Example command-line workflow after cloning the repository:

    git lfs install
    git lfs track "*.zip" "*.gz" "*.drup" "*.drat" "*.lrat"
    # copy files into the destinations above
    git add .gitattributes repro-v1/evidence/archives repro-v1/evidence/reports releases
    git commit -m "Add preserved binary evidence archives"
    git push origin main

After copying, verify the bytes against `MANUAL_UPLOAD_SHA256SUMS.txt` before or after the push.

Do not rename evidence files unless the corresponding ledger paths/hashes are updated.
