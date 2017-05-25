# SpotyProject

Authors: Eduard Robinat && Gerard Mata


### Start the website
```
python manage.py runserver
```
### Data models:
```
Library: name, genere
Artist: nomArtista, tags, web, Library, user
Album: nomAlbum, releasedate, artist, Library, user
Track: nomTrack, duration, artist, album, Library, user
```
### Subpages:
```
Main page: http://127.0.0.1:8000/appmusic/librarys
Login screen: http://127.0.0.1:8000/accounts/login
Logout screen: http://127.0.0.1:8000/accounts/logout/
Admin panel: http://127.0.0.1:8000/admin/
API: http://127.0.0.1:8000/musicapp/api/[librarys-artists-albums-tracks]
```
### Default users:
```
Role - Username - Password

Admin: gmata 1234qwer
User: erobinat 1234qwer
```
