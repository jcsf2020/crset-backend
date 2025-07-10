
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from models import ExportRequest, ExportType
import logging
import pandas as pd
import io
from datetime import datetime, timedelta
import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/generate")
async def generate_export(export_request: ExportRequest):
    """Gerar exportação de dados em PDF ou Excel"""
    try:
        if export_request.type == ExportType.PDF:
            return await generate_pdf_export(export_request)
        elif export_request.type == ExportType.EXCEL:
            return await generate_excel_export(export_request)
        else:
            raise HTTPException(status_code=400, detail="Tipo de exportação inválido")

    except Exception as e:
        logger.error(f"Error generating export: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao gerar exportação")

async def generate_pdf_export(export_request: ExportRequest):
    """Gerar relatório PDF"""
    try:
        # Criar buffer em memória
        buffer = io.BytesIO()
        
        # Configurar documento PDF
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        # Título
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#1F2937')
        )
        story.append(Paragraph("Finance Flow - Relatório Financeiro", title_style))
        story.append(Paragraph(f"João Fonseca | {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
        story.append(Spacer(1, 20))

        # Resumo Executivo
        story.append(Paragraph("Resumo Executivo", styles['Heading2']))
        summary_data = [
            ["Saldo Total", "€15.750"],
            ["Receita Semanal", "€38.500"],
            ["Oportunidades Abertas", "8"],
            ["Crescimento Mensal", "+5.2%"]
        ]
        
        summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F3F4F6')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1F2937')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E5E7EB'))
        ]))
        story.append(summary_table)
        story.append(Spacer(1, 20))

        # Ativos
        if export_request.includeAssets:
            story.append(Paragraph("Portfólio de Ativos", styles['Heading2']))
            assets_data = [
                ["Ativo", "Tipo", "Valor", "Moeda"],
                ["Bitcoin Holdings", "Crypto", "€8.500", "EUR"],
                ["Ethereum Holdings", "Crypto", "€3.200", "EUR"],
                ["Conta Poupança BCP", "Cash", "€2.500", "EUR"],
                ["CRSET Solutions", "Business", "€1.550", "EUR"]
            ]
            
            assets_table = Table(assets_data, colWidths=[2.5*inch, 1.5*inch, 1*inch, 1*inch])
            assets_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3B82F6')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E5E7EB'))
            ]))
            story.append(assets_table)
            story.append(Spacer(1, 20))

        # Oportunidades
        if export_request.includeOpportunities:
            story.append(Paragraph("Oportunidades de Investimento", styles['Heading2']))
            opps_data = [
                ["Oportunidade", "Tipo", "Status", "Valor"],
                ["Apartamento T2 Porto", "Imobiliário", "Aberta", "€120.000"],
                ["Startup FinTech", "Investment", "Em Progresso", "€25.000"],
                ["Consultoria BCP", "Projeto", "Fechada", "€18.000"],
                ["Workshop Tech", "Projeto", "Fechada", "€8.500"]
            ]
            
            opps_table = Table(opps_data, colWidths=[2.5*inch, 1.5*inch, 1.2*inch, 1.3*inch])
            opps_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#10B981')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E5E7EB'))
            ]))
            story.append(opps_table)
            story.append(Spacer(1, 20))

        # Transações
        if export_request.includeTransactions:
            story.append(Paragraph("Transações Recentes", styles['Heading2']))
            trans_data = [
                ["Data", "Descrição", "Tipo", "Valor"],
                ["07/07/2025", "Consultoria BCP", "Receita", "€18.000"],
                ["06/07/2025", "Cliente VIP", "Receita", "€12.000"],
                ["05/07/2025", "Workshop Tech", "Receita", "€8.500"],
                ["01/07/2025", "Compra BTC", "Investimento", "-€2.000"]
            ]
            
            trans_table = Table(trans_data, colWidths=[1.2*inch, 2.8*inch, 1.5*inch, 1*inch])
            trans_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EF4444')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E5E7EB'))
            ]))
            story.append(trans_table)

        # Rodapé
        story.append(Spacer(1, 40))
        story.append(Paragraph("Relatório gerado automaticamente pelo Finance Flow Personal", styles['Normal']))
        story.append(Paragraph(f"CRSET Solutions | {datetime.now().isoformat()}", styles['Normal']))

        # Construir PDF
        doc.build(story)
        buffer.seek(0)

        # Retornar como response
        return StreamingResponse(
            io.BytesIO(buffer.read()),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=finance_flow_report_{datetime.now().strftime('%Y%m%d')}.pdf"}
        )

    except Exception as e:
        logger.error(f"Error generating PDF: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao gerar PDF")

async def generate_excel_export(export_request: ExportRequest):
    """Gerar exportação Excel"""
    try:
        # Criar buffer em memória
        buffer = io.BytesIO()
        
        # Criar workbook Excel
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            
            # Aba de Resumo
            summary_df = pd.DataFrame({
                'Métrica': ['Saldo Total', 'Receita Semanal', 'Oportunidades Abertas', 'Crescimento Mensal'],
                'Valor': ['€15.750', '€38.500', '8', '+5.2%']
            })
            summary_df.to_excel(writer, sheet_name='Resumo', index=False)
            
            # Aba de Ativos
            if export_request.includeAssets:
                assets_df = pd.DataFrame({
                    'Nome': ['Bitcoin Holdings', 'Ethereum Holdings', 'Conta Poupança BCP', 'CRSET Solutions'],
                    'Tipo': ['Crypto', 'Crypto', 'Cash', 'Business'],
                    'Valor': [8500.0, 3200.0, 2500.0, 1550.0],
                    'Moeda': ['EUR', 'EUR', 'EUR', 'EUR'],
                    'Data Compra': ['2024-01-15', '2024-02-10', '', '2023-06-01']
                })
                assets_df.to_excel(writer, sheet_name='Ativos', index=False)
            
            # Aba de Oportunidades
            if export_request.includeOpportunities:
                opportunities_df = pd.DataFrame({
                    'Título': ['Apartamento T2 Porto', 'Startup FinTech', 'Consultoria BCP', 'Workshop Tech'],
                    'Tipo': ['Imobiliário', 'Investment', 'Projeto', 'Projeto'],
                    'Status': ['Aberta', 'Em Progresso', 'Fechada Won', 'Fechada Won'],
                    'Valor': [120000.0, 25000.0, 18000.0, 8500.0],
                    'Prioridade': ['Alta', 'Média', 'Alta', 'Média'],
                    'Contacto': ['Maria Silva - Remax', 'Pedro Santos - CEO', 'Millennium BCP', 'Tech Hub Lisboa']
                })
                opportunities_df.to_excel(writer, sheet_name='Oportunidades', index=False)
            
            # Aba de Transações
            if export_request.includeTransactions:
                transactions_df = pd.DataFrame({
                    'Data': ['2025-07-07', '2025-07-06', '2025-07-05', '2025-07-01'],
                    'Descrição': ['Consultoria Bancária Digital - Millennium BCP', 'Assessoria Investimento Particular - Cliente VIP', 'Workshop Empresas Tech - Tech Hub Lisboa', 'Compra adicional BTC - DCA strategy'],
                    'Tipo': ['Receita', 'Receita', 'Receita', 'Investimento'],
                    'Valor': [18000.0, 12000.0, 8500.0, -2000.0],
                    'Categoria': ['Consultoria', 'Assessoria', 'Formação', 'Crypto']
                })
                transactions_df.to_excel(writer, sheet_name='Transações', index=False)

        buffer.seek(0)

        # Retornar como response
        return StreamingResponse(
            io.BytesIO(buffer.read()),
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename=finance_flow_data_{datetime.now().strftime('%Y%m%d')}.xlsx"}
        )

    except Exception as e:
        logger.error(f"Error generating Excel: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao gerar Excel")

@router.get("/templates")
async def get_export_templates():
    """Obter templates de exportação disponíveis"""
    return {
        "pdf": {
            "name": "Relatório PDF",
            "description": "Relatório completo em formato PDF profissional",
            "features": ["Resumo executivo", "Gráficos", "Tabelas formatadas", "Cabeçalho/rodapé"]
        },
        "excel": {
            "name": "Dados Excel",
            "description": "Dados estruturados em múltiplas abas para análise",
            "features": ["Múltiplas abas", "Dados estruturados", "Fórmulas", "Gráficos"]
        }
    }

@router.get("/schedule")
async def get_export_schedule():
    """Obter agenda de exportações automáticas"""
    return {
        "weekly": {
            "enabled": True,
            "day": "sunday",
            "time": "09:00",
            "format": "pdf",
            "email": "joao.fonseca@crset.com"
        },
        "monthly": {
            "enabled": True,
            "day": "last",
            "time": "18:00",
            "format": "excel",
            "email": "joao.fonseca@crset.com"
        },
        "quarterly": {
            "enabled": False,
            "format": "pdf"
        }
    }
