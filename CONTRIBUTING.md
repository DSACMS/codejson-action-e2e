# How to Contribute

We're so thankful you're considering contributing to an [open source project of
the U.S. government](https://code.gov/)! If you're unsure about anything, just
ask -- or submit the issue or pull request anyway. The worst that can happen is
you'll be politely asked to change something. We appreciate all friendly
contributions.

We encourage you to read this project's CONTRIBUTING policy (you are here), its
[LICENSE](LICENSE), and its [README](README.md).

## Getting Started

This repository only tests [automated-codejson-generator](https://github.com/DSACMS/automated-codejson-generator). Most changes to the action need no change here. Contribute here when a change to the action needs a new or different end-to-end scenario.

### Team Specific Guidelines

The maintainers are listed in [COMMUNITY.md](COMMUNITY.md). Changes here usually go together with a pull request in automated-codejson-generator, so link to it.

### Building dependencies

Nothing to install beyond the [GitHub CLI](https://cli.github.com/), which you need to dispatch the workflow. The workflow builds the action's Docker image itself.

### Building the Project

There is no build. The workflow checks out the action at the commit you give it and builds it with `docker build`.

### Workflow and Branching

Every e2e run from the action's pull requests uses `e2e.yml` on `main`, so a broken change on `main` breaks every pull request there. To change the workflow or a fixture:

1. Create a branch from `main`.
2. Make your change and push the branch.
3. Dispatch the workflow from your branch against a known good commit of the action:

   ```sh
   gh workflow run e2e.yml --repo DSACMS/codejson-action-e2e --ref <your-branch> \
     -f action_sha=<commit> -f pr_number=<pr> -f correlation_id=manual-1
   ```

4. Check that every step passes, and that the sandbox is clean afterwards: no `code-json-*` branches, and `code.json` on `main` matches `e2e/fixtures/code.json.good`.
5. Open a pull request against `main` and link the passing run.

### Testing Conventions

Each scenario stages a fixture from `e2e/fixtures/`, runs the action, and then asserts on what actually happened (the action's outputs, the pull request it opened, or the commit on `main`), not on its exit code. The action can exit 0 without having done anything, so the exit code proves nothing.

Scenarios check the flow, not the details. A scenario should prove the action ran end to end and that its inputs reached the code. Merge rules and field-level behaviour belong in the action's unit tests.

### Coding Style and Linters

- Assertion steps start with `set -euo pipefail`.
- The reset step leaves out `-e` so that every cleanup is attempted.
- A failed assertion prints a `::error::` line saying what went wrong.
- Comments explain why a step exists, not what it does.

### Writing Issues

Report problems with the action itself in [automated-codejson-generator's issues](https://github.com/DSACMS/automated-codejson-generator/issues). Open an issue here only for problems with the e2e workflow or the sandbox. Include a link to the failing run.

### Writing Pull Requests

Follow the [pull request template](.github/PULL_REQUEST_TEMPLATE.md). In the Test Plan section, link the manual run from your branch.

### Reviewing Pull Requests

Reviewers check that the linked run passed and that the sandbox was left clean afterwards.

## Shipping Releases

This repository isn't released. A change takes effect when it merges to `main`.

## Documentation

Improvements to these docs are welcome. Please file an [issue](https://github.com/DSACMS/codejson-action-e2e/issues) or open a pull request.

## Policies

### Open Source Policy

We adhere to the [CMS Open Source
Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any
questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

_Submit a vulnerability:_ Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

For more information about our Security, Vulnerability, and Responsible Disclosure Policies, see [SECURITY.md](SECURITY.md).

## Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.
