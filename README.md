# Transcrição de Vídeos do YouTube

Este é um programa em Python que permite transcrever vídeos do YouTube diretamente para texto. Ele utiliza a biblioteca `youtube_transcript_api` para extrair legendas (se disponíveis) e exibi-las em uma interface gráfica simples.

## Funcionalidades

- **Transcrição Automática:** Extrai legendas de vídeos do YouTube (geradas pelo criador ou automáticas).
- **Interface Gráfica:** Interface amigável para inserir a URL do vídeo e visualizar a transcrição.
- **Copiar Texto:** Botão para copiar a transcrição gerada para a área de transferência.
- **Suporte a Múltiplos Idiomas:** Prioriza legendas em português (`pt`), mas também suporta inglês (`en`).

## Requisitos

- Python 3.6 ou superior
- Bibliotecas necessárias:
  - `pytube`
  - `youtube_transcript_api`
  - `tkinter` (já vem com o Python)

## Como Usar

1. **Instale as dependências:**
   ```bash
   pip install pytube youtube_transcript_api
   ```

2. **Execute o programa:**
   ```bash
   python transcricao_youtube.py
   ```

3. **Interface Gráfica:**
   - Insira a URL do vídeo do YouTube no campo de texto.
   - Clique em **"Obter Transcrição"** para gerar a transcrição.
   - Use o botão **"Copiar Texto"** para copiar a transcrição para a área de transferência.

4. **Exemplo de Uso:**
   - URL de exemplo: `https://www.youtube.com/watch?v=7IwU2JLCQ7w`
   - A transcrição será exibida na caixa de texto abaixo.

## Limitações

- O vídeo deve ter legendas disponíveis (geradas pelo criador ou automáticas).
- Vídeos com restrições de direitos autorais podem não permitir o acesso às legendas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorar o projeto.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

