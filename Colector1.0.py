from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False) #abre o chromium, por padrao é headless
    context = navegador.new_context() #permite gerenciar varias paginas
    
    ansitraWeb = context.new_page() #abre uma aba no navegador
    
    ansitraWeb.goto("http://localhost:8080/sat_rotaoeste/ControladorLogin") #vai ate a pagina na string
    #page.go_back() # setinha de voltar no navegador    
        
    ansitraWeb.screenshot(path="C://Stine//WebLogin.png")
    
    navegador.close() #fecha o chromium
    
    # python -m PyInstaller --clean --noconfirm -F --name MainStine .\Colector1.0.py