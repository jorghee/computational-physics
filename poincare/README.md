# Compilación del Informe

El documento utiliza el paquete `TikZ` para renderizar elementos visuales en la portada (como la barra izquierda) y `listings` para mostrar el código fuente con coloreado de sintaxis.

## Cómo compilar

### Opción 1: Usar Make (Recomendado)
Se ha creado un archivo `Makefile` que automatiza el proceso y asegura que se ejecuten las pasadas necesarias. Puedes compilar el documento simplemente ejecutando:

```bash
make
```

### Opción 2: Compilar manualmente
Si prefieres hacerlo manualmente, debes ejecutar `pdflatex` **dos veces seguidas** para que las referencias de posición de la portada se calculen correctamente:

```bash
pdflatex report.tex
pdflatex report.tex
```

> **Nota sobre el código fuente:** 
> Ya no es necesario usar el flag `-shell-escape` ni tener Python/pygmentize instalado, ya que el resaltado de código ahora se maneja de forma nativa en LaTeX usando el paquete `listings`.
