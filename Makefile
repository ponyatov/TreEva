CWD    = $(CURDIR)
MODULE = $(notdir $(CWD))

NOW = $(shell date +%d%m%y)
REL = $(shell git rev-parse --short=4 HEAD)



all: doxy run



run: TreEva.py
	python3 $^



doxy:
	rm -rf docs ; doxygen doxy.gen 1> /dev/null



MERGE  = Makefile README.md doxy.gen
MERGE += TreEva.py

merge:
	git checkout master
	git checkout shadow -- $(MERGE)
	$(MAKE) doxy

release:
	git tag $(NOW)-$(REL)
	git push -v && git push -v --tags
	git checkout shadow
