# 📊 Superstore Sales Analysis

Análisis completo de ventas del dataset **Sample Superstore** (2014–2017), desde la limpieza y el análisis exploratorio hasta un dashboard interactivo desplegado en Streamlit.

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 Objetivo

Identificar patrones de ventas, productos clave y segmentos de clientes para optimizar la estrategia comercial de un retailer estadounidense. El análisis responde a 5 preguntas de negocio:

1. ¿Cómo evolucionan las ventas en el tiempo?
2. ¿Qué categorías y productos generan más ingresos y profit?
3. ¿Quiénes son los clientes más valiosos?
4. ¿Los clientes vuelven a comprar?
5. ¿Cuál es el impacto real de los descuentos?

---

## 🚀 Dashboard interactivo

👉 **[Ver dashboard en vivo](https://superstore-sales-analysisi.streamlit.app)**

**Funcionalidades:**
- Filtros dinámicos por año, región, categoría y segmento
- 4 KPIs que se recalculan en tiempo real
- Evolución mensual de ventas
- Ventas por categoría (donut)
- Top 10 sub-categorías por ventas
- Profit y ventas por región
- Análisis Profit vs Descuento
- Tabla de sub-categorías con pérdidas

---

## 📁 Estructura del proyecto
ecommerce_sales/
├── dashboard/
│ └── app.py # Aplicación interactiva en Streamlit
├── data/
│ ├── superstore.csv # Dataset original
│ └── clean.csv # Dataset limpio y listo para análisis
├── notebooks/
│ ├── 01_cleaning.ipynb # Limpieza y transformación
│ └── 02_eda.ipynb # Análisis exploratorio
├── requirements.txt
└── README.md


---

## 🧹 Limpieza de datos

- **9.994 filas** originales, sin nulos ni duplicados tras la limpieza
- Fechas (`Order Date`, `Ship Date`) convertidas a `datetime`
- Columnas temporales creadas: `Year`, `Month`, `YearMonth`, `Quarter`, `DayOfWeek`
- Cálculo de `ShipDays` (días entre pedido y envío)

---

## 🔍 Principales hallazgos

### 1. Crecimiento sostenido
- **Ventas**: +52% entre 2014 ($484K) y 2017 ($733K)
- **Profit**: +90% entre 2014 ($49K) y 2017 ($93K)
- Pico máximo en **noviembre de 2017** ($118K)

### 2. Furniture: mucho volumen, poco margen
| Categoría | Ventas | Margen |
|---|---|---|
| Technology | $836K | **17.4%** |
| Office Supplies | $719K | **17.0%** |
| Furniture | $742K | **2.5%** 🚨 |

**Sub-categorías con pérdidas netas:**
- Tables: **−$17.725**
- Bookcases: **−$3.473**
- Supplies: **−$1.189**

### 3. Los descuentos destruyen valor
| Descuento | Margen |
|---|---|
| 0% | **+29.5%** ✅ |
| 1–20% | +11.9% ✅ |
| 21–30% | **−10.1%** 🚨 |
| 31–50% | **−24.8%** 🚨 |
| > 50% | **−119.2%** 🚨 |

**Conclusión**: el punto de inflexión está en descuentos > 20%.

### 4. RFM — la mina de oro escondida
| Segmento | Clientes | % Clientes | % Ventas | Profit |
|---|---|---|---|---|
| En riesgo (alto valor) | 107 | 13.5% | 23.1% | $82.6K |
| Leales | 180 | 22.7% | 23.7% | $54.5K |
| Champions | 58 | 7.3% | 15.6% | $49.0K |
| Perdidos (bajo valor) | 238 | 30.0% | 19.0% | $46.8K |

**Insight**: el segmento **"En riesgo de alto valor"** (13.5% de los clientes) genera el **23.1% de las ventas** y el mayor profit histórico. Reactivar a esos 107 clientes es la acción con mayor ROI del negocio.

### 5. Retención — el cliente fiel existe
- Caída del **100% al 12.1%** entre el mes 0 y el mes 1
- Estabilización en el **15–20%** durante años
- Las cohortes recientes (2016–2017) muestran mejor retención

---

## 🛠️ Tecnologías utilizadas

- **Python 3.11** — pandas, numpy
- **Visualización** — matplotlib, seaborn, plotly
- **Dashboard** — Streamlit
- **Notebooks** — Jupyter
- **Control de versiones** — Git + GitHub

---

## ⚙️ Cómo ejecutarlo localmente

```bash
# Clonar el repositorio
git clone https://github.com/rol45786/superstore-sales-analysis.git
cd superstore-sales-analysis

# Instalar dependencias
pip install -r requirements.txt

# Lanzar el dashboard
streamlit run dashboard/app.py

📚 Fuente de los datos
Sample Superstore — Kaggle

👤 Autor
Rolando Tellez

GitHub: @rol45786

LinkedIn: linkedin.com/in/rolando-tellez-luna-6a22541a7
