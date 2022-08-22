for data in $@
do
	if ! [ -e $data ]; then

		mkdir $data

	else
		echo "La carpeta ya existe"

	fi

done
