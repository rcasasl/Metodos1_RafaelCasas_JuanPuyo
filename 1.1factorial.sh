echo calcular faactorial de: 
read n
function factorial(){
	local fact=1
	while [ $n -gt 1 ]
	do
		let fact=($fact*$n)
		let n=($n-1)
	done
	final=$fact

}
factorial
echo $final



