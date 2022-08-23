pass=0
i=1
o=0
function checkvalue(){
	if [[ $1 -eq $o ]]
	then	
		let pass=($pass+1)
	
	elif [[ $1 -eq $i ]]
	then	
		let pass=($pass+1)
		
	else
		echo "Por favor, ingrese 0 o 1"
	
	fi
}

while [ $pass -eq $o ]
do
	read n
	checkvalue $n  
done
