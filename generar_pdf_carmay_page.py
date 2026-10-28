import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "/home/your-vps-user/proyectos/FACEBOOK/Reporte de Entidad Facebook - Your Brand.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# Estilos tipográficos
title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=colors.HexColor('#1E293B'),
    spaceAfter=12
)

h2_style = ParagraphStyle(
    'H2Style',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#0F172A'),
    spaceBefore=14,
    spaceAfter=8
)

body_style = ParagraphStyle(
    'BodyStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=14,
    textColor=colors.HexColor('#334155')
)

bold_label = ParagraphStyle(
    'BoldLabel',
    parent=body_style,
    fontName='Helvetica-Bold',
    textColor=colors.HexColor('#0F172A')
)

story = []

# Encabezado
story.append(Paragraph("Reporte de Entidad de Facebook", title_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#CBD5E1'), spaceAfter=15))

# 1. Identificación de la Entidad / Página Comercial
story.append(Paragraph("1. Identificación de la Entidad Comercial", h2_style))
entidad_data = [
    [Paragraph("Nombre de la Entidad:", bold_label), Paragraph("Your Brand", body_style)],
    [Paragraph("Tipo de Cuenta:", bold_label), Paragraph("Página Comercial / Perfil Profesional (Page Plus Delegate)", body_style)],
    [Paragraph("Identificador de Perfil (ID):", bold_label), Paragraph("61594230158782", body_style)],
    [Paragraph("ID Delegado de Página (Asset ID):", bold_label), Paragraph("1304361639431893", body_style)],
    [Paragraph("ID de Cuenta Comercial (Business ID):", bold_label), Paragraph("2687840971646678", body_style)],
    [Paragraph("Estado de Vinculación:", bold_label), Paragraph("Activo en Meta Business Suite y Switcher de Perfiles", body_style)],
    [Paragraph("Enlace Directo de Perfil:", bold_label), Paragraph("https://www.facebook.com/profile.php?id=61594230158782", body_style)]
]
t_entidad = Table(entidad_data, colWidths=[170, 360])
t_entidad.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
]))
story.append(t_entidad)
story.append(Spacer(1, 10))

# 2. Arquitectura de Propiedad y Administración en Meta
story.append(Paragraph("2. Propiedad y Administración en Meta Business Suite", h2_style))
admin_data = [
    [Paragraph("Propietario / Gestor Titular:", bold_label), Paragraph("Your Brand (Gestionado mediante Your Name)", body_style)],
    [Paragraph("ID del Administrador Gestor:", bold_label), Paragraph("YOUR_FB_C_USER (Usuario titular de la sesión activa)", body_style)],
    [Paragraph("Plataforma de Control:", bold_label), Paragraph("Meta Business Suite", body_style)],
    [Paragraph("Enlace de Administración Business:", bold_label), Paragraph("https://business.facebook.com/latest/home?business_id=2687840971646678&asset_id=1304361639431893", body_style)],
    [Paragraph("Ecosistema Asociado:", bold_label), Paragraph("Vinculado al Grupo Oficial de Ventas: YOUR_GROUP_NAME (ID: YOUR_FB_GROUP_ID)", body_style)]
]
t_admin = Table(admin_data, colWidths=[170, 360])
t_admin.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
]))
story.append(t_admin)
story.append(Spacer(1, 10))

# 3. Datos Comerciales del Negocio
story.append(Paragraph("3. Datos Comerciales y Operativos", h2_style))
com_data = [
    [Paragraph("Descripción Comercial:", bold_label), Paragraph("TIENDA MAYORISTA DE ROPA FASHION (SHEIN Y TEMU), PRECIOS MAYORISTAS.", body_style)],
    [Paragraph("Sede / Dirección Física:", bold_label), Paragraph("Avellaneda #260 e/ San Esteban y San Martin, Camagüey, Cuba", body_style)],
    [Paragraph("Línea Telefónica de Atención:", bold_label), Paragraph("+53 63791924", body_style)],
    [Paragraph("Horarios de Operación:", bold_label), Paragraph("Lunes a Viernes: 8:30 AM - 5:00 PM<br/>Sábados: 8:30 AM - 2:00 PM<br/>Domingos: Cerrado", body_style)]
]
t_com = Table(com_data, colWidths=[170, 360])
t_com.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
]))
story.append(t_com)

doc.build(story)
print(f"PDF generado: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
