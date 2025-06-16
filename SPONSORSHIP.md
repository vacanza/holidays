# Open World Holidays Framework Sponsorship Program

The Open World Holidays Framework is launching a year-round sponsorship program to reward meaningful, independent contributions based on task complexity. Sponsored tasks are open year-round and tiered by complexity and available budget. We aim to reward meaningful work fairly while encouraging long-term engagement beyond specific coding events.

- [Program Goals](#program-goals)
- [Current Funding](#current-funding)
- [Sponsorship Amounts](#sponsorship-amounts)
- [Eligibility](#eligibility)
- [Application and Selection Process](#application-and-selection-process)
- [Payment Process](#payment-process)
- [For Potential Sponsors](#for-potential-sponsors)
- [FAQ](#faq)
- [Contact](#contact)

## Program Goals

- Encourage ongoing, impactful contributions from developers and holiday data researchers
- Provide fair compensation for time-intensive tasks
- Support the long-term sustainability and growth of the framework

## Current Funding

This program is currently supported through the [Tidelift Maintainer Program](https://tidelift.com/lifter/search/pypi/holidays), where we receive compensation based on the usage and maintenance of the `holidays` Python package. We are reinvesting these earnings to sponsor contributions to the Open World Holidays Framework.

We are actively exploring additional sources of funding and will provide updates as new opportunities arise (at least on a monthly basis).

## Sponsorship Amounts

The amount sponsored will vary depending on the complexity of the task:

| Task Size | Description                                                                                    | Compensation |
| --------- | ---------------------------------------------------------------------------------------------- | ------------ |
| Medium    | Tasks such as implementing holidays for a new entity using well-established templates or rules | \$25 USD     |
| Hard       | Tasks requiring deeper research, localization, or custom rule logic                           | \$50 USD     |

### Sponsorship Amounts Notes

- These rates are contingent on available funding and **do not cover any fees** charged by payment processors or platforms.
- By default, tasks are classified as `sponsorship-medium`, unless a maintainer explicitly labels them as `sponsorship-hard`.
- A task may be **reclassified as `sponsorship-hard` at the maintainer’s discretion, based on its complexity or scope.

## Eligibility

To participate in the sponsorship program, contributors must:

- Have successfully implemented at least one entity’s holiday support (not necessarily through the sponsorship program)
- Not be currently receiving payment through other structured coding programs (e.g., GSoC, Outreachy)
- Have a GitHub Sponsors account set up and eligible to receive payments (check [GitHub’s supported countries](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors#supported-regions-for-github-sponsors))

### Eligibility Notes

- If the GitHub Sponsors program is not available for the contributor's country, we may consider **alternative payment options** (e.g., crypto payments in USDT) on a **case-by-case basis**.
- Maintainers may specify additional eligibility requirements for specific entities or tasks. These may include familiarity with the country or region in question, native language proficiency, or relevant domain knowledge to ensure the accuracy and quality of the contribution.

## Application and Selection Process

To apply for a sponsored issue, simply comment on the issue expressing your interest in working on it. Please make sure the issue is labeled as eligible for the program (e.g. [sponsorship](https://github.com/vacanza/holidays/issues?q=state:open%20label:sponsorship), [sponsorship-medium](https://github.com/vacanza/holidays/issues?q=state:open%20label:sponsorship:medium), [sponsorship-hard](https://github.com/vacanza/holidays/issues?q=state:open%20label:sponsorship:hard). Each sponsored issue will remain open for applications for at least **7 days** to give all eligible contributors a fair opportunity to participate.

Before applying, please ensure that you meet the eligibility requirements:

- You must have **at least one merged pull request** that adds support for a new entity’s holidays.

If more than one eligible contributor expresses interest, we will review each applicant’s prior contributions and sponsorship participation history. Priority will be given to **new eligible contributors** who have not yet participated in the sponsorship program. This helps ensure a fair and balanced distribution of sponsored tasks across the community.

A previously sponsored contributor will not be assigned to a new task if there is another eligible contributor who has not yet had the opportunity to participate.

All applications from eligible contributors will be considered, and the issue will be assigned to one selected contributor for sponsored work. Only after the issue is officially assigned (i.e., your GitHub username appears in the assignee field) should work begin. Starting work prematurely does not provide any advantage during the selection process. If you are unsure about the assignment status or have any questions, please contact the project maintainers (see the [Contact](#contact) section).

## Payment Process

- **Our preferred method of payment is GitHub Sponsors**
- Payments are processed after the sponsored task is officially released, typically on the **1st and 3rd Monday of each month**
- Contributors are responsible for setting up and maintaining their payment details in GitHub Sponsors or any approved alternative method
- **We do not cover any transaction or processing fees** imposed by [GitHub Sponsors](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors#about-github-sponsors), banks, or other platforms. The amounts listed in the [Sponsorship Amounts](#sponsorship-amounts) section represent the **maximum compensation per task before fees**
- A **transaction confirmation number** will be sent directly to the contributor via private Slack message once the payment has been processed.

## For Potential Sponsors

We welcome additional financial support from individuals and organizations who believe in the mission of Open World Holidays Framework and want to help sustain high-quality open source contributions. The easiest way to contribute to our sponsorship fund is via: [Open Collective – Open World Holidays Framework](https://opencollective.com/open-world-holidays-framework). To recognize your support, all sponsors who contribute $100 USD or more will be acknowledged in the project's README.md file.

Your contributions help expand our budget, allowing us to sponsor more contributors and cover a wider range of countries, regions, and entities. Thank you for helping us grow the Open World Holidays Framework community.

## FAQ

**Q: GitHub payment isn't available in my country. What are my options?**  
**A:** We rely on GitHub Sponsors payments as our main payment option. We may consider offering an alternative crypto payment (USDT) on a case-by-case basis.

**Q: What is the difference between medium and hard tasks?**  
**A:**

- Medium task example: [PR #2525](https://github.com/vacanza/holidays/pull/2525)
- Hard task example: [PR #2386](https://github.com/vacanza/holidays/pull/2386)

**Q: Can I work on multiple sponsored tasks simultaneously?**  
**A:** No, one person can work on a single sponsorship-eligible issue at a time.

**Q: What happens if I cannot complete my task within the deadline?**  
**A:** We provide reasonable deadlines:

- Any task must be completed within 6 weeks of the start date
- A draft PR must be submitted within the first 2 weeks

If these requirements are not met, the contributor will be unassigned and **no payment will be issued**.

**Q: Are there any tax implications I should be aware of?**  
**A:** Contributors are entirely responsible for handling any applicable taxes in their local jurisdiction.

**Q: How are tasks prioritized for sponsorship?**  
**A:** We prioritize based on existing community interest. If no specific entity has been requested, we typically proceed alphabetically or focus on uncovered one-off entities.

**Q: Are my previous contributions eligible for sponsorship payments?**  
**A:** No, previously submitted pull requests are not eligible for sponsorship. Only contributions linked to issues explicitly labeled with sponsorship are considered part of the program. These issues will also include a label indicating their complexity or the associated payment amount.

**Q: What are the acceptance criteria for a sponsored task to be eligible for payment?**  
**A:** To be eligible for payment, the pull request must be successfully merged into the dev branch. This typically requires 100% test coverage (in line with the current project standard) and adherence to strict code style and quality guidelines. Please refer to our contributing guide and recently merged PRs for examples. These standards help maintain the high quality of a project used by millions, with over 10 million downloads per month.

**Q: Is there a limit to the number of sponsorship-eligible pull requests a contributor can complete per month?**  
**A:** There is no fixed limit on the number of sponsorship-eligible pull requests a contributor can complete per month. However, to ensure fair distribution of available tasks, contributors may only work on one sponsored task at a time. Priority is given to new eligible contributors who have not yet participated in the program. As long as you meet the eligibility criteria and follow the assignment process, you’re welcome to continue contributing.

## Contact

To express interest in joining the sponsorship program or if you have any questions, please:

- [Open an issue](https://github.com/vacanza/holidays/issues/new) on our GitHub repository
- Contact maintainers via [Discussions](https://github.com/vacanza/holidays/discussions/2545)
- Join our [Slack](https://join.slack.com/t/vacanza-team/shared_invite/zt-31jz9je5t-dl0vayg0iJ3DEzDh82~8Sg) and reach out to the maintainers at [#sponsorship](https://vacanza-team.slack.com/archives/C08S8394T4N) channel

---

We appreciate your support in helping us build a comprehensive, accessible, and reliable global holiday framework for all.
