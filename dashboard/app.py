"""
Dashboard de Ventas - Superstore E-commerce
Autor: [Tu nombre]
Dataset: Sample Superstore (2014-2017)
Fuente: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =========================================================
# CONFIGURACIÓN DE LA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CARGA DE DATOS (cacheada)
# =========================================================
@st.cache_data
def cargar_datos():
    # Encontrar la raíz del proyecto (carpeta que contiene 'data')
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / 'data' / 'clean.csv'
    df = pd.read_csv(data_path, parse_dates=['Order Date', 'Ship Date'])
    return df

df = cargar_datos()

# =========================================================
# SIDEBAR — FILTROS
# =========================================================
st.sidebar.header("🔎 Filtros")

years = sorted(df['Year'].unique())
selected_years = st.sidebar.multiselect(
    "Año",
    options=years,
    default=years
)

regions = sorted(df['Region'].unique())
selected_regions = st.sidebar.multiselect(
    "Región",
    options=regions,
    default=regions
)

categories = sorted(df['Category'].unique())
selected_categories = st.sidebar.multiselect(
    "Categoría",
    options=categories,
    default=categories
)

segments = sorted(df['Segment'].unique())
selected_segments = st.sidebar.multiselect(
    "Segmento",
    options=segments,
    default=segments
)

# Aplicar filtros
filtrado = df[
    (df['Year'].isin(selected_years)) &
    (df['Region'].isin(selected_regions)) &
    (df['Category'].isin(selected_categories)) &
    (df['Segment'].isin(selected_segments))
]

# =========================================================
# ENCABEZADO
# =========================================================
st.title("📊 Superstore Sales Dashboard")
st.markdown(
    f"**Periodo:** {filtrado['Order Date'].min().date()} "
    f"→ {filtrado['Order Date'].max().date()} · "
    f"**Registros:** {len(filtrado):,}"
)

# =========================================================
# KPIs PRINCIPALES
# =========================================================
c1, c2, c3, c4 = st.columns(4)

total_sales     = filtrado['Sales'].sum()
total_profit    = filtrado['Profit'].sum()
total_orders    = filtrado['Order ID'].nunique()
total_customers = filtrado['Customer ID'].nunique()
margen = (total_profit / total_sales * 100) if total_sales > 0 else 0

c1.metric("💰 Ventas totales",  f"${total_sales:,.0f}")
c2.metric("📈 Profit total",     f"${total_profit:,.0f}", f"{margen:.1f}% margen")
c3.metric("🧾 Pedidos",          f"{total_orders:,}")
c4.metric("👥 Clientes únicos",  f"{total_customers:,}")

st.divider()

# =========================================================
# FILA 1: Evolución mensual + Ventas por categoría
# =========================================================
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📅 Evolución mensual de ventas")
    monthly = filtrado.groupby('YearMonth')['Sales'].sum().reset_index()
    fig = px.line(monthly, x='YearMonth', y='Sales', markers=True)
    fig.update_layout(
        xaxis_title="",
        yaxis_title="Ventas ($)",
        margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig, width='stretch')

with col2:
    st.subheader("🥧 Ventas por categoría")
    by_cat = filtrado.groupby('Category')['Sales'].sum().reset_index()
    fig = px.pie(by_cat, values='Sales', names='Category', hole=0.4)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig, width='stretch')

# =========================================================
# FILA 2: Top sub-categorías + Profit por región
# =========================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 Sub-categorías por ventas")
    top_sub = (filtrado.groupby('Sub-Category')['Sales']
               .sum().nlargest(10).reset_index()
               .sort_values('Sales'))
    fig = px.bar(top_sub, x='Sales', y='Sub-Category', orientation='h')
    fig.update_layout(
        xaxis_title="Ventas ($)",
        yaxis_title="",
        margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig, width='stretch')

with col2:
    st.subheader("🗺️ Ventas y Profit por región")
    by_region = filtrado.groupby('Region').agg(
        Sales=('Sales', 'sum'),
        Profit=('Profit', 'sum')
    ).reset_index()
    fig = px.bar(by_region, x='Region', y=['Sales', 'Profit'],
                 barmode='group')
    fig.update_layout(
        xaxis_title="",
        yaxis_title="$",
        legend_title="",
        margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig, width='stretch')

# =========================================================
# FILA 3: Profit vs Descuento
# =========================================================
st.subheader("🔍 Profit vs Descuento — la causa raíz de las pérdidas")
fig = px.scatter(
    filtrado, x='Discount', y='Profit',
    color='Category', opacity=0.4
)
fig.add_hline(y=0, line_dash="dash", line_color="red", opacity=0.6)
fig.update_layout(
    xaxis_title="Descuento",
    yaxis_title="Profit ($)",
    legend_title="Categoría",
    margin=dict(l=0, r=0, t=10, b=0)
)
st.plotly_chart(fig, width='stretch')

# =========================================================
# FILA 4: Tabla de sub-categorías con pérdidas
# =========================================================
st.subheader("🚨 Sub-categorías con pérdidas")
loss = (filtrado.groupby('Sub-Category')
        .agg(Sales=('Sales', 'sum'), Profit=('Profit', 'sum'))
        .reset_index())
loss = loss[loss['Profit'] < 0].sort_values('Profit')

if len(loss) > 0:
    st.dataframe(
        loss.style.format({'Sales': '${:,.0f}', 'Profit': '${:,.0f}'}),
        width='stretch'
    )
else:
    st.success("Ninguna sub-categoría tiene pérdidas con los filtros actuales.")

# =========================================================
# FOOTER
# =========================================================
st.divider()
st.caption(
    "Dashboard creado con Streamlit · "
    "Dataset: Sample Superstore (2014-2017) · "
    "Análisis de datos end-to-end"
)