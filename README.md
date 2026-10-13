# codejson-action-e2e

A disposable sandbox for end-to-end testing the [automated-codejson-generator](https://github.com/DSACMS/automated-codejson-generator) GitHub Action against a real repository.

Nothing here is a product. The repository holds just enough to give the action something to work on, and the e2e workflow resets it after every run.

## What's here

- `e2e/sample/textstats.py`: a small Python text-statistics module (word counts, word frequencies, sentence and word lengths, lexical diversity). It exists so `scc` has real source code to measure for `laborHours` and `languages`.
- `e2e/fixtures/`: the `code.json` files the workflow stages before each scenario. `code.json.good` is the known good baseline, and the others each test one behaviour of the action.
- `code.json`: the live metadata file. The workflow overwrites it during a run and restores it from `code.json.good` afterwards.
- `.github/workflows/e2e.yml`: the end-to-end workflow.

## How it runs

Pull requests in automated-codejson-generator dispatch `e2e.yml` here with the commit to test. The workflow builds the action from that commit and runs it against this repository. It covers validation, opening a pull request, pushing directly to `main`, the agency schema input, and AI enrichment. It checks the outcome of each scenario, then closes any `code-json-*` pull requests, deletes their branches, and resets `code.json` on `main`.

Runs share this repository, so they queue rather than run in parallel. Don't keep anything here that you'd mind the workflow overwriting.

## Policies

We adhere to the [CMS Open Source Policy](https://github.com/CMSGov/cms-open-source-policy). For security reports, see [SECURITY.md](SECURITY.md).

## Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).
