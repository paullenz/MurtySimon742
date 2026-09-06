# Prepared GitHub Release instructions

The reviewer package and its repository record are prepared. A GitHub Release page has not been created by the assistant: the connected GitHub tools do not expose release creation or release-asset uploads. These are the remaining interface steps for Paul.

1. Fetch the latest `paullenz/MurtySimon25` changes in GitHub Desktop so the updated README and `releases/n25-reviewer-v1` folder are visible.
2. In the repository's GitHub website, open **Releases**, then **Draft a new release**. Use the tag `n25-reviewer-v1`, targeting the commit that added this reviewer edition. Confirm that commit contains the updated README and the reviewer folder.
3. Use the title **N25 reviewer edition 1 — candidate proof awaiting independent review** and the prepared release text below. Mark it as a **pre-release**.
4. Attach the intact `N25_Reviewer_Package_v1_2026-09-06.zip`, `N25_Reviewer_Manuscript_v1.pdf` and `N25_Reviewer_Package_v1_SHA256.txt` supplied with this edition. The ZIP is small enough for ordinary GitHub upload; no Git LFS setup or multi-gigabyte expanded JSON upload is required.
5. Check the attached ZIP's SHA256 against the receipt. Save the release as a draft while deciding whom to approach, or publish the pre-release within the repository's existing visibility when ready to distribute it. A GitHub publication is not mathematical certification.

GitHub documents ordinary repository browser uploads up to 25 MiB and standard Git files up to 100 MiB. Release assets are a separate distribution mechanism. [Official file-size guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), [official release instructions](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

## Prepared release text

This reviewer edition presents a complete candidate argument for the order-25 Murty–Simon statement: at most 156 edges in a diameter-2-critical graph, with equality exactly for K₁₂,₁₃.

It includes a readable manuscript and editable source, the frozen mathematical evidence, exact hashes, complete numerical replay instructions, all 1,959 final equality rejection certificates, a literature and attribution check, and forms for independent review.

The mathematical development and code involved substantial ChatGPT/Codex assistance. The computations have been internally reproduced, including separately implemented arithmetic checks. Independent mathematical review and an external researcher's fresh reproduction remain OPEN. No novelty, external endorsement, formal verification or theorem-ledger promotion is claimed.

Start with the manuscript PDF and REVIEW_GUIDE.md. Record findings against the exact package version and SHA256, with section/equation references and full computational logs where applicable. Later corrections will be issued as a new version while this edition remains preserved.
