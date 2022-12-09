# Animebot

## Using

1. Install dependecies:

```bash
conda create -f environment 
conda activate animebot
pip install -r requirements.txt
pip install -e . # installs inner code as python package in developing mode
```
2. Create an `.env` file from template `.env-example`:
```bash
touch .env
```
3. Initialize database:
```bash
python src/scraper/init_db.py # 
```
4. Run sraper:
```bash
python src/scraper/scraper.py # 
```