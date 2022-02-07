# Inserindo os textos
Header = '>>>Este curriculo foi gerado em Python. Para ver o código completo acesse o meu github<<<'
Name = 'TNORIO'
Title = 'Data Science & Analytics'
Contact = '(555)55555-5555\nABCsdfgshuokl@email.com\nlinkedin.com/in/qwerty\ngithub.com/tnorio'

txt1a = """  Sou um profissional versátil, adaptável e com motivação para
 novos aprendizados e desafios."""

SobreHeader = 'Sobre mim'
Sobre = txt1a

WorkHeader = 'Experiência'
WorkOneTitle,WorkOneTime = 'Coordenador Operacional', 'EMPRESA.SA entre 8/2015-2020'
WorkOneDesc = 'Descrição do trabalho'

WorkTwoTitle, WorkTwoTime = 'Trabalho 2','EMPRESA LTDA. entre 2020 - 2022'
WorkTwoDesc = 'Descrição do trabalho 2'

EduHeader = 'EDUCAÇÃO'
EduOneTitle, EduOneTime = 'Curso', '10/2021-06/2022'
EduOneDesc = 'Descrição do curso'
EduTwoTitle, EduTwoTime = 'Faculdade', '2015-2020'
EduTwoDesc = 'Descrição estudos / tcc faculdade'
EduThreeTitle, EduThreeTime = 'Curso 2', '2019'
EduThreeDesc = 'Descrição curso 2'

CertHeader = 'CERTIFICADOS'
Cert1Title, Cert1Time = 'Scientific Computing with Python - FreeCodeCamp.org', '10/2021-12/2021'
Cert2Title, Cert2Time = 'Data Analysis with Python - FreeCodeCamp.org', '12/2021-01/2022'
Cert3Title, Cert3Time = 'The Ultimate MySQL Bootcamp - Udemy', '01/2022-03/2022'


HSkillsHeader = 'Hard Skills'
HSkillsDesc = '- Python, SQL, R\n- Pandas, NumPy\n- Banco de Dados\n- Webscrapping\n- ETL\n- Análise e Visualização de Dados\n- Transformação de dados\n- Git e Controle de Versão\n- APIs\n- Machine Learning\n- Probabilidade e Estatística'
SSkillsHeader = 'Soft Skills'
SSkillsDesc = '- Trabalho em equipe\n- Comunicação\n- Capacidade de adaptação\n- Pensamento crítico\n- Ética de trabalho\n- Pensamento ágil e criativo'

# Gerando o PDF
import matplotlib.pyplot as plt
%matplotlib inline
# escolhendo a fonte
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))
# criando as linhas/ box de decoração
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#1d3d4e', alpha=0.5, linewidth=300) #right column
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
# cor de fundo
ax.set_facecolor('white')
# remover a grade do 'gráfico'
plt.axis('off')
# inserindo o texto
# o plt.annotate recebe os seguitnes argumentos: plt.annotate(texto,(tupla localização x,y), weight = se a fonte é normal/bold/italico..., fontsize=tamanho da fonte, alpha = trânsparecia)
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.75)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.905), weight='regular', fontsize=14)
plt.annotate(Contact, (.7,.91), weight='bold', fontsize=9.25, color='#ffffff')
plt.annotate(SobreHeader, (.02,.875), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(Sobre, (.02,.8), weight='regular', fontsize=9.5, ma=("left"))

plt.annotate(WorkHeader, (.02,.615), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02,.590), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.574), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04,.555), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.47), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.45), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.43), weight='regular', fontsize=9)

plt.annotate(EduHeader, (.02,.35), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02,.325), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02,.31), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduOneDesc, (.02,.28), weight='regular', fontsize=9)

plt.annotate(EduTwoTitle, (.02,.25), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.02,.235), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduTwoDesc, (.02,.22), weight='regular', fontsize=9)

plt.annotate(EduThreeTitle, (.02,.175), weight='bold', fontsize=10)
plt.annotate(EduThreeTime, (.02,.16), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduThreeDesc, (.02,.14), weight='regular', fontsize=9)

plt.annotate(CertHeader, (.02,.115), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(Cert1Title, (.02,.09), weight='bold', fontsize=10)
plt.annotate(Cert1Time, (.02,.075), weight='regular', fontsize=9, alpha=.6)

plt.annotate(Cert2Title, (.02,.055), weight='bold', fontsize=10)
plt.annotate(Cert2Time, (.02,.04), weight='regular', fontsize=9, alpha=.6)

plt.annotate(Cert3Title, (.02,.02), weight='bold', fontsize=10)
plt.annotate(Cert3Time, (.02,.005), weight='regular', fontsize=9, alpha=.6)


plt.annotate(HSkillsHeader, (.7,.825), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(HSkillsDesc, (.7,.6), weight='regular', fontsize=10, color='#ffffff')

plt.annotate(SSkillsHeader, (.7,.55), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SSkillsDesc, (.7,.42), weight='regular', fontsize=10, color='#ffffff')

plt.savefig('exemplo_curriculo.pdf', dpi=300, bbox_inches='tight')
