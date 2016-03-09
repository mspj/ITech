all: pull

pull:
	@echo "[*] Pulling new commits..."
	git pull
	@echo "[+] Pulling done"

clean:
	@echo "[*] Removing db.sqlite3..."
	-rm -f db.sqlite3
	@echo "[*] Installing new packages..."
	pip install -r requirements.txt
	@echo "[+] Installing new packages done"
	@echo "[*] Making migrations..."
	python manage.py makemigrations
	@echo "[+] Making migrations done"
	@echo "[*] Migrating new db file..."
	python manage.py migrate
	@echo "[+] Migrating done"
	@echo "[*] Populating data..."
	python populate_data.py
	@echo "[+] Populating data done"

deploy: pull clean
