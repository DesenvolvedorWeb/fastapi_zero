
## Tailwind CSS

Este projeto usa Tailwind CSS para estilização. Para trabalhar com o Tailwind:

1. Instale as dependências:
   ```bash
   npm install
   ```

2. Para desenvolvimento (observa mudanças e recompila automaticamente):
   ```bash
   npm run watch:css
   # ou
   task css
   ```

3. Para produção (minifica o CSS):
   ```bash
   npm run build:css
   ```

4. Os estilos são compilados de `static/css/input.css` para `static/css/styles.css`

5. Todas as classes do Tailwind estão disponíveis nos templates HTML

