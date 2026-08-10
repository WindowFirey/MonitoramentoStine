#teste playwright

from playwright.sync_api import sync_playwright
import time #só pra teste, não é ideal usar

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False) #abre o chromium, por padrao é headless
    context = navegador.new_context() #permite gerenciar varias paginas
    
    page = navegador.new_page() #abre uma aba no navegador
    
    page.goto("https://playwright.dev/python/docs/writing-tests") #vai ate a pagina na string
    #page.go_back() # setinha de voltar no navegador
    page.screenshot(path="C://Temp//TesteColector//teste1.png")
    
    #Locators
    #xpath, nao recomendavel        page.locator('xpath=//*[@id="__docusaurus"]/nav/div[1]/div[2]/div[1]/button/svg[2]/path').click()
    
    #[cmd do projeto] playwright codegen <link>
    #vai encontrar o local é só copiar
    page.get_by_role("link", name="Trace viewer").first.click()
    
    links = page.get_by_role("link").all()  #cria uma lista com todos (all()) os links da pagina
    for link in links:
        print(link)                         #ai da pra verificar todos os links

    
    #tira print
    page.screenshot(path="C://Temp//TesteColector//teste2.png")
        
    #time.sleep(5)
    navegador.close() #fecha o chromium
