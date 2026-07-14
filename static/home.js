async function  carregar_transacoes() {
    const resposta = await fetch('/transacoes');
    const contas = await resposta.json();

    console.log(contas);

    preencher_transacoes(contas.transacoes);

}

function preencher_transacoes(transacoes){
    const tbody = document.querySelector('#transacoes tbody')

    transacoes.forEach((transacao)=>{
        const linha = document.createElement("tr");
        
        linha.innerHTML = `
            <td>${transacao.descricao}</td>
            <td>${transacao.valor}</td>
            <td>${transacao.tipo}</td>
            <td>${transacao.categoria}</td>
            <td>${transacao.data}</td>
            <td>${transacao.status}</td>
        `;

        tbody.appendChild(linha);

    });
}

carregar_transacoes()