function help(){

        echo "---Debe incluir tres parametros:posicion inicial, velocidad inicial y tiempo total.---"
}

if ! [ $# -eq 3 ]; then
	help
	exit 1
fi
        echo "corriendo programa"








