#!/usr/bin/env bash

# INIT GLOBAL VARIABLES:
_VERSION="2.0"
_SCRIPT_NAME="$0"
_THEME_SRC_PATH="src"
_SYSTEM_CONF_PATH="/usr/share/Kvantum"
_USER_CONF_PATH="$HOME/.config/Kvantum"
_NO_ASK=false


help() {
	script=$_SCRIPT_NAME
	printf "Usage: ${script} [options]                                      \n"
	printf "                                                                \n"
	printf "Options:                                                        \n"
	printf "                                                                \n"
	printf " --no-ask    | -na  don't ask for confirmation                  \n"
	printf " --build     | -b   {theme_name}                                \n"
	printf " --install   | -i   {theme_name}                                \n"
	printf " --uninstall | -u   uninstall theme                             \n"
	printf " --version   | -v   print version                               \n"
	printf " --help      | -h   print this message and exit                 \n"
	printf "                                                                \n"
	printf "Examples:                                                       \n"
	printf "                                                                \n"
	printf "${script} --build nord    the nord theme will be built          \n"
	printf "${script} --install       the default theme will be installed   \n"
	printf "${script} --install nord  the nord theme will be installed      \n"
	printf "${script} --install custom ~/my-base16.json                     \n"
	printf "${script} --uninstall     the default theme will be uninstalled \n"
}


abort() {
	local abort_message=$1
	echo $abort_message
	exit 1
}


continue_handler() {
    local message=$1
    local abort_message=$2
    
    echo "${message}"
	read -p "Continue? (Y/N): " confirm \
	&& [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || abort "${abort_message}"
}


build() {
	local theme="$1"
	local custom_theme_path="$2"

	if [ "${theme}" == "custom" ]; then
		echo "${custom_theme_path}"
		python3 "gradience/gradience.py" "--custom" $custom_theme_path
	else
		python3 "gradience/gradience.py" "--theme" $theme
	fi
	if [ $? -ne 0 ]; then
		local abort_msg="Installation aborted"
		abort "${abort_message}"
	fi
}


install() {
    local theme="$1"
	local custom_theme_path="$2"
	local src_path="${_THEME_SRC_PATH}"  # default source path
    local dst_path="${_USER_CONF_PATH}"  # default destination path
    local abort_msg="Installation aborted"
	local success_msg="Installation complete"
	local gradience_msg=""

    if ! [ -z "${theme}" ] && ! [ "${theme}" == "adwaita" ]; then
        src_path="gradience/result"
		gradience_msg="with gradience ${theme} "
	else
		theme="adwaita"
    fi

    if [ "$EUID" -eq 0 ]; then
        dst_path="${_SYSTEM_CONF_PATH}"
	fi

	if ! $_NO_ASK; then
		local msg="Install KvLibadwaita ${gradience_msg}in ${dst_path}?"
		continue_handler "${msg}" "${abort_msg}"
	fi

	if [ "${theme}" == "adwaita" ]; then
		cp -r $src_path/* $dst_path
	else
		build "${theme}" "${custom_theme_path}"
		cp -r $src_path/* $dst_path
	fi
	echo "${success_msg}"
}


uninstall() {
	local dst_path="${_USER_CONF_PATH}"  # default destination path
	local abort_msg="Uninstallation aborted"
	local success_msg="Uninstallation complete"

    if [ "$EUID" -eq 0 ]; then
        dst_path="${_SYSTEM_CONF_PATH}"
	fi

	if ! $_NO_ASK; then
		local msg="Uninstall KvLibadwaita from ${dst_path}?"
		continue_handler "${msg}" "${abort_msg}"
	fi

	rm -r $dst_path/KvLibadwaita
	echo "${success_msg}"
}


# Parse user options
optparser() {
	# count user-passed options:
	local count_options=$#
	# run help if empty and exit:
	if [[ count_options -eq 0 ]]; then
		# help
        help
		exit 2
	fi
	# parse opts:
	while [ ! -z "$1" ]; do
		case "$1" in
			--no-ask|-na)
				_NO_ASK=true
				;;		
			--build|-b)
				shift
				build $1 $2
				exit 0
				;;
			--install|-i)
				shift
				install $1 $2
				exit 0
				;;
			--uninstall|-u)
				uninstall
				;;
			--help|-h)
				help
				exit 0
				;;
			--version|-v)
				echo "${_VERSION}"
				exit 0
				;;
			*)
                help
                exit 1
                ;;
		esac
	shift
	done
}


main() {
    optparser "$@"
}


# RUN IT:
main "$@"
