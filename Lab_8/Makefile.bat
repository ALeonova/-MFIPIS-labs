pandoc L8_Leonova_report.md -F pandoc-crossref --number-sections --citeproc -o L8_Leonova_report.docx
pandoc L8_Leonova_report.md -F pandoc-crossref --pdf-engine=xelatex --pdf-engine-opt=--shell-escape --citeproc --number-sections -o L8_Leonova_report.pdf
pandoc L8_Leonova_presentation.md -F pandoc-crossref --pdf-engine=lualatex --number-sections -t beamer --slide-level=2 -o L8_Leonova_presentation.pdf
