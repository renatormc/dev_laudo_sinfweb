# Deploy 

```poweshell
python manage.py prepare up
python main.py change-version
poetry export --without-hashes -f requirements.txt -o requirements.txt
python .\fastdoc\updater\pack_dist.py D:\src\fastdoc\dist
```