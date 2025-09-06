.PHONY: cspell-install cspell-check cspell-run

cspell-install:
	@DOCKER_BUILDKIT=1 docker build \
	$(if $(FORCE),--no-cache,) \
	-f cspell/Dockerfile \
	. \
	-t cspell

cspell-check: CMD=--no-progress -r /holidays
cspell-check: cspell-install cspell-run

	@docker run \
	--mount type=bind,src="$(CURDIR)",dst=/holidays \
	--rm \
	cspell -c cspell/cspell.json $(CMD)
