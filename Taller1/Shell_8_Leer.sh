a=()
echo ${a[@]}
#a=(Arch "${a[@]}")
#echo ${a[@]}

while IFS= read -r line
do
  #echo "$line"
  a=("${a[@]}" $line)
done < archivo_rutas.dat
echo ${a[2]}
