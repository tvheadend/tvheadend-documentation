#
# Tvheadend documentation makefile
# Copyright (C) 2015 Jaroslav Kysela
#
# Makefile Licence: WTFPL 2
#

LANGUAGES?=en cs
SOURCES=$(wildcard docs/*.md docs/webui/*.md)
TVHMD=./tvhmd.py
MSGMERGE?=msgmerge

ifeq ($(LEVEL2),yes)

RSOURCES=$(subst docs/,,$(SOURCES))
POTS=    $(foreach f,$(RSOURCES),intl/$(f)/$(basename $(notdir $(f))).pot)
POS=     $(foreach f,$(RSOURCES),$(foreach l,$(LANGUAGES),intl/$(f)/$(basename $(notdir $(f))).$(l).po))
MDS=     $(foreach f,$(RSOURCES),$(foreach l,$(LANGUAGES),build/$(l)/$(f)))
WEBUIS=  $(foreach f,$(RSOURCES),$(foreach l,$(LANGUAGES),webui/$(l)/$(basename $(f)).html))

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
	@$(TVHMD) --format=lang-md "--in=$(1)" "--po=$(4)" "--out=$(2).new"
	@mv "$(2).new" "$(2)"
endef

define do_webui
	@printf "Building $(2)\n"
	@$(TVHMD) --format=lang-html "--in=$(1)" "--out=$(2).new"
	@mv "$(2).new" "$(2)"
endef

all: $(POTS) $(POS) $(MDS) $(WEBUIS)
	@echo "Finished"

else

all: Makefile.rules
	@$(MAKE) LEVEL2=yes all
	@echo $(TARGETS)

endif

.PHONY: clean
clean:
	find . -name "*~" -exec rm -f {} \;
	rm -rf build webui

Makefile.rules: Makefile Makefile.rules.py $(SOURCES)
	@./Makefile.rules.py --out=Makefile.rules.new $(SOURCES)
	@mv Makefile.rules.new Makefile.rules
