# Sample code to make sure that code within the if .. fi is executed

echo -e "\t\t\tNo more fear of commitment...messages"
cat bunny.txt
echo -e "\n"

#if [ 1 -eq 1 ]; then
#	echo "Start server"
#	python3 ./querytest.py
#fi;

git add .

userName=$(git config user.name)
#echo $userName

modifiedExtensions=$(git status | grep 'modified\|new file\|deleted'| grep -Poi '\.(.*)$')
#echo $modifiedExtensions

mostCommonExtension=$(python3 ./LoopOver.py $modifiedExtensions)
#echo $mostCommonExtension

tweet=$(python3 ./markov_text.py $mostCommonExtension)
echo $tweet

git commit -m "$tweet"
git pull
git push

python3 ./twitterBot.py "$tweet"
