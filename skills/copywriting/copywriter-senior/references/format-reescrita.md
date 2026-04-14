# Formato: Reescrita, Extração de Tom e Humanização

Engloba três tarefas relacionadas: reescrever copy fora do tom, extrair o tom do expert e humanizar textos com cara de IA.

---

## 1. Reescrever Copy Fora do Tom

### Entradas necessárias
- Transcrições de aulas ou reuniões do expert.
- Copies antigas aprovadas (e-mails, WhatsApp, páginas).
- Qualquer material que mostre como o expert fala.

### Processo
1. Ler material do expert e extrair padrões (vocabulário, ritmo, expressões).
2. Manter o **conteúdo** da copy original.
3. Adaptar **forma, ritmo e vocabulário** para o tom real do expert.

### Super Prompt
> Esta copy está fora da linguagem do expert. Para reescrever corretamente, envie: (1) Transcrições de aulas ou reuniões do expert, (2) Copies antigas aprovadas (e-mails, WhatsApp), (3) Qualquer material que mostre como ele/ela fala. Com base nisso, vou extrair a linguagem e reescrever as peças mantendo o conteúdo e adaptando para o tom real do expert.

---

## 2. Extrair Comunicação do Expert

Produz um documento de referência reutilizável para todas as campanhas.

### Entradas
- Transcrições de aulas.
- Transcrições de reuniões.
- Copies aprovadas (e-mails, WhatsApp, páginas, lives).

### O que extrair
- Vocabulário característico (palavras e gírias que o expert usa).
- Expressões recorrentes.
- Estrutura de raciocínio (como ele monta argumentos).
- Tom emocional predominante.
- Ritmo de escrita/fala.
- Como se conecta com o público (analogias, referências, exemplos).

### Super Prompt
> Preciso criar um documento de comunicação do expert para usar em todas as campanhas. Envie: (1) Transcrições de aulas, (2) Transcrições de reuniões, (3) Copies aprovadas de campanhas anteriores (e-mails, WhatsApp, páginas). Com base nesses materiais, vou extrair: vocabulário característico, expressões recorrentes, estrutura de raciocínio, tom emocional, ritmo de escrita e como o expert se conecta com o público. Entrego em artefato detalhado para guiar todas as próximas campanhas.

---

## 3. Humanizar Texto Robotizado

### Entradas
- Documento de comunicação do expert (se existir).
- Texto a ser reescrito.
- Tom desejado.

### Processo
- Passar pela skill `anti-ia-writing`.
- Cortar conectivos mecânicos ("além disso", "por outro lado").
- Variar tamanho de frase.
- Inserir transições naturais e referências ao parágrafo anterior.

### Super Prompt
> Este texto está robotizado, sem fluidez e sem conexão entre os parágrafos. Preciso reescrever entendendo que estamos falando com humanos reais. Envie: (1) Documento de comunicação do expert (se existir), (2) O texto a ser reescrito, (3) Tom desejado. Vou reescrever com linguagem leve, fluida, com transições naturais, sem padrões de IA, para que qualquer pessoa leia com facilidade e prazer.

---

## Seguir Documento de Referência (estrutura sem copiar conteúdo)

> Tenho um documento de referência e preciso que o novo texto siga sua estrutura e lógica, mas com conteúdo completamente diferente. Não copie o texto, apenas siga o modelo: mesma estrutura, mesmo tipo de argumento, mesmo fluxo. O conteúdo novo está nos documentos que estou enviando junto.

---

## Regra Anti-Fakes (aplica a tudo)

> REGRA ABSOLUTA: Nunca criar copies com informações falsas, métricas inventadas, nomes aleatórios, depoimentos fictícios ou cases de sucesso fabricados. Sempre usar fontes reais e validadas. Quando não houver dados disponíveis, deixar o espaço em aberto: [Nome do aluno], [X% de aprovação], [Número de casos]. Se buscar dados externos, trazer a fonte com URL para validação.
