# TEXT TO SPEECH

Ferramenta de conversão de texto para áudio por meio da API gtts.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-<COLOR>.svg)](https://shields.io/)
[![Status](https://img.shields.io/badge/Status-Concluído-green)](https://shields.io)

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Instruções](#instrucoes)
* [Lista de idiomas](#lista-de-idiomas)
* [Licença](#licença)

# Descrição do Projeto

Ferramenta de conversão de texto para áudio utilizando a API gtts. A ferramenta recebe como parâmetros o texto a ser convertido, o idioma em forma de código e o caminho onde se deseja salvar o áudio.

## Tecnologias utilizadas

- [Python versão 3](https://docs.python.org/3/)
- [Pacote gtts](https://gtts.readthedocs.io/en/latest/)

## Instruções

1. É necessário rodar esse aplicativo em um ambiente virtual python. Veja este [tutorial](https://github.com/cesarcalafrioli/tutorial-ambiente-virtual-python) para saber como.
2. Instale os pacotes listados acima.
3. Instale os requisitos desse projeto
    ```
    pip install -r requirements.txt
    ```
4. Rode a aplicação
    ```
    python text-to-speech.py <TEXTO  A SER CONVERTIDO> <IDIOMA ( VER LISTA ABAIXO )> <DIRETÓRIO PARA SALVAR O ARQUIVO CONVERTIDO>
    ```
    Exemplo
    
    ```
    python text-to-speech.py "Hello World!" en /home/audio
    ```
   
## Lista de idiomas
   
 | Código | Idioma  | Código | Idioma  |
| --- | ----------- | --- | ----------- |
| af | Afrikaans Afrikaans | sq sq | Albanian Albanês
| ar-sa ar-sa | Arabic (Saudi Arabia) Árabe (Arábia Saudita) | ar-iq ar-iq | Arabic (Iraq) Árabe (Iraque) |
| ar-eg ar-eg | Arabic (Egypt) Árabe (Egito) | ar-ly ar-ly | Arabic (Libya) Árabe (Líbia) |
| ar-dz ar-dz | Arabic (Algeria) Árabe (Argélia) | ar-ma ar-ma | Arabic (Morocco) Árabe (Marrocos) | 
| ar-tn ar-tn | Arabic (Tunisia) Árabe (Tunísia) | ar-om ar-om | Arabic (Oman) Árabe (Omã) |
| ar-ye ar-vos | Arabic (Yemen) Árabe (Iêmen) | ar-sy ar-sy | Arabic (Syria) Árabe (Síria) | 
| ar-jo ar-jo | Arabic (Jordan) Árabe (Jordânia) | ar-lb ar-lb | Arabic (Lebanon) Árabe (no Líbano) |
| ar-kw ar-kw | Arabic (Kuwait) Árabe (Kuwait) | ar-ae ar-ae | Arabic (UAE) Árabe (EAU) | 
| ar-bh ar-bh | Arabic (Bahrain) Árabe (Bahrain) | ar-qa ar-qa | Arabic (Qatar) Árabe (Catar) | 
| eu UE | Basque Basco | bg bg | Bulgarian Búlgaro | 
| be ser | Belarusian Bielorrússia | ca ca | Catalan Catalão | 
| zh-tw zh-tw | Chinese (Taiwan) Chinês (Taiwan) | zh-cn zh-cn | Chinese (PRC) Chinês (PRC) |
| zh-hk zh-hk | Chinese (Hong Kong SAR) Chinês (RAE de Hong Kong) | zh-sg zh-sg | Chinese (Singapore) Chinês (Cingapura) |
| hr hr | Croatian Croata | cs cs | Czech Checa |
| da da | Danish Dinamarquês | nl nl | Dutch (Standard) Holandês (Standard) |
| nl-be nl-be | Dutch (Belgium) Holandês (Bélgica) | en en | English Inglês | 
| en-us en-us | English (United States) Inglês (Estados Unidos) | en-gb pt-br | English (United Kingdom) Inglês (Reino Unido) |
| en-au en-au | English (Australia) Inglês (Austrália) | en-ca en ca- | English (Canada) Inglês (Canadá) |
| en-nz en-nz | English (New Zealand) Inglês (Nova Zelândia) | "en-ie ou seja, en-" | English (Ireland) Inglês (Irlanda) |
| en-za en-za | English (South Africa) Inglês (África do Sul) | en-jm en-jm | English (Jamaica) Inglês (Jamaica) |
| en en | English (Caribbean) Inglês (Caribe) | en-bz en-bz | English (Belize) Inglês (Belize) |
| en-tt pt-tt | English (Trinidad) Inglês (Trinidad) | et et | Estonian Estoniano |
| fo para | Faeroese Das Ilhas Faroé | fa fa | Farsi Persa |
| fi fi | Finnish Finlandesa | fr fr | French (Standard) Francês (França) |
| fr-be fr-se | French (Belgium) Francês (Bélgica) | fr-ca fr-ca | French (Canada) Francês (Canadá) |
| fr-ch fr-ch | French (Switzerland) Francês (Suíça) | fr-lu fr-lu | French (Luxembourg) Francês (Luxemburgo) |
| gd gd | Gaelic (Scotland) Gaélico (Escócia) | ga ga | Irish Irlandês |
| de de | German (Standard) Alemão (Standard) | de-ch de-ch | German (Switzerland) Alemão (Suíça) |
| de-at de-at | German (Austria) Alemão (Áustria) | de-lu de lu- | German (Luxembourg) Alemão (Luxemburgo) |
| de-li de-li | German (Liechtenstein) Alemão (Liechtenstein) | el el | Greek Grego |
| he ele | Hebrew Hebraico | hi oi | Hindi Hindi | 
| hu hu | Hungarian Húngaro | is é | Icelandic Islandesa |
| id id | Indonesian Indonésio | it ele | Italian (Standard) Italiano (Standard) | 
| it-ch it-ch | Italian (Switzerland) Italiano (Suíça) | ja ja | Japanese Japonês |
| ko ko | Korean Coreano | ko ko | Korean (Johab) Coreano (Johab) |
| lv lv | Latvian Letã | lt lt | Lithuanian Lituano |
| mk mk | Macedonian (FYROM) Macedônio (FYROM) | ms ms | Malaysian Malásia |
| mt mt | Maltese Maltês | no não | Norwegian (Bokmal) Norueguês (bokmal) |
| no não | Norwegian (Nynorsk) Norueguês (Nynorsk) | pl pl | Polish Polonês |
| pt-br pt-br | Portuguese (Brazil) Português (Brasil) | pt pt | Portuguese (Portugal) Português (Portugal) |
| rm rm | Rhaeto-Romanic Reto-românico | ro ro | Romanian Romeno |
| ro-mo ro mo- | Romanian (Republic of Moldova) Romeno (República da Moldávia) | ru ru | Russian Russo |
| ru-mo ru-mo | Russian (Republic of Moldova) Russo (República da Moldávia) | sz sz | Sami (Lappish) Sami (Lapónia) |
| sr SR | Serbian (Cyrillic) Sérvio (cirílico) | sr SR | Serbian (Latin) Sérvio (Latim) |
| sk sk | Slovak Eslovaca | sl SL | Slovenian Esloveno |
| sb sb | Sorbian Sorbian | es es | Spanish (Spain) Espanhol (Espanha) |
| es-mx es-mx | Spanish (Mexico) Espanhol (México) | es-gt es-gt | Spanish (Guatemala) Espanhol (Guatemala) |
| es-cr es-cr | Spanish (Costa Rica) Espanhol (Costa Rica) | es-pa es pa- | Spanish (Panama) Espanhol (Panamá) |
| es-do es-do | Spanish (Dominican Republic) Espanhol (República Dominicana) | es-ve es-ve | Spanish (Venezuela) Espanhol (Venezuela) |
| es-co es co- | Spanish (Colombia) Espanhol (Colômbia) | es-pe es-pe | Spanish (Peru) Espanhol (Peru) |
| es-ar es-ar | Spanish (Argentina) Espanhol (Argentina) | es-ec es-CE | Spanish (Ecuador) Espanhol (Equador) |
| es-cl es-cl | Spanish (Chile) Espanhol (Chile) | es-uy es-uy | Spanish (Uruguay) Espanhol (Uruguai) |
| es-py es-py | Spanish (Paraguay) Espanhol (Paraguai) | es-bo es-bo | Spanish (Bolivia) Espanhol (Bolívia) |
| es-sv es-sv | Spanish (El Salvador) Espanhol (El Salvador) | es-hn es-hn | Spanish (Honduras) Espanhol (Honduras) |
| es-ni es-ni | Spanish (Nicaragua) Espanhol (Nicarágua) | es-pr es-pr | Spanish (Puerto Rico) Espanhol (Porto Rico) |
| sx sx | Sutu À sutura | sv sv | Swedish Sueco |
| sv-fi sv-fi | Swedish (Finland) Sueco (Finlândia) | th ª | Thai Tailandês |
| ts ts | Tsonga Tsonga | tn tn | Tswana Tswana |
| tr tr | Turkish Turco | uk Reino Unido | Ukrainian Ucraniano |
| ur ur | Urdu Urdu | ve ve | Venda Venda |
| vi vi | Vietnamese Vietnamita | xh xh | Xhosa Xhosa |
| ji ji | Yiddish Ídiche | zu zu | Zulu Zulu |


## Licença

[Licença MIT](./LICENSE) © César Augusto de Carvalho Calafrioli Móes
