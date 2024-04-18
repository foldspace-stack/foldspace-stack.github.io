npm run build
ret=$?
if [ $ret -eq 0 ]
then
   echo "In If"
   git add docs
   git add .obsidian
   git commit -a -m "自动提交 $(date)"
   git push origin 
else
   exit
fi
