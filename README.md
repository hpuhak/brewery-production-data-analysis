# 🍺 Brewery Production Analysis

Projekti simuloi **pienpanimon tuotantodataa** ja näyttää, miten Pythonilla voidaan analysoida SQL-tietokannassa olevaa dataa.

## Projektin tavoitteet
- Yhdistää **PostgreSQL** ja **Python** (SQLAlchemy + Pandas)
- Tehdä **data-analyysi** tuotannosta, laatupoikkeamista ja seisokeista
- Visualisoida tulokset **Matplotlibilla**
- Projektissa on mukana myös **Streamlit-dashboard**, joka näyttää samat tiedot visuaalisessa muodossa selaimessa.

## Teknologiat
- Python 3
- Pandas
- Matplotlib
- SQLAlchemy
- PostgreSQL + psycopg2
- Streamlit
- Plotly

## Asennus ja käyttö
```bash
git clone https://github.com/hpuhak/brewery-production-data-analysis.git
cd brewery-production-data-analysis
pip install -r requirements.txt
```
1. Luo tietokanta `brewery_db` PostgreSQL:ään
2. Aja `create_tables.sql` ja `insert_data.sql`
3. Muokkaa `analysis.py` ja `dashboard.py` tietokantayhteyden tiedot oikein
4. Aja:
```bash
python analysis.py
streamlit run dashboard.py
```
