help:
	@echo "Usage: make <target>"
	@echo "    check         run pre-commit and tests"
	@echo "    coverage      identify code not covered with tests"
	@echo "    doc           run documentation build process"
	@echo "    help          show summary of available commands"
	@echo "    l10n          update .pot and .po files"
	@echo "    package       build package distribution"
	@echo "    pre-commit    run pre-commit against all files"
	@echo "    setup         setup development environment"
	@echo "    test          run tests (in parallel)"

check:
	@$(MAKE) l10n
	@$(MAKE) pre-commit
	@$(MAKE) doc
	@$(MAKE) test

clean: CMD="find . -type f \( -name '*.mo' -o -name '*.pot' -o -name '*.pyc' \) -delete && \
	rm -rf .cache .mypy_cache .pytest_cache .ruff_cache build dist site"
clean: docker-run

coverage: CMD="pytest --cov-report term-missing --no-cov-on-fail"
coverage: docker-run

doc: CMD="mkdocs build"
doc: docker-run

docker-build:
	@DOCKER_BUILDKIT=1 docker buildx use holidays-builder || \
	docker buildx create --use --name holidays-builder && \
	docker buildx build \
		--cache-from=type=local,src=./.buildx-cache \
  		--cache-to=type=local,dest=./.buildx-cache \
		--load \
		. \
		-t holidays > /dev/null 2>&1

docker-run: docker-build
	@docker run \
		-it \
		--mount type=bind,src="$(PWD)",dst=/home/user \
		--rm \
		holidays sh -c $(CMD)

docker-shell: docker-build
	@docker run \
		-it \
		--mount type=bind,src="$(PWD)",dst=/home/user \
		--rm \
		holidays /bin/sh

l10n: CMD="find . -type f -name "*.pot" -delete && \
	scripts/l10n/generate_po_files.py > /dev/null 2>&1 && \
	scripts/l10n/generate_mo_files.py"
l10n: docker-run

package: CMD="scripts/l10n/generate_mo_files.py && python -m build"
package: docker-run

pre-commit: CMD="pre-commit run --all-files"
pre-commit: docker-run

release-notes: CMD="scripts/generate_release_notes.py"
release-notes: docker-run

sbom: CMD="python -m cyclonedx_py requirements requirements/runtime.txt"
sbom: docker-run

setup: \
	$(MAKE) l10n
	$(MAKE) package

snapshot: CMD="scripts/l10n/generate_mo_files.py && scripts/generate_snapshots.py"
snapshot: docker-run

test: CMD="scripts/l10n/generate_mo_files.py && pytest"
test: docker-run
