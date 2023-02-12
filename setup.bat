gh repo create Advent-of-Code-2022-attempts --private
echo "# Advent-of-Code-2022-attempts" >> README.md 
git init
git add --all :/
git commit -m "first commit"
git branch -M main
git remote remove origin
git remote add origin https://github.com/ruodeee/Advent-of-Code-2022-attempts.git
git push -u origin main