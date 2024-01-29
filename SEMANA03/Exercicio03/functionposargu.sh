#1/bin/bash
showname(){
	echo hello $1
	if [ ${1,,} = Pedro ]; then
		return 0
	else
		return 1
	fi
}
showname $1
if [ $? = 1 ]; then
	echo "Estranhos na area!"
fi
