#!/bin/bash
# ------------------------------------------------
# Program:
#       This program is used to be tested.
#       此项目用于测试使用
# History:
#       2022/11/18 周月南 First release
#       2023/02/05 周月南 Second release
# ------------------------------------------------
set -ex
function build_prepare () {
    GIT_URL=test
    return 0
}
function build_check_lang () {
    if [[ "${LC_ALL}" =~ en_US.* ]]; then
        echo "======================== The language set is English! ========================"
    elif [[ "${LC_ALL}" =~ zh_CN.* ]]; then
        echo "======================== The language set is Chinese! ========================"
    elif [[ "${LC_ALL}" == "" ]]; then
        echo "======================== The language set is none! ========================"
    else
        echo "======================== The language set is other language! ========================"
    fi
}
function main () {
    build_prepare
    build_check_lang
}
main