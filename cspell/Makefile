.PHONY: cspell-install cspell-check sort-custom-dict

cspell-install:
	@command -v docker > /dev/null 2>&1 || (echo "ERROR: docker not found in PATH. Install Docker."; exit 1)
	@DOCKER_BUILDKIT=1 docker build \
	$(if $(FORCE),--no-cache,) \
	-f cspell/Dockerfile \
	cspell \
	-t cspell

cspell-check: CMD=--no-progress --cache --cache-location /cspellcache/cache -r /holidays
cspell-check: cspell-install
	@mkdir -p "$(CURDIR)/cspell/.cspellcache"
	@docker run \
	--user "$(shell id -u):$(shell id -g)" \
	--mount type=bind,src="$(CURDIR)",dst=/holidays,readonly \
	--mount type=bind,src="$(CURDIR)/cspell/.cspellcache",dst=/cspellcache \
	--rm \
	cspell lint -c cspell/cspell.json $(CMD)

# Prefer the project-local uv (pinned via the ci dependency group) when present.
# Invoked with -f from the repo root, so paths here are root-relative, same as Makefile.
UV = $(if $(wildcard .venv/bin/uv),.venv/bin/uv,uv)
UV_RUN_CMD = $(UV) run --no-sync

sort-custom-dict:
	@$(UV_RUN_CMD) tools/sort_cspell_dict.py
