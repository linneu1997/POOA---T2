# Programação Orientada a Objetos Avançada - T2
<p align="justify">Linneu Augusto Mendo Zanco - 769155 </br>
Julio Cesar dos Santos Oliveira Filho - 779800
 </p>
 
 ## Introdução
 <p align="justify"> O Princípio Aberto-Fechado, em programação orientada a objetos, é um princípio que diz que as classes em um programa devem ser abertas para extensão, mas fechadas para modificação. Neste trabalho, foi utilizada a linguagem de programação Python para desenvolver um programa que recupera os títulos das notícias em uma página de notícias da Internet. Foi necessário desenvolver o código do programa de maneira que ele não apenas respeitasse o Princípio Aberto-Fechado, mas também o Princípio da Responsabilidade Única. Inicialmente, o código recupera as manchetes do site da UOL.
  </p>
  
  ## Desenvolvimento
  <p align="justify"> O programa foi desenvolvido utilizando a linguagem de programação Python. Utilizou-se a biblioteca "requests" para recuperar as informações da página de notícias. Com a biblioteca "BeautifulSoup", então, foi feito o processo de "parsing". No arquivo "readhtml.py", estão contidas as classes relacionadas à leitura da URL. Já no arquivo "extractinfo.py", encontramos as classes relacionadas à extrair as informações buscadas. Dessa maneira, com a separação de responsabilidades, garantimos que nosso programa respeite o Princípo da Responsabilidade Única.
</p>
<p align="justify"> No arquivo "readhtml.py" temos duas classes, a classe abstrata "read_URL" e a classe "read_UOL" que herda o método "get_URL". A partir da classe abstrata pode-se garantir que caso seja necessário expandir o código de alguma maneira, como adicionar a leitura de outras páginas por exemplo, não será necessário alterar o código já escrito, essa expansão pode ser feita apenas pela adição de novo código, criando uma nova classe que também herda o método "get_URL", por exemplo. Esse mesmo comportamento pode ser visto no arquivo "extractinfo.py", onde temos a classe abstrata "extract" e a classe "extract_UOL" que herda seus métodos. Dessa forma podemos afirmar que o código implementado segue corretamente o Prncípio Aberto-Fechado, sendo possível alterá-lo para adicionar novas funcionalidades, modificando o minímo possível do código já escrito. </p>

## Execução
<p align="justify"> Para executar o código, primeiramente instale os arquivos "readhtml.py", "extractinfo.py" e "main.py". Para rodar, no terminal utilize o comando "python3 main.py". Após a execução do programa, será gerado um arquivo .csv contendo os títulos das notícias da página de notícias escolhida.</p>
 
 ## Expansão
 <p align="justify"> Seguindo o Princípio Aberto-Fechado, podemos expandir o código para adicionar novas funcionalidades sem realizar mudanças significativas no código previamente escrito. Para adicionarmos um novo site como opção para a listagem de títulos, devemos inicialmente adicionar uma nova classe no arquivo "readhtml.py", que irá herdar os métodos da classe abstrata "read_URL". Essa nova classe deve adaptar o método "get_URL" para ler a URL da página desejada. Então, devemos adicionar uma nova classe ao arquivo "extractinfo.py", que herdará da classe abstrata "extract". Nessa nova classe devemos escrever o método "news_title" de maneira correta a obter as manchetes do site a partir das classes definidas pelo código html da página de notícias. Por fim, deve-se alteraar o código do arquivo "main.py" para adicionar a opção ao usuário de recuperar manchets do novo site. </p>
 <p align="jusify"> Para se adicionar novos algoritmos, as alterações devem ser feitas no código do arquivo "extractinfo.py". Devemos adicionar novos métodos às classes abstrata e herdeiras, que deverão corretamente extrair as informações buscadas, como o link da notícia ou o conteúdo dessas, por exemplo. O código de "main.py" também deve ser alterado para permitir ao usuário escolher essas novas opções.</p>
 
 ## Conclusão
 <p align="justify"> O código desenvolvido obtém corretamente as manchetes das notícias publicadas na página da UOL. Além disso, o código segue o Princípio Aberto-Fechado, possibilitando facilmente a expansão do código sem realizar modificações para contemplar as adições previstas pelas extensões 1 e 2 descritas no arquivo do trabalho.</p>
