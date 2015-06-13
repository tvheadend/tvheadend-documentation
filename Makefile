#
# Tvheadend documentation makefile
# Copyright (C) 2015 Jaroslav Kysela
#
# Makefile Licence: WTFPL 2
#

# valid TVHVERSION values: 4.0 4.2

TVHVERSION?=4.2
LANGUAGES?=en cs

SOURCES=$(wildcard docs/*.md docs/webui/*.md docs/Appendices/*.md)
YAMLS=  $(foreach l,$(LANGUAGES),mkdocs/$(l)/mkdocs.yml)
TVHMD=./tvhmd.py
TVHMD_VER=$(TVHMD) --tvhversion=$(TVHVERSION)
MSGMERGE?=msgmerge
MKDOCS?=mkdocs

ifeq ($(TVHVERSION),4.0)
SOURCES:=$(filter-out docs/webui/config_passwords.md,$(SOURCES))
endif

ifeq ($(LEVEL2),yes)

RSOURCES=$(subst docs/,,$(SOURCES))
POTS=    $(foreach f,$(RSOURCES),intl/$(f)/$(basename $(notdir $(f))).pot)
POS=     $(foreach f,$(RSOURCES),$(foreach l,$(LANGUAGES),intl/$(f)/$(basename $(notdir $(f))).$(l).po))
MDS=     $(foreach f,$(RSOURCES),$(foreach l,$(LANGUAGES),build/$(l)/$(f)))
WEBUIS=  $(foreach f,$(RSOURCES),$(foreach l,$(LANGUAGES),webui/$(l)/$(basename $(f)).html))
SITES=   $(foreach l,$(LANGUAGES),mkdocs/$(l)/site/index.html)

-include Makefile.rules

define do_pot
	@printf "Building $(2)\n"
	@$(TVHMD) --format=pot "--in=$(1)" "--out=$(2).new"
	@mv "$(2).new" "$(2)"
endef

define do_po
	@printf "Building $(2)\n"
	@if ! test -r "$(2)"; then \
	   cp "$(1)" "$(2).new"; \
	 else \
	   $(MSGMERGE) -o "$(2).new" "$(2)" "$(1)"; \
	 fi
	@mv "$(2).new" "$(2)"
endef

define do_md
	@printf "Building $(2)\n"
	@$(TVHMD_VER) --format=lang-md "--in=$(1)" "--po=$(4)" "--out=$(2).new"
	@mv "$(2).new" "$(2)"
endef

define do_webui
	@printf "Building $(2)\n"
	@$(TVHMD_VER) --format=lang-html "--in=$(1)" "--out=$(2).new"
	@mv "$(2).new" "$(2)"
endef

define do_yml
	@printf "Building $(2)\n"
	@$(TVHMD_VER) --format=lang-yml "--in=$(1)" "--po=$(4)" "--out=$(2).new"
	@mv "$(2).new" "$(2)"
endef

define do_site
	@printf "Building $(1)/site\n"
	@ln -sf "../../build/$(3)" "$(1)/docs"
	@cd "$(1)" && mkdocs build
endef

all: $(POTS) $(POS) $(MDS) $(WEBUIS)
	@echo "Finished"

.PHONY: mkdocs
mkdocs: $(MDS) intl/mkdocs/mkdocs.pot $(YAMLS) $(SITES)
	@echo $(SITES)

intl/mkdocs/mkdocs.pot: mkdocs.yml
	@printf "Building $@\n"
	@$(TVHMD) --format=yml-pot "--in=$<" "--out=$@.new"
	@mv $@.new $@

else

all: Makefile.rules
	@$(MAKE) LEVEL2=yes all

.PHONY: mkdocs
mkdocs: Makefile.rules
	@$(MAKE) LEVEL2=yes mkdocs

endif

.PHONY: clean
clean:
	find . -name "*~" -exec rm -f {} \;
	rm -rf build webui mkdocs Makefile.rules

Makefile.rules: Makefile Makefile.rules.py $(SOURCES)
	@./Makefile.rules.py --out=Makefile.rules.new \
	  "--mds=$(SOURCES)" "--ymls=$(YAMLS)"
	@mv Makefile.rules.new Makefile.rules
