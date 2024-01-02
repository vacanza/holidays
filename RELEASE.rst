How to release a new version of Python Holidays
===============================================

- Finalize the current development version

  - switch to ``beta`` branch and pull the most recent changes
    from https://github.com/vacanza/python-holidays remote ``beta`` branch.
  - generate release notes by running the following script
    ``scripts/generate_release_notes.py -t <version>``, where <version> is the
    value of tag/version you're going to release, e.g. 0.39
  - insert the script's output into the top of ``CHANGES`` file
    (see previous release notes for consistent formatting)
  - commit the updated ``CHANGES`` file to ``beta`` branch with the following
    commit message 'Finalize v<version>', e.g. 'Finalize v0.39'
  - push changes to https://github.com/vacanza/python-holidays ``beta`` branch
  - make sure the push related CI/CD job(s) have been completed successfully

- Merge the finalized changes into ``master`` branch:

  - create a new PR for the recent changes from ``beta`` to ``master`` branch
    using 'v<version>' as a PR title and the previously generated release notes
    as a PR description
  - get the PR reviewed by at least one of the code owners
  - merge the PR into ``master`` branch with 'Create a merge commit' action
    (**do not use 'Squash and merge'**)
  - make sure the PR related CI/CD job(s) have been completed successfully
  - make sure readthedocs.org documentation build jobs at
    https://readthedocs.org/projects/python-holidays/builds/
    have been completed successfully

- Create a new release:

  - open https://github.com/vacanza/python-holidays/releases page and click
    on the 'Draft a new release' button
  - click on 'Choose a tag', enter 'v<version>' into the input field
    (you should see something like 'Create a new tag: v0.39' on publish'
  - select **master** - instead of default ``beta`` in 'Target' dropdown
  - put 'v<version>' into 'Release title' field, e.g. 'v0.39'
  - click on 'Generate release notes' button to collect new contributors and
    full changelog link information (we normally keep it at the bottom with
    a bit of re-formatting)
  - replace auto-generated release notes with the previously generated release
    notes (keep the new contributors and full changelog link)
  - check/uncheck the 'Set as the latest release' checkbox depending on the
    release status
  - save the draft (do not publish it yet)
  - preview the release on https://github.com/vacanza/python-holidays/releases
  - after making sure everything looks right click 'Edit' and then
    'Publish release'

- Verify the new release:

  - make sure the release related CI/CD job(s) have been completed successfully
  - check https://pypi.org/project/holidays/ package page -- it should have
    the current version and the released date updated

- Finish the process with the following post-release actions:

  - send "Python Holidays 'v<version>' has been released!" (or similar) message
    to Vacanza Team Slack #release channel
  - pull the recent changes from ``master`` branch into ``beta``
  - bump the Python Holidays version at ``holidays/__init__.py`` file
  - create a commit with 'Initialize v<version>' message, e.g.
    'Initialize v0.40' and push it to ``beta`` branch (this may require
    running ``make package`` to pass the tests locally)
  - make sure ``beta`` branch **is not behind** the master branch (there
    will be a message on top of the
    https://github.com/vacanza/python-holidays/tree/beta page in case it is)
  - make sure the push related CI/CD job(s) have been completed successfully
