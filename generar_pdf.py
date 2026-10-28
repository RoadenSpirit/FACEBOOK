import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "/home/your-vps-user/proyectos/FACEBOOK/Reporte de Grupo de Facebook.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# Estilos personalizados
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

# Título y separador
story.append(Paragraph("Reporte de Grupo de Facebook", title_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#CBD5E1'), spaceAfter=15))

# 1. Información General del Grupo
story.append(Paragraph("1. Información General del Grupo", h2_style))
gen_data = [
    [Paragraph("Nombre del Grupo:", bold_label), Paragraph("YOUR_GROUP_NAME", body_style)],
    [Paragraph("ID de Grupo:", bold_label), Paragraph("YOUR_FB_GROUP_ID", body_style)],
    [Paragraph("Fecha de Creación:", bold_label), Paragraph("26 de julio de 2024", body_style)],
    [Paragraph("Privacidad:", bold_label), Paragraph("Público (Visible para cualquier usuario)", body_style)],
    [Paragraph("Cantidad de Miembros:", bold_label), Paragraph("3,475 miembros registrados", body_style)],
    [Paragraph("Ubicación Registrada:", bold_label), Paragraph("Camagüey, Cuba", body_style)],
    [Paragraph("Enlace Oficial:", bold_label), Paragraph("https://www.facebook.com/groups/YOUR_FB_GROUP_ID/", body_style)]
]
t_gen = Table(gen_data, colWidths=[150, 380])
t_gen.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
]))
story.append(t_gen)
story.append(Spacer(1, 10))

# 2. Datos Comerciales y Contacto
story.append(Paragraph("2. Datos de Contacto y Ubicación Comercial", h2_style))
com_data = [
    [Paragraph("Descripción:", bold_label), Paragraph("TIENDA MAYORISTA DE ROPA FASHION (SHEIN Y TEMU), TENEMOS LOS MEJORES PRECIOS DE TODO EL MERCADO.", body_style)],
    [Paragraph("Dirección Física:", bold_label), Paragraph("Avellaneda #260 e/ San Esteban y San Martin, Camagüey, Cuba", body_style)],
    [Paragraph("Teléfono de Contacto:", bold_label), Paragraph("+53 63791924", body_style)],
    [Paragraph("Horarios de Atención:", bold_label), Paragraph("Lunes a Viernes: 8:30 AM - 5:00 PM<br/>Sábados: 8:30 AM - 2:00 PM<br/>Domingos: Cerrado", body_style)]
]
t_com = Table(com_data, colWidths=[150, 380])
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
story.append(Spacer(1, 10))

# 3. Administradores del Grupo
story.append(Paragraph("3. Administradores del Grupo", h2_style))
admin_headers = [Paragraph("Nombre", bold_label), Paragraph("Rol", bold_label), Paragraph("Perfil de Facebook", bold_label)]
admin_rows = [
    admin_headers,
    [
        Paragraph("Mayensy Rodríguez", body_style),
        Paragraph("Administrador", body_style),
        Paragraph("https://www.facebook.com/maye.alcala.90", body_style)
    ],
    [
        Paragraph("Danay Álvarez", body_style),
        Paragraph("Administrador", body_style),
        Paragraph("https://www.facebook.com/danay.alvarez.589", body_style)
    ],
    [
        Paragraph("Rioger De Jesús Vega Pérez", body_style),
        Paragraph("Administrador", body_style),
        Paragraph("https://www.facebook.com/rioger.de.jesus.vega.perez", body_style)
    ]
]
t_admin = Table(admin_rows, colWidths=[140, 130, 260])
t_admin.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
]))
story.append(t_admin)

doc.build(story)
print(f"PDF generado exitosamente en: {pdf_path}, tamaño: {os.path.getsize(pdf_path)} bytes")
