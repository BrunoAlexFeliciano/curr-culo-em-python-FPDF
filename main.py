from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_margins(left=12, top=12, right=12)

def adicionar_titulo(titulo):
    pdf.set_font("Arial", size=13)
    pdf.cell(0, 10, text=titulo, new_x='LMARGIN', new_y='NEXT', markdown=True)
    pdf.ln(1)

def adicionar_info(info):
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, text=info, new_x='LMARGIN', new_y='NEXT', markdown=True)

def adicionar_texto(texto):
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text=texto, new_x='LMARGIN', new_y='NEXT', markdown=True)
    pdf.ln(5)

adicionar_titulo("**BRUNO ALEX FELICIANO**")
adicionar_info("CIDADE/ESTADO Brasil | XX anos")
adicionar_info("Linkedin: XXXXXXXXXXXXXX")
adicionar_info("GitHub: XXXXXXXXXXXXXX")
adicionar_info("E-mail: exemplo@email.com.br")
adicionar_info("Telefone: Telefone: +55 (XX) XXXXX-XXXX")
pdf.ln(5)

adicionar_titulo("**FORMAÇÃO ACADÊMICA**")
adicionar_texto("Graduação em Ciências da Computação Universidade Exemplo - XXXX")

adicionar_titulo("**CURSOS COMPLEMENTARES**")
adicionar_texto("Curso de Arduino - SENAI - Curso de Hardware e Manutenção de PCs - Microcamp - Do zero a automação em python - Udemy")

adicionar_titulo("**EXPERIÊNCIA PROFISSIONAL**")
adicionar_texto("Técnico de Informática / Assistência Técnica - Diagnóstico e conserto de desktops e notebooks - Formatação, instalação de sistemas - Manutenção preventiva e corretiva de hardware")

adicionar_titulo("**HABILIDADES**")
adicionar_texto("Manutenção e montagem de computadores - Diagnostico de problemas de hardware e software - Conhecimentos em Linux - Noções de redes")

adicionar_titulo("**PYTHON**")
adicionar_texto("Nível: Júnior Automação com Python:Escrita e extração de dados de arquivos PDF, automação e análise de planilhas Excel, gerenciamento de caminhos e diretórios, leitura, escrita e organização de arquivos, manipulação de documentos DOCX. Conhecimentos em automação de envio de e-mails, gerenciamento de tarefas no Windows, consumo de APIs, básico de SQL, bancos de dados e interfaces.")

pdf.output("currículo.pdf")