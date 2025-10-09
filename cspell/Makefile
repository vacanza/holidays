.PHONY: cspell-install cspell-check cspell-run sort-custom-dict

cspell-install:
	@which docker > /dev/null 2>&1 || (echo "ERROR: docker not found in PATH. Install Docker."; exit 1)
	@DOCKER_BUILDKIT=1 docker build \
	$(if $(FORCE),--no-cache,) \
	-f cspell/Dockerfile \
	cspell \
	-t cspell

cspell-check: CMD=--no-progress -r /holidays
cspell-check: cspell-install cspell-run

	@docker run \
	--mount type=bind,src="$(CURDIR)",dst=/holidays,readonly \
	--rm \
	cspell lint -c cspell/cspell.json $(CMD)

sort-custom-dict:
	@python tools/sort_cspell_dict.py
