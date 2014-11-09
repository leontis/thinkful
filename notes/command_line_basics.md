cp -r #copy recursively the directory -- all contents of directory
rm -r hello_world # recursive delete
find . -name *.md # find all .md files

echo 'print "Hello World!"' > hello_world.py # copy text into a file

cat hello_world.py # print the file

less hello_world.py # print page by page with "q" to exit

curl website > file # download a file

grep is zen.txt
wc -l zen.txt 	# count lines in file; also: -w, -c
grep is zen.txt | wc -w # use of pipe 

Environment variables: Show and Set
printenv # show current variables
export BLOGFUL_SECRET_KEY="your_secret_key_here" # Create new environment variable

Paths: Set
PYTHONPATH=..
PYTHONPATH=.


#Use git GUI:
gitk
