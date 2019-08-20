#!/bin/bash

heuristic_case() {
case "$1" in
	################################
	###       Modify here!       ###
	###                          ###
	###  Possible variables are: ###
	###    -task (required)      ###
	###    -rec                  ###
	###    -acq                  ###
	###    -dir                  ###
	###                          ###
	###                          ###
	###    See example below     ###
	################################

	origfilename1 ) task=newname1 ;;
	origfilename2 ) task=newname2; run=runnum ;;
	BH4 ) task=breathhold ;;
	MOTOR? ) task=motor ;;
	PINEL? ) task=pinel ;;
	SIMON? ) task=simon ;;
	BH4 ) task=breathhold ;;
	RS1 ) task=rest; run=01 ;;
	RS2 ) task=rest; run=02 ;;
	RS3 ) task=rest; run=03 ;;
	RS4 ) task=rest; run=04 ;;

	################################
	### Don't modify below this! ###
	################################
	* ) echo "Something's wrong here, can't find $1 !"; exit 1 ;;

esac

name="${2}_task-${task}"

if [ ${run} ]; then name="${name}_run-${run}"; fi
if [ ${rec} ]; then name="${name}_rec-${rec}"; fi
if [ ${acq} ]; then name="${name}_acq-${acq}"; fi
if [ ${dir} ]; then name="${name}_dir-${dir}"; fi

name="${name}_physio"

export ${name}
}

check_dir() { if [ ! -d $1 ]; then mkdir $1; fi }

#${heur} ${in::-4} ${odir} ${sub} ${ses}
in=$1
odir=$2
name=$3
ses=$4

if [ ${name:0:3} != sub ]; then name="sub-${name}"; fi
fld=${name}
check_dir ${odir}${fld}

if [ ${ses} ]
then
	fld="${fld}/ses-${ses}"
	check_dir ${odir}${fld}
	name="${name}_ses-${ses}"
fi

name="$( heuristic_case ${in} ${name} )"
fld="${fld}/func"
check_dir ${odir}${fld}

echo "Files ${odir}${in}.* will be moved to:"
echo "   ${fld}/${name}.*"

if [ -e ${odir}${in}.tsv.gz ]; then mv ${odir}${in}.tsv.gz ${fld}/${name}.tsv.gz; fi
if [ -e ${odir}${in}.json ]; then mv ${odir}${in}.json ${fld}/${name}.json; fi