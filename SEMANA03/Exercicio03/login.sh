#!/bin/bash

case ${1,,} in
	pedro | admin)
		echo "Salve chefe"
		;;
	help)
		echo "Suspeito"
		;;
	*)
		echo "Pega ladrão ts ts ts"
		;;
esac
