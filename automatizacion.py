import streamlit as st
import graphviz as graphviz

# Título principal de la aplicación
st.title("🔧 Prototipo de Automatización de Procesos")
st.markdown("### Explora cómo automatizar flujos de trabajo con **Datosfera** y **n8n.io**")
st.write("""
Selecciona un área de tu empresa y un proceso que deseas automatizar para obtener un flujo de trabajo automatizado sugerido.
La automatización de procesos permite ahorrar tiempo, reducir errores humanos y mejorar la eficiencia operativa.
""")

# Diccionario con procesos automatizables por área
procesos_por_area = {
    'Ventas': ['Automatización de informes de ventas', 'Seguimiento de clientes potenciales', 'Notificaciones de pagos pendientes'],
    'Recursos Humanos': ['Onboarding automatizado de empleados', 'Generación de informes de nómina', 'Seguimiento de evaluaciones de desempeño'],
    'Marketing': ['Automatización de campañas de email', 'Segmentación de clientes basada en comportamiento', 'Generación de reportes de ROI'],
    'Finanzas': ['Automatización de conciliaciones bancarias', 'Notificaciones automáticas de facturas vencidas', 'Generación de informes financieros'],
    'Logística': ['Seguimiento automatizado de envíos', 'Alertas de inventario bajo', 'Automatización de órdenes de compra'],
    'Soporte Técnico': ['Creación automática de tickets de soporte', 'Asignación automática de tareas a técnicos', 'Seguimiento de SLA de tickets abiertos']
}

# Selección de área y proceso
area_seleccionada = st.selectbox("Selecciona un área", list(procesos_por_area.keys()))
proceso_seleccionado = st.selectbox("Selecciona un proceso a automatizar", procesos_por_area[area_seleccionada])

# Mostrar descripción del proceso seleccionado
st.markdown(f"### Has seleccionado automatizar el proceso de: **{proceso_seleccionado}** en el área de **{area_seleccionada}**.")

# Visualización del flujo de trabajo sugerido usando Graphviz
st.markdown("### Flujo de trabajo automatizado sugerido")
flow = graphviz.Digraph()

# Crear flujo de trabajo básico
if area_seleccionada == 'Ventas':
    flow.edge('Nuevo Pedido', 'Generación de Informe de Ventas')
    flow.edge('Generación de Informe de Ventas', 'Envío de Informe al Director de Ventas')
elif area_seleccionada == 'Recursos Humanos':
    flow.edge('Nuevo Empleado', 'Onboarding Automatizado')
    flow.edge('Onboarding Automatizado', 'Generación de Informe de Nómina')
elif area_seleccionada == 'Marketing':
    flow.edge('Inicio de Campaña', 'Segmentación de Clientes')
    flow.edge('Segmentación de Clientes', 'Automatización de Campaña de Email')
elif area_seleccionada == 'Finanzas':
    flow.edge('Factura Vencida', 'Generación de Informe Financiero')
    flow.edge('Generación de Informe Financiero', 'Notificación Automática de Factura')
elif area_seleccionada == 'Logística':
    flow.edge('Orden de Compra', 'Seguimiento de Envío')
    flow.edge('Seguimiento de Envío', 'Notificación de Inventario Bajo')
elif area_seleccionada == 'Soporte Técnico':
    flow.edge('Ticket Creado', 'Asignación Automática de Técnico')
    flow.edge('Asignación Automática de Técnico', 'Seguimiento de SLA')

# Mostrar el flujo visualizado
st.graphviz_chart(flow)

# Información adicional sobre la alianza con Datosfera y n8n.io
st.markdown("### Alianza con Datosfera y n8n.io")
st.write("""
En **Datosfera**, somos expertos en automatización de procesos empresariales utilizando **n8n.io**, una herramienta flexible 
y poderosa para crear flujos de trabajo automatizados en cualquier área de tu organización. 
Desde ventas hasta finanzas, podemos ayudarte a **reducir tiempos**, **eliminar errores humanos** y **optimizar operaciones**.
""")

# Botón de contacto (opcional)
if st.button('Solicitar más Información'):
    st.write("Gracias por tu interés. Un miembro de nuestro equipo se pondrá en contacto contigo para discutir cómo implementar la automatización en tu empresa.")

# Pie de página con la alianza
st.markdown("---")
st.markdown("**Este prototipo fue desarrollado por Datosfera en colaboración con Jorge Bustamante.**")
st.write("Transforma tus procesos empresariales con automatización eficiente.")

# Añadir un pie de página adicional
st.write("Desarrollado con ❤️ por Datosfera")
