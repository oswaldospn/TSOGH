function criarTabela(botao) {
  //Desabilita botão criar
  botao.disabled = true;
  //Cria tabela
  t = document.createElement("TABLE");
  t.id = "T1";
  //Cria corpo da tabela
  tb = document.createElement("TBODY");
  //Cria linha
  l = document.createElement("TR");
  //Cria primeira célula para a linha
  c1 = document.createElement("TH");
  x = document.createTextNode("Nome completo");
  c1.width = "100px";
  c1.appendChild(x);
  c1.label 
  c1.class="label" 
  c1.for="label1"
  //Cria segunda célula para a linha
  c2 = document.createElement("TH");
  x = document.createTextNode("Cargo");
  c2.width = "100px";
  c2.appendChild(x);
  c2.label 
  c2.class="label" 
  c2.for="label2"


  c3 = document.createElement("TH");
  x = document.createTextNode("E-mail");
  c3.width = "100px";
  c3.appendChild(x);
  c3.label 
  c3.class="label" 
  c3.for="label3"


  c4 = document.createElement("TH");
  x = document.createTextNode("Data de admissão");
  c4.width = "100px";
  c4.appendChild(x);
  c4.label 
  c4.class="label" 
  c4.for="label4"


  c5 = document.createElement("TH");
  x = document.createTextNode("Anos de empresa");
  c5.width = "100px";
  c5.appendChild(x);
  c5.label 
  c5.class="label" 
  c5.for="label5"


  c6 = document.createElement("TH");
  x = document.createTextNode("Salário bruto");
  c6.width = "100px";
  c6.appendChild(x);
  c6.label 
  c6.class="label" 
  c6.for="label6"


  c7 = document.createElement("TH");
  x = document.createTextNode("Salário liquido");
  c7.width = "100px";
  c7.appendChild(x);
  c7.label 
  c7.class="label" 
  c7.for="label7"



 
  l.appendChild(c1); // adiciona célula a linha
  l.appendChild(c2); // adiciona célula a linha
  l.appendChild(c3); // adiciona célula a linha
  l.appendChild(c4);
  l.appendChild(c5);
  l.appendChild(c6);
  l.appendChild(c7);
  tb.appendChild(l); // adiciona linha ao corpo tabela
  t.appendChild(tb); // adicionar corpo a tabela
  t.border = 2;
  document.body.appendChild(t); // adiciona tabela ao documento
}
function incluirLinha() {
  T1 = document.getElementById("T1"); // obtem tabela
  TR = T1.insertRow(T1.rows.length); // insere linha final
  TR.innerHTML =
    "<td><input class='ic' type='text' value='' id='saida1' name='saida1'/></td>" +
    "<td><input class='ic' type='text' value='' id='saida2' name='saida2'/></td>" +
    "<td><input class='ic' type='text' value='' id='saida3' name='saida3'/></td>" +
    "<td><input class='ic' type='text' value='' id='saida4' name='saida4'/></td>" +
    "<td><input class='ic' type='text' value='' id='saida5' name='saida5'/></td>" +
    "<td><input class='ic' type='text' value='' id='saida6' name='saida6'/></td>" +
    "<td><input class='ic' type='text' value='' id='saida7' name='saida7'/></td>" ;
}

