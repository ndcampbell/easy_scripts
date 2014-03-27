#!/usr/bin/env bash

#Author: Doug Campbell
#Email: doug.campbell@aardv.com
#Date: 02-28-2014

#Description: Creates headers for a script and then opens in vi
#Usage: scripthead script.ext

###

if [[ $# -ne 1 ]]
then
    echo -e "\nUsage: scripthead scriptname.ext\n"
    exit 1
fi

SCRIPT=$1
CUR_DATE=`date +'%B %d, %Y'`
AUTHOR='Doug Campbell'
EMAIL='ndouglascampbell@gmail.com'

touch $SCRIPT
if [ $(wc -l $SCRIPT |cut -f1 -d' ') -gt 0 ]
then
    echo "${SCRIPT} already exists and has content"
    exit -1
fi

#splits up file based on extension
IFS='.' read -ra EXT <<< "$SCRIPT"

if [ "${EXT[@]:(-1)}" == "py" ]
then
    SHEBANG="#!/usr/bin/env python"

elif [ "${EXT[@]:(-1)}" == "sh" ]
then
    SHEBANG="#!/usr/bin/env bash"

elif [ "${EXT[@]:(-1)}" == "pl" ]
then
    SHEBANG="#!/usr/bin/env perl"

elif [ "${EXT[@]:(-1)}" == "rb" ]
then
    SHEBANG="#!/usr/bin/env ruby"

else 
    SHEBANG=""

fi

HEADER="${SHEBANG}\n\n#Author: ${AUTHOR}\n#Email: ${EMAIL}\n#Date: ${CUR_DATE}\n\n#Description:\n#Usage:\n\n###\n"


echo -e $HEADER > $SCRIPT
vi +12 $SCRIPT

