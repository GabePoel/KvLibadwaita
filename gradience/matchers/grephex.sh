#!/usr/bin/env bash


# get hex codes in form #fff and #ffffff
# checks to see if not - especially needed on #fff matches
# FIXME: - currently prints trailing character
color_parser() {
	if [[ ! -a $1 ]]; then
		echo File not found
		exit 1
	fi
	sed ':a;N;$!ba;s/\n/ /g' "$1" | grep -o '\#[0-9a-fA-F]\{3\}[^0-9a-fA-F]' | sed 's/[^0-9a-fA-F#]//g' | sort -u
	sed ':a;N;$!ba;s/\n/ /g' "$1" | grep -o '\#[0-9a-fA-F]\{6\}[^0-9a-fA-F]' | sed 's/[^0-9a-fA-F#]//g' | sort -u
	exit
}


main() {
	color_parser $@
}


# Run IT:
main $@
