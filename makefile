hello:
	echo "Hello, World"

save-conda-env:
	conda list -e | cut -d '=' -f 1,2 > requirements.txt
	conda env export > environment.yaml