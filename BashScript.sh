# Sample code to make sure that code within the if .. fi is executed

if [ 1 -eq 1 ]; then
	echo "Start server"
	python3 ./querytest.py
fi;

userName=$(git config user.name)
echo $userName

modifiedExtensions=$(git status | grep modified| grep -Poi '\.(.*)$')
echo $modifiedExtensions

python3 ./LoopOver.py $modifiedExtensions