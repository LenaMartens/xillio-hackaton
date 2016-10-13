# Sample code to make sure that code within the if .. fi is executed

echo -e "\t\t\tNo more fear of commitment...messages"
cat bunny.txt
echo -e "\n"

# Git add has to be done first, in case of untracked files.
git add .


userName=$(git config user.name)
#echo $userName

# Three possible suffixes for changed files
modifiedExtensions=$(git status | grep 'modified\|new file\|deleted'| grep -Poi '\.(.*)$')
#echo $modifiedExtensions

mostCommonExtension=$(python ./LoopOver.py $modifiedExtensions)
#echo $mostCommonExtension

tweet=$(python ./markov_text.py $mostCommonExtension)
echo $tweet

git commit -m "$tweet"

echo -e "Your changes, have been committed, go ahead and push if you're ready"
python3 ./twitterBot.py "$tweet"
