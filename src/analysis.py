import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Yhteys PostgreSQL:ään
# Luodaan yhteys tietokantaan käyttämällä SQLAlchemyä ja psycopg2-ajuria
# Format: "postgresql+psycopg2://KÄYTTÄJÄ:SALASANA@PALVELIN:PORTTI/TIETOKANTA"
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/brewery_db")

# Haetaan kaikki kolme taulua Pandasiin
df_production = pd.read_sql("SELECT * FROM production", engine)
df_quality = pd.read_sql("SELECT * FROM quality_checks", engine)
df_downtime = pd.read_sql("SELECT * FROM downtime", engine)

# Tuotantoanalyysi
# Lasketaan kokonais- ja tuotekohtainen tuotanto
prod_summary = df_production.groupby("product_name")["units_produced"].sum().reset_index()

# Pylväsdiagrammi tuotekohtaisesta tuotannosta
plt.figure(figsize=(6, 4))
plt.bar(prod_summary["product_name"], prod_summary["units_produced"], color=["gold", "orange", "brown"])
plt.title("Viikon tuotanto tuotteittain")
plt.xlabel("Tuote")
plt.ylabel("Valmistetut yksiköt")
plt.tight_layout()
plt.savefig("production_summary.png")
plt.close()

# Laatupoikkeama-analyysi
# Lasketaan poikkeamien määrä tyypeittäin
quality_summary = df_quality.groupby("defect_type")["defect_count"].sum().reset_index()

plt.figure(figsize=(6, 4))
plt.barh(quality_summary["defect_type"], quality_summary["defect_count"], color="red")
plt.title("Laatupoikkeamat viikon aikana")
plt.xlabel("Poikkeamien määrä")
plt.ylabel("Poikkeamatyyppi")
plt.tight_layout()
plt.savefig("quality_summary.png")
plt.close()

# Seisokkianalyysi
# Lasketaan seisokit syyn mukaan
downtime_summary = df_downtime.groupby("reason")["minutes_lost"].sum().reset_index()

plt.figure(figsize=(6, 4))
plt.barh(downtime_summary["reason"], downtime_summary["minutes_lost"], color="gray")
plt.title("Seisokit viikon aikana")
plt.xlabel("Menetetyt minuutit")
plt.ylabel("Syyt")
plt.tight_layout()
plt.savefig("downtime_summary.png")
plt.close()

# Yhteenvetoraportti
# Lasketaan kokonaisluvut
total_units = df_production["units_produced"].sum()
top_product = prod_summary.sort_values("units_produced", ascending=False).iloc[0]
most_common_defect = quality_summary.sort_values("defect_count", ascending=False).iloc[0]
main_downtime_reason = downtime_summary.sort_values("minutes_lost", ascending=False).iloc[0]

summary_text = f"""
📊 Pienpanimon viikkoraportti

Tuotanto yhteensä: {total_units} yksikköä
Eniten valmistettu tuote: {top_product['product_name']} ({top_product['units_produced']} yksikköä)

Yleisin laatupoikkeama: {most_common_defect['defect_type']} ({most_common_defect['defect_count']} kpl)
Suurin seisokkien syy: {main_downtime_reason['reason']} ({main_downtime_reason['minutes_lost']} minuuttia)

Kuvaajat:
- production_summary.png → tuotantomäärät tuotteittain
- quality_summary.png → laatupoikkeamien jakauma
- downtime_summary.png → seisokkien syyt
"""

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print(summary_text)

