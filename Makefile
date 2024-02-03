##
# Multipost
#
# @file
# @version 0.1

.PHONY: build install all

:all: build install

build:
	@echo "Building..."
	@pyinstaller --noconfirm --name=multipost --collect-data TKinterModernThemes app.py

install:
	@echo "Installing..."
	@cp dist/multipost ~/.local/share/multipost
	@ln -s ~/.local/share/multipost/multipost ~/.local/bin/multipost



# end
