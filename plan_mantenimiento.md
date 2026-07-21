# Plan de Mantenimiento Multilingüe (Español, Inglés, Francés, Alemán)

Este documento detalla la estrategia para colocar el sitio de **Spelling Bee** en modo mantenimiento premium mientras se realizan los ajustes requeridos.

## Objetivos
1. Reemplazar la página principal (`index.html`) por una pantalla de mantenimiento multilingüe de **calidad premium** con diseño Glassmorphism, animaciones estelares de fondo, contador/indicador de estado y selector de idioma dinámico (Español, Inglés, Francés, Alemán).
2. Asegurar que las rutas directas o subcarpetas de los proyectos (`/English/`, `/French/`, `/German/`) redirijan automáticamente a la página de mantenimiento en caso de que alguien intente ingresar directamente a los juegos/plataformas.
3. Guardar copia de seguridad de las versiones activas actuales (`index.html` -> `index_active_backup.html` y correspondientes en las subcarpetas) para habilitar el sitio de nuevo de forma instantánea al finalizar los ajustes.

---

## 1. Diseño de la Página de Mantenimiento (`index.html`)

La pantalla contará con:
- **Estética Ultra Premium Dark Glassmorphic**:
  - Degradado cósmico/estelar con luciérnagas y estrellas animadas en segundo plano.
  - Tarjeta central traslúcida con `backdrop-filter: blur(25px)`, bordes neón/dorados de alta elegancia.
  - Insignia/Icono animado de la abeja (Spelling Bee) pulsandome con destellos de luz.
- **Selector de Idiomas Trilingüe / Cuatrilingüe en tiempo real**:
  - Pestañas/botones interactivos con banderas (🇪🇸 Español, 🇬🇧 English, 🇫🇷 Français, 🇩🇪 Deutsch).
  - Cambio de textos y estados sin recargar la página.
- **Mensaje explicativo de alta calidad por idioma**:
  - **Español (Principal)**: *"Estamos realizando mejoras exclusivas. Regresaremos pronto con una experiencia renovada."*
  - **English**: *"We are currently performing scheduled maintenance to improve your experience. We will be back online shortly."*
  - **Français**: *"Nous effectuons actuellement une maintenance programmée. Notre plateforme sera de nouveau disponible très bientôt."*
  - **Deutsch**: *"Wir führen derzeit geplante Wartungsarbeiten durch, um Ihre Erfahrung zu verbessern. Wir sind in Kürze wieder für Sie da."*
- **Detalles Visuales Adicionales**:
  - Barra de progreso animada indicando *"Optimizando plataforma..."* / *"System Optimization in Progress"*.
  - Indicador de estado en tiempo real (Status: Maintenance Mode / Mantenimiento Activo).
  - Pie de página elegante con copyright y redes/contacto.

---

## 2. Bloqueo y Redirección en Subdirectorios (`English`, `French`, `German`)

Para garantizar que **el código no esté disponible/accesible** desde las rutas secundarias mientras se realizan los ajustes:
1. Renombrar temporalmente los `index.html` dentro de `English/`, `French/` y `German/` (ejemplo: `index.html` -> `index_active_backup.html`).
2. Crear un archivo `index.html` ligero de redirección en cada subdirectorio que redirija automáticamente a la raíz `/index.html` (Mantenimiento).

---

## 3. Plan de Despliegue (Git / Servidor / GitHub Pages)

Para bajar el sitio en producción:
1. Crear una rama de mantenimiento `feature/maintenance-mode` o trabajar sobre `main`.
2. Reemplazar `index.html` en la raíz con el nuevo diseño de mantenimiento premium.
3. Aplicar las redirecciones en las subcarpetas.
4. Hacer `git commit` y `git push` a los remotos (`origin`, `french`, `german`) para que GitHub Pages / Servidor se actualice automáticamente con la pantalla de mantenimiento.

---

## 4. Plan de Restauración (Volver a subir el proyecto)

Una vez terminados tus ajustes:
1. Restaurar `index.html` desde `index_active_backup.html`.
2. Restaurar los archivos `index.html` en `English/`, `French/` y `German/`.
3. Hacer `git push` a los remotos para volver a poner el proyecto arriba en línea.
