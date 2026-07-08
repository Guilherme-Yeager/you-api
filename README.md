<div align="center">
  
  # You API
  
</div>

Uma API desenvolvida para o gerenciamento de "momentos". Para mais detalhes do projeto verifique: [You.](https://github.com/Guilherme-Yeager/you)

<div align="center">
  
  ### Armazenamento
  
</div>

Esta API **não utiliza nenhum banco de dados** no momento. Todos os dados são salvos em estruturas de dados em memória para teste.
Isso significa que **sempre que o servidor for reiniciado, os dados inseridos serão perdidos**.

<div align="center">
  
  ### Documentação (Swagger)

</div>

A API possui uma interface visual do Swagger para testar os endpoints diretamente do navegador.

Com a aplicação rodando, acesse:

```text
http://localhost:5000/apidocs/
```

<img width="3881" height="2009" alt="You API" src="https://github.com/user-attachments/assets/8a5854b8-e54f-4d82-aeac-d7622bf627e0" />

<div align="center">
  
  ### Rotas da API
  
</div>

### `POST /momentos/`

Insere um novo momento.

**Payload:**

```json
{
  "descricao": "Fiz meus primeiros 10km.",
  "timestamp": "2026-07-07T20:48:00-03:00",
  "latitude": -10.689931630776984,
  "longitude": -37.42178240832807
}
```

### `GET /momentos/`

Lista os momentos cadastrados. Suporta filtros via Query String.

**Filtros Disponíveis:**

* `?ultimo=true` : Retorna apenas o último momento inserido.

<div align="center">
  
  ### Tecnologias Utilizadas
  
</div>

* **Python**
* **Flask** (Framework Web)
