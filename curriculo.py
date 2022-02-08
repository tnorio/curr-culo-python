# Inserindo os textos
Header ='>>>Este curriculo foi gerado em Python. Para ver o código completo acesse o meu github<<<'
nome = 'TNORIO'
titulo = 'Data Science & Analytics'
contato = '(555)55555-5555\nABCsdfgshuokl@email.com\nlinkedin.com/in/qwerty\ngithub.com/tnorio'

txt1a = '''  Sou um profissional versátil, adaptável e com motivação para
 novos aprendizados e desafios.'''

SobreHeader = 'Sobre mim'
Sobre = txt1a

trabalhoheader = 'Experiência'
trabalho1titulo, trabalho1duracao = 'Coordenador Operacional', 'EMPRESA.SA entre 8/2015-2020'
trabralho1descricao = 'Descrição do trabalho'

trabalho2titulo, trabalho2duracao = 'Trabalho 2','EMPRESA LTDA. entre 2020 - 2022'
trabalho2descricao = 'Descrição do trabalho 2'

EduHeader = 'EDUCAÇÃO'
edu1titulo,edu1duracao = 'Curso', '10/2021-06/2022'
edu1descricao = 'Descrição do curso'
edu2titulo,edu2duracao = 'Faculdade', '2015-2020'
edu2descricao = 'Descrição estudos / tcc faculdade'
edu3titulo, edu3duracao = 'Curso 2', '2019'
edu3descricao = 'Descrição curso 2'

CertHeader = 'CERTIFICADOS'
cert1titulo,cert1duracao = 'Scientific Computing with Python - FreeCodeCamp.org', '10/2021-12/2021'
cert2titulo,cert2duracao = 'Data Analysis with Python - FreeCodeCamp.org', '12/2021-01/2022'
cert3titulo,cert3duracao = 'The Ultimate MySQL Bootcamp - Udemy', '01/2022-03/2022'

hskillsHeader = 'Hard Skills'
hskillsdescricao = '- Python, SQL, R\n- Pandas, NumPy\n- Banco de Dados\n- Webscrapping\n- ETL\n- Análise e Visualização de Dados\n- Transformação de dados\n- Git e Controle de Versão\n- APIs\n- Machine Learning\n- Probabilidade e Estatística'
sskillsHeader = 'Soft Skills'
sskillsdescricao = '- Trabalho em equipe\n- Comunicação\n- Capacidade de adaptação\n- Pensamento crítico\n- Ética de trabalho\n- Pensamento ágil e criativo'

idioma = "-Portugês(nativo)\n- Inglês(intermediário)"

# Gerando o PDF
import matplotlib.pyplot as plt
%matplotlib inline
# escolhendo a fonte
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))
# criando as linhas/ box de decoração
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#1d3d4e',alpha=0.5,linewidth=300) #coluna da direita
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
# cor de fundo
ax.set_facecolor('white')
# remover a grade do 'gráfico'
plt.axis('off')
# inserindo o texto
# o plt.annotate recebe os seguitnes argumentos: plt.annotate(texto,(tupla localização x,y), weight = se a fonte é normal/bold/italico..., fontsize=tamanho da fonte, alpha = trânsparecia)
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.75)
plt.annotate(nome, (.02,.94), weight='bold', fontsize=20)
plt.annotate(titulo,(.02,.905), weight='regular', fontsize=14)
plt.annotate(contato, (.7,.91), weight='bold', fontsize=9.25, color='#ffffff')
plt.annotate(SobreHeader, (.02,.875), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(Sobre, (.02,.8), weight='regular', fontsize=9.5, ma=("left"))

plt.annotate(trabalhoheader, (.02,.615), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(trabalho1titulo, (.02,.590), weight='bold', fontsize=10)
plt.annotate(trabalho1duracao, (.02,.574), weight='regular', fontsize=9, alpha=.6)
plt.annotate(trabralho1descricao, (.04,.555), weight='regular', fontsize=9)
plt.annotate(trabalho2titulo, (.02,.47), weight='bold', fontsize=10)
plt.annotate(trabalho2duracao, (.02,.45), weight='regular', fontsize=9, alpha=.6)
plt.annotate(trabalho2descricao, (.04,.43), weight='regular', fontsize=9)

plt.annotate(EduHeader, (.02,.35), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(edu1titulo, (.02,.325), weight='bold', fontsize=10)
plt.annotate(edu1duracao, (.02,.31), weight='regular', fontsize=9, alpha=.6)
plt.annotate(edu1descricao, (.02,.28), weight='regular', fontsize=9)

plt.annotate(edu2titulo, (.02,.25), weight='bold', fontsize=10)
plt.annotate(edu2duracao, (.02,.235), weight='regular', fontsize=9, alpha=.6)
plt.annotate(edu2descricao, (.02,.22), weight='regular', fontsize=9)

plt.annotate(edu3titulo, (.02,.175), weight='bold', fontsize=10)
plt.annotate(edu3duracao, (.02,.16), weight='regular', fontsize=9, alpha=.6)
plt.annotate(edu3descricao, (.02,.14), weight='regular', fontsize=9)

plt.annotate(CertHeader,(.02,.115), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(cert1titulo, (.02,.09), weight='bold', fontsize=10)
plt.annotate(cert1duracao, (.02,.075), weight='regular', fontsize=9, alpha=.6)

plt.annotate(cert2titulo, (.02,.055), weight='bold', fontsize=10)
plt.annotate(cert2duracao, (.02,.04), weight='regular', fontsize=9, alpha=.6)

plt.annotate(cert3titulo, (.02,.02), weight='bold', fontsize=10)
plt.annotate(cert3duracao, (.02,.005),weight='regular', fontsize=9, alpha=.6)

plt.annotate(hskillsHeader, (.7,.825), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(hskillsdescricao, (.7,.6), weight='regular', fontsize=10, color='#ffffff')

plt.annotate(sskillsHeader, (.7,.55), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(sskillsdescricao, (.7,.42), weight='regular', fontsize=10, color='#ffffff')
plt.annotate("Idomas", (.7,.37), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(idioma, (.7,.32), weight = 'regular', fontsize=10, color='#ffffff')

plt.savefig('exemplo_curriculo.pdf', dpi=300, bbox_inches='tight')
