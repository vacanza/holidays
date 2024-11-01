How to release a new version of Holidays
========================================

- Finalize the current development version

  - switch to ``dev`` branch and pull the most recent changes
    from https://github.com/vacanza/holidays remote ``dev`` branch.
  - generate release notes by running ``make release-notes``
  - insert the command's output into the top of ``CHANGES`` file
    (see previous release notes for consistent formatting)
  - commit the updated ``CHANGES`` file to ``dev`` branch with the following
    commit message 'Finalize v<version>', e.g. 'Finalize v0.39'
  - push changes to https://github.com/vacanza/holidays ``dev`` branch
  - make sure the push related CI/CD jobs have been completed successfully

- Merge the finalized changes into ``main`` branch:

  - create a new PR for the recent changes from ``dev`` to ``main`` branch
    using 'v<version>' as a PR title and the previously generated release notes
    as a PR description
  - get the PR reviewed by at least one of the code owners
  - merge the PR into ``main`` branch using 'Merge when ready' button
  - make sure the PR related CI/CD jobs have been completed successfully
  - make sure readthedocs.org documentation build jobs at
    https://readthedocs.org/projects/holidays/builds/
    have been completed successfully

- Create a new release:

  - open https://github.com/vacanza/holidays/releases page and click
    on the 'Draft a new release' button
  - click on 'Choose a tag', enter 'v<version>' into the input field
    (you should see something like 'Create a new tag: v0.39' on publish'
  - select **main** - instead of default ``dev`` in 'Target' dropdown
  - put 'v<version>' into 'Release title' field, e.g. 'v0.39'
  - click on 'Generate release notes' button to collect new contributors and
    full changelog link information (we normally keep it at the bottom with
    a bit of re-formatting)
  - replace auto-generated release notes with the previously generated release
    notes (keep the new contributors and full changelog link)
  - check/uncheck the 'Set as the latest release' checkbox depending on the
    release status
  - save the draft (do not publish it yet)
  - preview the release on https://github.com/vacanza/holidays/releases
  - after making sure everything looks right click 'Edit' and then
    'Publish release'

- Verify the new release:

  - make sure the release related CI/CD jobs have been completed successfully
  - check https://pypi.org/project/holidays/ package page -- it should have
    the current version and the released date updated

- Finish the process with the following post-release actions:

  - send "Holidays 'v<version>' has been released!" (or similar) message
    to Vacanza Team Slack #release channel
  - pull the recent changes from ``main`` branch into ``dev``
  - bump the Holidays version at ``holidays/version.py`` file
  - create a commit with 'Initialize v<version>' message, e.g.
    'Initialize v0.40' and push it to ``dev`` branch (this may require
    running ``make package`` to pass the tests locally)
  - make sure ``dev`` branch **is not behind** the ``main`` branch (there
    will be a message on top of the
    https://github.com/vacanza/holidays/tree/dev page in case it is)
  - make sure the push related CI/CD jobs have been completed successfully
