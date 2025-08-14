import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
import plotly.express as px

# Yhteys PostgreSQL:ään SQLAlchemyllä
# Format: "postgresql+psycopg2://KÄYTTÄJÄ:SALASANA@PALVELIN:PORTTI/TIETOKANTA"
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/brewery_db")

# Haetaan data
df_production = pd.read_sql("SELECT * FROM production", engine)
df_quality = pd.read_sql("SELECT * FROM quality_checks", engine)
df_downtime = pd.read_sql("SELECT * FROM downtime", engine)

# Streamlit-käyttöliittymä
st.set_page_config(page_title="Pienpanimon tuotanto-dashboard", layout="wide")

st.title("🍺 Pienpanimon tuotanto-dashboard")
st.markdown("Tämä dashboard näyttää tuotannon, laatupoikkeamat ja seisokit kuukauden ajalta.")

# Tuotanto kuvaajana
prod_summary = df_production.groupby("product_name")["units_produced"].sum().reset_index()
fig_prod = px.bar(prod_summary, x="product_name", y="units_produced",
                  title="Tuotanto tuotteittain", color="product_name")
st.plotly_chart(fig_prod, use_container_width=True)

# Laatupoikkeamat kuvaajana
quality_summary = df_quality.groupby("defect_type")["defect_count"].sum().reset_index()
fig_quality = px.bar(quality_summary, x="defect_type", y="defect_count",
                     title="Laatupoikkeamien jakauma", color="defect_type")
st.plotly_chart(fig_quality, use_container_width=True)

# Seisokit kuvaajana
downtime_summary = df_downtime.groupby("reason")["minutes_lost"].sum().reset_index()
fig_downtime = px.bar(downtime_summary, x="reason", y="minutes_lost",
                      title="Seisokkien syyt", color="reason")
st.plotly_chart(fig_downtime, use_container_width=True)

# Yhteenveto
total_units = df_production["units_produced"].sum()
top_product = prod_summary.sort_values("units_produced", ascending=False).iloc[0]
most_common_defect = quality_summary.sort_values("defect_count", ascending=False).iloc[0]
main_downtime_reason = downtime_summary.sort_values("minutes_lost", ascending=False).iloc[0]

st.markdown(f"""
**Kokonaisvalmistusmäärä:** {total_units} yksikköä  
**Eniten valmistettu tuote:** {top_product['product_name']} ({top_product['units_produced']} yksikköä)  
**Yleisin laatupoikkeama:** {most_common_defect['defect_type']} ({most_common_defect['defect_count']} kpl)  
**Suurin seisokkien syy:** {main_downtime_reason['reason']} ({main_downtime_reason['minutes_lost']} minuuttia)  
""")
