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
	--mount type=bind,src="$(CURDIR)",dst=/holidays,readonly \
	--mount type=bind,src="$(CURDIR)/cspell/.cspellcache",dst=/cspellcache \
	--rm \
	cspell lint -c cspell/cspell.json $(CMD)

sort-custom-dict:
	@python tools/sort_cspell_dict.py
