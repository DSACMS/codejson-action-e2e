# codejson-action-e2e

A disposable sandbox for end-to-end testing the [automated-codejson-generator](https://github.com/DSACMS/automated-codejson-generator) GitHub Action against a real repository.

Nothing here is a product. The repository holds just enough to give the action something to work on, and the e2e workflow resets it after every run.

## About the Project

### Project Vision

Every change to automated-codejson-generator is proven against a live GitHub repository before it ships, not just in unit tests.

### Project Mission

Run the action from each pull request's own code, in each of its modes, against a real repository, and fail the pull request if the action doesn't do what it claims.

### Agency Mission

The CMS Open Source Program Office helps CMS share its source code and metadata openly, including the `code.json` inventory files required under the SHARE IT Act. automated-codejson-generator keeps those files current, and this sandbox keeps that tool reliable.

### Team Mission

Keep the `code.json` tooling trustworthy enough that CMS teams can adopt it without checking its output by hand.

## Core Team

The people responsible for this repository are listed in [COMMUNITY.md](COMMUNITY.md), and code ownership is in [CODEOWNERS.md](.github/CODEOWNERS.md).

## Repository Structure

- `e2e/sample/textstats.py`: a small Python text-statistics module (word counts, word frequencies, sentence and word lengths, lexical diversity). It exists so `scc` has real source code to measure for `laborHours` and `languages`.
- `e2e/fixtures/`: the `code.json` files the workflow stages before each scenario. `code.json.good` is the known good baseline, and the others each test one behaviour of the action.
- `code.json`: the live metadata file. The workflow overwrites it during a run and restores it from `code.json.good` afterwards.
- `.github/workflows/e2e.yml`: the end-to-end workflow.

## How it runs

Pull requests in automated-codejson-generator dispatch `e2e.yml` here with the commit to test. The workflow builds the action from that commit and runs it against this repository. It covers validation, opening a pull request, pushing directly to `main`, the agency schema input, and AI enrichment. It checks the outcome of each scenario, then closes any `code-json-*` pull requests, deletes their branches, and resets `code.json` on `main`.

Runs share this repository, so they queue rather than run in parallel. Don't keep anything here that you'd mind the workflow overwriting.

## Local Development

There's nothing to build here. To run the e2e workflow by hand against a commit of the action:

```sh
gh workflow run e2e.yml --repo DSACMS/codejson-action-e2e \
  -f action_sha=<commit> -f pr_number=<pr> -f correlation_id=manual-1
```

To change what a scenario tests, edit the fixture in `e2e/fixtures/` or the matching step in `e2e.yml`. Keep `code.json.good` and `code.json` on `main` identical, because the reset step treats any difference as something to undo.

## Coding Style and Linters

Assertion steps in `e2e.yml` run under `set -euo pipefail`. The reset step deliberately leaves out `-e` so that every cleanup runs. Each assertion prints a `::error::` line that says what went wrong before it exits.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Community

This repository serves the automated-codejson-generator community. Questions and ideas about the action belong in [its issues](https://github.com/DSACMS/automated-codejson-generator/issues).

### Community Guidelines

Principles and guidelines for participating are in [COMMUNITY.md](COMMUNITY.md), and everyone is expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Policies

### Open Source Policy

We adhere to the [CMS Open Source Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

_Submit a vulnerability:_ Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

For more information, see [SECURITY.md](SECURITY.md).

## Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.
