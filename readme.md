# <samp>Instrucciones de compilación</samp>

Este proyecto utiliza el paquete `minted` para renderizar código fuente Python con resaltado de sintaxis.  
Por ello, es necesario:

- habilitar `shell-escape` al compilar,
- tener Python instalado,
- y contar con la librería `Pygments`.

## Requisitos

### Linux / macOS

Verifica que tengas instalado:

- TeX Live
- Python 3
- pip

Instala `Pygments`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install Pygments
```

### Arch Linux

Instala las dependencias necesarias:

```bash
sudo pacman -S texlive texlive-latexextra python python-pip biber
```

Luego instala `Pygments`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install Pygments
```


## Compilación del documento

Compila desde la raíz del proyecto ejecutando:

```bash
pdflatex -shell-escape main.tex
```

Si realizaste cambios en referencias cruzadas, índices, figuras o ecuaciones numeradas, recompila una segunda vez:

```bash
pdflatex -shell-escape main.tex
pdflatex -shell-escape main.tex
```

Si además modificaste el archivo de bibliografía (`.bib`), ejecuta:

```bash
pdflatex -shell-escape main.tex
biber main
pdflatex -shell-escape main.tex
pdflatex -shell-escape main.tex
```

## Overleaf

El proyecto es compatible con Overleaf. `minted` y `shell-escape` están habilitados automáticamente en Overleaf, por lo que no se requiere configuración adicional. En caso de problemas de compilación:

1. Ve a **Menu → Compiler**
2. Selecciona: `pdfLaTeX`
3. Recompila el proyecto.

## Estructura del proyecto

El documento principal es `main.tex`. Las secciones se encuentran en [sections/](./sections/). El código fuente Python utilizado en los reportes se encuentra en [code/](./code/), y las imágenes y gráficas deben almacenarse en [images/](./images/)
