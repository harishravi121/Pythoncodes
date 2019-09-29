import os
import sys
Folderandtime=str(sys.argv[1])
csvfile='Results_'+Folderandtime+'.csv'
Worstfig='Worst_'+Folderandtime+'.pdf'
Bestfig='Best_'+Folderandtime+'.pdf'
tfile='Report_'+Folderandtime+'.tex'
#importing data#
f1=open(csvfile,'r')

ar=f1.read()
data=['']*7*4
word=''
j=0
for f in ar:
    if f!=',' and f!='\n':
        word=word+f
    
    else:
        data[j]=data[j]+word
        j=j+1
        word=''
        
f1.close()
#end of import


f=open(tfile,'w')


f.write('\\documentclass[a4paper]{article}\n')
f.write('\\usepackage{a4wide}\n')
f.write('\\usepackage{amsmath}\n')
f.write('\\usepackage{dcolumn}% Align table columns on decimal point\n')
f.write('\\usepackage{bm}% bold math\n')
f.write('\\usepackage{textcomp}\n')
f.write('\\usepackage{graphicx}\n')
f.write('\\usepackage{caption}\n')
f.write('\\usepackage{subcaption}\n')


f.write('\\title{\\vspace{-1.5in} EDM Measurement }\n')

f.write('\\date{\\vspace{-0.4in} \\today}\n')

f.write('\\begin{document}\n')
f.write('\\maketitle\n')

f.write('\\section{Description}\n')
f.write('\\begin{itemize}\n')
f.write('\\item Electric field is  5.7 KV/cm\n')
f.write('\\item ' +data[2]+' points with High voltage and '+data[0]+' points with Low voltage\n') #data[0],[1] low, data[2],[3] high
f.write('\\item Is the High voltage application Randomized? - Yes\n')
f.write('\\end{itemize}\n')

f.write('\\section{Table of results}\n')
f.write('\\begin{table}[h]\n')
f.write('\\centering\n')
f.write('{\n')
f.write('\\begin{tabular}{ l r c r c }\n')
f.write('& \\multicolumn{2}{c}{No E field} &  \\multicolumn{2}{c}{With E field} \\\ \n')
f.write('& \\multicolumn{1}{c}{Average} & Std dev & \\multicolumn{1}{c}{Average} & Std dev \\\ \n')
f.write('& \\multicolumn{1}{c}{(mG)} & (\\textmu G) & \\multicolumn{1}{c}{(mG)} & (\\textmu G) \\\ \n')
f.write('\\hline \n')



f.write('Right &'+ str(round(float(data[4]),4)) +'&' +str(round(float(data[5])*1000,1)) +'&'+ str(round(float(data[6]),4))+ '&' +str(round(float(data[7])*1000,1))+ '\\\ \n')
f.write('Left &'+ str(round(float(data[8]),4)) +'&' +str(round(float(data[9])*1000,1))+'&'+ str(round(float(data[10]),4))+ '&' +str(round(float(data[11])*1000,1))+ '\\\ \n')
f.write('Centre &'+ str(round(float(data[12]),4)) +'&' +str(round(float(data[13])*1000,1)) +'&'+str(round(float(data[14]),4))+ '&' +str(round(float(data[15])*1000,1))+ '\\\ \n')
f.write('Separation &'+ str(round(float(data[16]),4)) +'&' +str(round(float(data[17])*1000,1))+'&'+ str(round(float(data[18]),4))+ '&' +str(round(float(data[19])*1000,1))+ '\\\ \n')
f.write('Linewidth  &'+ str(round(float(data[20]),4)) +'&' +str(round(float(data[21])*1000,1))+'&'+ str(round(float(data[22]),4))+ '&' +str(round(float(data[23])*1000,1))+ '\\\ \n')

f.write('\\end{tabular}\n')

f.write('\\label{tab:Data2}\n')


f.write('}\n')
f.write('\\end{table}\n')
f.write('\\begin{itemize}\n')
f.write('\\item \\textbf{$d_{\\text{A meas}}$} = '+data[24]+' e-cm,  \\textbf{$d_{\\text{E meas}}$}= '+data[25]+' e-cm , \\textbf{$d_{\\text{E lim}}$}= '+data[26]+' e-cm \n')
f.write('\\end{itemize}\n')

f.write('\\begin{figure*}[ht]\n')
f.write('   \\centering\n')
f.write('    \\begin{subfigure}{0.5\\textwidth}\n')
f.write('        \\centering\n')
f.write('        \\includegraphics[width=\\textwidth]{'+Bestfig+'}\n')
f.write('        \\caption{Best fit}\n')
f.write('    \\end{subfigure}%\n')
f.write('    ~ \n')
f.write('    \\begin{subfigure}{0.5\\textwidth}\n')
f.write('        \\centering\n')
f.write('        \\includegraphics[width=\\textwidth]{'+Worstfig+'}\n')
f.write('        \\caption{Worst fit}\n')
f.write('\\end{subfigure}\n')
f.write('\\caption{Out of phase component versus magnetic field}\n')
f.write('\\end{figure*}\n')

f.write('\\end{document}')

f.close()
path=os.path.abspath(tfile)
os.system('pdflatex '+path)
