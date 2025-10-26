# 🚀 Guía de Deploy en Streamlit Cloud

## Pasos para Publicar tu Dashboard

### 1. Preparar el Repositorio Git

```bash
# Inicializar repositorio (si no existe)
git init

# Agregar todos los archivos
git add .

# Hacer commit
git commit -m "Dashboard Analytics Ecommerce Global v3.1 listo para deploy"

# Crear repositorio en GitHub y conectar
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git branch -M main
git push -u origin main
```

### 2. Deploy en Streamlit Cloud

1. **Ir a Streamlit Cloud**
   - Visita: https://share.streamlit.io
   - Inicia sesión con tu cuenta de GitHub

2. **Crear Nueva App**
   - Click en "New app"
   - Selecciona tu repositorio de GitHub
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: Elige un nombre único

3. **Configurar (Opcional)**
   - Python version: 3.11
   - No requiere secrets para la versión con Parquet

4. **Deploy**
   - Click en "Deploy"
   - Espera 2-5 minutos mientras se instalan dependencias
   - ¡Tu dashboard estará en línea!

### 3. URL Final

Tu dashboard estará disponible en:
```
https://TU_NOMBRE_APP.streamlit.app
```

---

## 📦 Archivos Necesarios (Ya Incluidos)

✅ `app.py` - Dashboard principal  
✅ `requirements.txt` - Dependencias  
✅ `.gitignore` - Archivos a ignorar  
✅ `data/*.parquet` - Datasets (17MB total)  
✅ `utils/` - Utilidades  
✅ `api/` - API (opcional)  
✅ `.streamlit/config.toml` - Configuración

---

## ⚙️ Configuración Avanzada (Opcional)

### Si usas PostgreSQL:

1. En Streamlit Cloud, ve a "Settings" → "Secrets"
2. Agrega:

```toml
[postgresql]
DATABASE_URL = "postgresql://usuario:password@host:5432/database"
```

3. Modifica `app.py` para usar `st.secrets` en producción

---

## 🔍 Troubleshooting

### Error: "Module not found"
- Verifica que todas las dependencias están en `requirements.txt`
- Revisa los logs en Streamlit Cloud

### Error: "Memory limit exceeded"
- Los archivos Parquet (17MB) están optimizados
- Streamlit Cloud tiene 1GB de RAM (suficiente)

### Error: "File not found"
- Verifica que `data/*.parquet` están en el repositorio
- No uses rutas absolutas, solo relativas

### Dashboard carga lento
- Normal en primera carga (instala dependencias)
- Cargas subsecuentes son rápidas (<3 segundos)

---

## 📊 Monitoreo

En Streamlit Cloud puedes:
- Ver logs en tiempo real
- Monitorear uso de recursos
- Ver analytics de visitantes
- Configurar dominios personalizados (plan paid)

---

## 🎯 Próximos Pasos

1. Comparte tu URL con clientes/stakeholders
2. Monitorea analytics y feedback
3. Actualiza con `git push` (auto-deploy)
4. Considera upgrade a plan paid para:
   - Más recursos
   - Dominio personalizado
   - Sin límite de visitantes

---

## ✨ Tu Dashboard Está Listo

**Características en Producción:**
- ✅ 472K transacciones analizadas
- ✅ 9 pestañas profesionales
- ✅ ML integrado (Prophet, K-Means)
- ✅ Visualizaciones optimizadas
- ✅ 100% en español
- ✅ Firma CMSR92
- ✅ Listo para cliente/directivos

**✨ Desarrollado por CMSR92 ✨**
