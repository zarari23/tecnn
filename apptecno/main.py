from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
import webbrowser
import json

class MainApp(MDApp):

    Window.size = (405, 720)
    infoapp = None

    def build(self):
        self.title = "main"
        # self.theme_cls.primary_palette = ""
        # self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")
        

    def on_start(self):
        Clock.schedule_interval(self.tem, 0)
        Clock.schedule_interval(self.spect, 0)
        Clock.schedule_interval(self.ita, 0)
        Clock.schedule_interval(self.aggiungiinfo, 0)
        Clock.schedule_interval(self.startinfo, 0)

    def tem(self, *args):
        store = JsonStore('archivio.json')
        if store.exists('tema'):
            if store.get('tema')['set'] == 'scuro':
                self.theme_cls.theme_style = "Dark"
            if store.get('tema')['set'] == 'chiaro':
                self.theme_cls.theme_style = "Light"
        else:
            pass

    def spect(self, *args):
        if self.theme_cls.theme_style == "Dark":
            self.root.ids["scuro"].active = True
        elif self.theme_cls.theme_style == "Light":
            self.root.ids["chiaro"].active = True


# LINGUE

    # def lang(self, *args):
    #     # lingua = "ita"
    #     store = JsonStore('archivio.json')
    #     if store.exists('lingua'):
    #         if store.get('lingua')['set'] == "ita":
    #             self.ita()
    #             pass
    #         if store.get('lingua')['set'] == "en":
    #             self.en()

    # def spectlang(self, *args):
    #     store = JsonStore('archivio.json')
    #     if store.exists('lingua'):
    #         if store.get('lingua')['set'] == "ita":
    #             self.root.ids["ita"].active = True
    #         elif store.get('lingua')['set'] == "en":
    #             self.root.ids["en"].active = True

    def ita(self, *args):
        self.root.ids["toolhome"].title = "Combustibili Fossili"
        self.root.ids["combfoss"].text = "I combustibili fossili"
        self.root.ids["combfosstext"].text = "I combustibili fossili ricoprono l’80% del fabbisogno energetico mondiale. Il loro massiccio utilizzo negli ultimi decenni ha fatto aumentare l’effetto serra in maniera esponenziale. A provocare l’effetto serra è l’anidride carbonica, che si sprigiona in grande quantità dalla combustione degli idrocarburi (sostanze composte da idrogeno e carbonio)."
        self.root.ids["effettoserra"].text = "L'effetto serra"
        self.root.ids["effettoserratext"].text = "L’effetto serra è il principale responsabile del surriscaldamento globale e, in generale, del cambiamento climatico."
        self.root.ids["ridurreleemissioni"].text = "Ridurre le emissioni"
        self.root.ids["ridurreleemissionitext"].text = "Per ridurre le emissioni e di conseguenza l’effetto serra si possono seguire 2 strade: \n - la prima, più immediata, è quella di raggiungere un alto livello di efficienza energetica;\n - con la seconda, inevitabile in un prossimo futuro, si risolve il problema a monte: verranno utilizzate fonti di energia rinnovabile e meno inquinante."
        self.root.ids["fontialternativetoolb"].title = "Fonti Alternative"
        self.root.ids["efficienzaenergetica"].text = "L'efficienza energetica"
        self.root.ids["efficienzaenergeticatext"].text = "Il termine efficienza energetica indica la capacità di un sistema fisico (impianto di illuminazione, impianto di riscaldamento ecc...) di ottenere le prestazioni richieste pur riducendo i consumi di energia. Per ogni “livello” di efficienza energetica sono state create le classi di efficienza energetica assegnate agli elettrodomestici o agli edifici in base a dei parametri di consumo."
        self.root.ids["biomasse"].text = "Le biomasse"
        self.root.ids["biomassetext"].text = "Con il termine biomassa si indicano una serie di materiali di origine biologica. Si tratta generalmente scarti di attività agricole che possono essere modificati attraverso vari procedimenti per ricavarne combustibili o direttamente energia elettrica e termica. Le biomasse ricoprono il 10% del fabbisogno energetico totale."
        self.root.ids["centraleidroelettrica"].text = "Le centrali idroelettriche"
        self.root.ids["centraleidroelettricatext"].text = "Le centrali idroelettriche sfruttano l’energia potenziale di grandi masse d’acqua che, con l’ausilio di alternatori e turbine, trasformano in energia elettrica."
        self.root.ids["energiaeolica"].text = "L'energia eolica"
        self.root.ids["energiaeolicatext"].text = "L’energia eolica sfrutta la potenza del vento. Per ricavare l’energia dalla forza del vento si utilizzano grandi  turbine che sono localizzate in luoghi molto ventosi. Funzionamento: il vento fa girare le eliche della turbina che trasmette l’energia meccanica ad un generatore che, a sua volta, trasforma l’energia meccanica in elettrica."
        self.root.ids["fotovoltaico"].text = "L'energia fotovoltaica"
        self.root.ids["fotovoltaicotext"].text = "L’energia fotovoltaica si ricava dai pannelli fotovoltaici che trasformano direttamente la luce solare in energia elettrica. Questo processo avviene grazie al silicio, adeguatamente trattato, che ricopre i pannelli fotovoltaici."
        self.root.ids["nucleare"].text = "L'energia nucleare"
        self.root.ids["nuclearetext"].text = "L’energia nucleare è una fonte energetica primaria. Con le centrali nucleari si produce energia elettrica. Nella centrale nucleare si produce elettricità sfruttando il calore che si genera dai processi di fissione di barre di combustibile atomico (uranio-235 o plutonio-239). Ci sono due strade per produrre energia nucleare:\n - per fissione: il nucleo di un elemento fissile viene bombardato di neutroni; l’elemento viene diviso in due nuclei più piccoli (findere = dividere) ma una parte del nucleo originario si trasforma nell'energia che si voleva ricavare; il processo della fissione genera una reazione a catena irreversibile dalla quale si ricava l’energia."
        self.root.ids["metano"].text = "Il metano"
        self.root.ids["metanotext"].text = "Il metano è un idrocarburo allo stato gassoso composto da quattro atomi di idrogeno e da uno di carbonio. Bruciando, quindi, genera una quantità relativamente bassa di anidride carbonica. Viene estratto da sotto la roccia e convogliato in grandi tubi per portarlo ai centri di stoccaggio."
        self.root.ids["usimetano"].text = "Usi del metano"
        self.root.ids["usimetanotext"].text = "Il metano viene usato nel settore residenziale per il riscaldamento delle abitazioni e per i fornelli; nella produzione di energia elettrica; come carburante per automobili; per alimentare gli stabilimenti industriali."
        self.root.ids["trasporto"].text = "Il trasporto del metano"
        self.root.ids["trasportotext"].text = "Il metano viene trasportato allo stato gassoso attraverso i gasdotti (grandi tubi), oppure allo stato liquido nelle navi metaniere. I gasdotti permettono il trasporto di ingenti quantità di gas, direttamente dal luogo di produzione fino al luogo di consumo, senza bisogno di alcuna operazione di carico o immagazzinamento."
        self.root.ids["gasdottiprinc"].text = "I gasdotti principali"
        self.root.ids["gasdottiprinctext"].text = "I gasdotti sono grandi tubi utilizzati per trasportare il metano. Il loro diametro dei gasdotti varia tra i 50 millimetri e i 1.400 millimetri. I più importanti sono:\n - Blue Stream e TurkStream\n - Nord Stream\n - Greenstream\n - Gasdotto Enrico Mattei"
        self.root.ids["riserve"].text = "Le riserve principali"
        self.root.ids["riservetext"].text = "Le riserve più importanti di metano si trovano in Russia, in Medio Oriente e negli Stati Uniti."

    # def setita(self):
    #     store = JsonStore('archivio.json')
    #     store.put('lingua', set = 'ita')
    #     # store.put('tshirtman', name = 'Gabriel', age = 27)
    
    # def seten(self):
    #     store = JsonStore('archivio.json')
    #     store.put('lingua', set = 'en')
    #     # store.put('tshirtman', name = 'Gabriel', age = 27)

    def aggiungiinfo(self, *args):
        store = JsonStore('archivio.json')
        if not store.exists('startinfo'):
            store.put('startinfo', set = 'non_fatto')

    def startinfo(self, *args):
        store = JsonStore('archivio.json')
        if store.exists('startinfo'):
            if store.get('startinfo')['set'] == 'non_fatto':
                self.infapp()
            else:
                pass

    def sett(self):
        self.root.ids["screenmanager"].current = "settt"
        self.root.ids["screenmanager"].transition.direction = 'up'
        self.root.ids["nav_drawer"].set_state("close")

    def st(self):
        self.root.ids["screenmanager"].current = "settt"
        self.root.ids["screenmanager"].transition.direction = 'right'

    def tema(self):
        self.root.ids["screenmanager"].current = "tema"
        self.root.ids["screenmanager"].transition.direction = 'left'

    def lingua(self):
        self.root.ids["screenmanager"].current = "lingua"
        self.root.ids["screenmanager"].transition.direction = 'left'

    def home(self):
        self.root.ids["screenmanager"].current = "home"
        self.root.ids["screenmanager"].transition.direction = 'down'

    def fonti(self):
        self.root.ids["screenmanager"].current = "fonti"
        self.root.ids["screenmanager"].transition.direction = 'up'
        self.root.ids["nav_drawer"].set_state("close")

    def temascuro(self):
        self.theme_cls.theme_style = "Dark"
        self.settemascuro()

    def temachiaro(self):
        self.theme_cls.theme_style = "Light"
        self.settemachiaro()

    def settemascuro(self):
        store = JsonStore('archivio.json')
        store.put('tema', set = 'scuro')
        # store.put('tshirtman', name = 'Gabriel', age = 27)
    
    def settemachiaro(self):
        store = JsonStore('archivio.json')
        store.put('tema', set = 'chiaro')
        # store.put('tshirtman', name = 'Gabriel', age = 27)

    def wiki_biomasse(self):
        webbrowser.open_new("https://it.wikipedia.org/wiki/Biomassa")

    def wiki_centrale_idroelettrica(self):
        webbrowser.open_new("https://it.wikipedia.org/wiki/Centrale_idroelettrica")

    def wiki_energia_eolica(self):
        webbrowser.open_new("https://it.wikipedia.org/wiki/Energia_eolica")

    def wiki_metano(self):
        webbrowser.open_new("https://it.wikipedia.org/wiki/Metano")

    def wiki_giacimenti_gas_naturale(self):
        webbrowser.open_new("https://it.wikipedia.org/wiki/Giacimenti_di_gas_naturale")

    def tecnologia_con_metodo(self):
        webbrowser.open_new("https://www.mondadorieducation.it/catalogo/tecnologia-con-metodo-0057028/")

    def infapp(self):
        if not self.infoapp:
            self.infoapp = MDDialog(
                title = "Informazioni App",
                text = "Puoi navigare tra le varie sezioni dell'app con le icone in basso, e scorrendo lo schermo puoi vedere gli approfondimenti sui vari argomenti.",
                size_hint_x = .8,
                auto_dismiss = False,
                buttons = [
                    MDFlatButton(
                        text = "CHIUDI", text_color = self.theme_cls.primary_color, on_release = self.chiudi
                    ),
                ],
            )
        self.infoapp.open()

    def chiudi(self, obj):
        store = JsonStore('archivio.json')
        self.infoapp.dismiss()
        store.put('startinfo', set = 'fatto') 

class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

MainApp().run()