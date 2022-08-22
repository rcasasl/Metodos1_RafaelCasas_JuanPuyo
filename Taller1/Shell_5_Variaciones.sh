n=20
r=3
f=20
let d=$(($f-$r))



function factorial(){
	local fact1=1
	local fact2=1
	while [ $n -gt 1  ] 
	do
		let fact1=($fact1*$n)
     		let n=($n-1)
		while [ $d -gt 1 ]
		do
			let fact2=($fact2*$d)
			let d=($d-1)
		done
	done
	nfact=$fact1
	rfact=$fact2



	variacion=$(($nfact/$rfact))



}
factorial
echo $variacion

