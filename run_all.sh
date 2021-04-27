for file in *.jpg; do

	A="$(echo $file | cut -d'.' -f1)"
	B="_filt.jpg"
	out_file="$A$B"
 	python run.py $file
done

