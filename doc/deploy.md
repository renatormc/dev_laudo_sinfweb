# Deploy 

```powershell
python manage.py prepare up
python main.py change-version
poetry export --without-hashes -f requirements.txt -o requirements.txt
git add . 
git commit -m "New release"
git push origin master
python .\fastdoc\updater\pack_dist.py D:\src\fastdoc\dist
```