# This script is developed by cybarone
# PS

shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
clear
python theme.py
PROMPT_DIRTRIM=2
PS1='\n  \e[1;32m┌──(\e[1;94mkali@localhost\e[1;32m)-[\e[1;96m\w\]\e[1;32m]\n  \e[1;32m└──\e[1;94m$\[\e[1;0m '
#xistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
