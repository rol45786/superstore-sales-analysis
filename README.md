# 📊 Superstore Sales Analysis

Análisis completo de ventas del dataset **Sample Superstore** (2014–2017), desde la limpieza hasta un dashboard interactivo desplegado en Streamlit.

## 🎯 Objetivo

Identificar patrones de ventas, productos clave y segmentos de clientes para optimizar la estrategia comercial. El análisis responde a 5 preguntas de negocio:

1. ¿Cómo evolucionan las ventas en el tiempo?
2. ¿Qué categorías y productos generan más ingresos y profit?
3. ¿Quiénes son los clientes más valiosos?
4. ¿Los clientes vuelven a comprar?
5. ¿Cuál es el impacto real de los descuentos?

## 📁 Estructura del proyecto
ecommerce_sales/
├── dashboard/ # App interactiva en Streamlit
│ └── app.py
├── data/ # Datos crudos y limpios
│ ├── superstore.csv
│ └── clean.csv
├── notebooks/ # Análisis paso a paso
│ ├── 01_cleaning.ipynb
│ └── 02_eda.ipynb
├── sql/ # Consultas SQL (opcional)
├── requirements.txt
└── README.md


## 🧹 Limpieza de datos

- 9.994 filas originales → 9.994 tras limpieza (sin nulos ni duplicados)
- Fechas convertidas a `datetime`
- Columnas temporales creadas: `Year`, `Month`, `YearMonth`, `Quarter`, `DayOfWeek`
- Cálculo de `ShipDays` (tiempo de envío)

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

**Sub-categorías con pérdidas netas**:
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

**Insight**: el segmento "En riesgo de alto valor" (13.5% de clientes) genera el 23.1% de las ventas y el mayor profit histórico. Reactivar a esos 107 clientes es la acción con mayor ROI.

### 5. Retención — el cliente fiel existe
- Caída del **100% al 12.1%** entre el mes 0 y el mes 1
- Estabilización en el **15–20%** durante años
- Cohortes recientes (2016–2017) muestran mejor retención

## 🚀 Dashboard interactivo

[Ver dashboard en vivo →](https://superstore-sales-analysis.streamlit.app)

**Funcionalidades**:
- Filtros por año, región, categoría y segmento
- 4 KPIs dinámicos
- Evolución mensual, ventas por categoría, top productos
- Análisis de profit vs descuento
- Tabla de sub-categorías con pérdidas

## ⚙️ Cómo ejecutarlo localmente

```bash
git clone https://github.com/TU-USUARIO/superstore-sales-analysis.git
cd superstore-sales-analysis
pip install -r requirements.txt
streamlit run dashboard/app.py

---

## Resumen de cambios aplicados al `app.py`

| Antes | Ahora |
|---|---|
| `use_container_width=True` | `width='stretch'` |
| `use_container_width=False` | `width='content'` |
| Pie sin etiquetas | Pie con `percent+label` dentro |
| Legend fuera | Pie sin legend (más limpio) |
| Sin márgenes | `margin=dict(...)` para compactar |
| Sidebar colapsado | `initial_sidebar_state='expanded'` |
| Sin footer | Footer con créditos y contexto |

---

## Próximos pasos

1. **Copia el `app.py` nuevo** en `dashboard/app.py` (sobreescribe el actual).
2. **Guarda los otros archivos**: `requirements.txt`, `.gitignore`, `README.md`.
3. **Detén Streamlit** con Ctrl + C en la terminal donde corre.
4. **Vuelve a lanzarlo** para verificar que todo sigue funcionando:
   ```powershell
   streamlit run dashboard/app.py