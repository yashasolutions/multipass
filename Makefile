##
# Mulipost
#
# @file
# @version 0.1

.PHONY: build install all

:all: build install

build:
	@echo "Building..."
	@pyinstaller --noconfirm --name=mulipost --collect-data TKinterModernThemes app.py

install:
	@echo "Installing..."
	@cp dist/mulipost ~/.local/share/mulipost
	@ln -s ~/.local/share/mulipost/mulipost ~/.local/bin/mulipost



# end
