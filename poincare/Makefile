.PHONY: all clean

all: report.pdf

report.pdf: report.tex
	pdflatex -interaction=nonstopmode report.tex
	pdflatex -interaction=nonstopmode report.tex

clean:
	rm -f *.aux *.log *.out *.pdf *.toc *.lof *.lot *.fls *.fdb_latexmk texput.log
