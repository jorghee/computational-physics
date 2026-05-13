### <samp>Instrucciones de compilación<samp>

Dado que este proyecto hace uso del paquete `minted` para renderizar el código Python, **necesitas habilitar la ejecución externa (shell escape)** al compilar, y tener **Python con la librería `Pygments` instalada** en tu sistema.

1. Instala Pygments en tu entorno virtual python (si no lo tienes):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install Pygments
   ```
2. Compila el documento principal pasándole el argumento `-shell-escape`:
   ```bash
   pdflatex -shell-escape main.tex
   biber main                # (si modificaste citas bibliográficas)
   pdflatex -shell-escape main.tex
   pdflatex -shell-escape main.tex
   ```
*Nota: Si utilizas un editor como **Overleaf**, `minted` y el flag `-shell-escape` ya están habilitados por defecto, por lo que el proyecto compilará inmediatamente.*
