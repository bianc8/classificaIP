import re
class IdentificaClassi:
    ritorno = indirizzo = binario  = ''
    ip = []
    esci = False
    future = 4

    def trova(self, indirizzo):
        self.ip = str(indirizzo).split('.')
        if len(self.ip) == 4:
            try:
                #converte in lista di interi da stringa, metodo migliore
                self.ip = list(map(int, self.ip))
                #la stringa viene salvata nell'oggetto
                self.indirizzo = str(indirizzo)
                #concatena lista self.ip in stringa usando la rappresentazione binaria
                self.binario = '.'.join(map(lambda x: str(bin(x))[2:], self.ip))
                #se tutti gli elementi della lista sono minori di 255 l'indirizzo è corretto
                if not all(i <= 255 for i in self.ip):
                    self.esci = True
            #se nel creare la lista self.ip sono contenuti caratteri alfabetici il flag ValueError scatta
            except ValueError:
                self.esci = True
            #gestire le eccezzioni per errori dati dalla concatenazione di stringe
            except IndexError:
                self.esci = True
            except TypeError:
                self.esci = True
        #se è stato inserito un indirizzo che non abbia 4 ottetti avviene un errore
        else:
            self.esci = True

    def __init__(self, indirizzo):
        #determina se l'ip inserito da utente è corretto
        self.trova(indirizzo)
        #se non avvengono errori in self.trova() si puo proseguire
        if not self.esci:
            #riempe con bit di padding gli ottetti in self.binario
            copia = self.binario+'.'
            uno = ''
            for j in range(4):
                self.binario = self.binario[:self.binario.find('.')]
                for i in range(8 - len(self.binario)):
                    self.binario = '0' + self.binario
                uno += '.' + self.binario
                self.binario = copia[copia.find('.')+1:]
                copia = copia[copia.find('.')+1:]
            self.binario = uno[1:]
            #determina la classe dell'indirizzo inserito
            self.classea()
            self.classeb()
            self.classec()
            self.classed()
            self.classee()
            # controlli per vedere se l indirizzo inserito è di default
            if self.ip == [0,0,0,0]:
                self.ritorno = 'Indirizzo IP 0.0.0.0 è l\' indirizzo di Rete di default'
            elif self.ip == [255, 255, 255, 255]:
                self.ritorno = 'Indirizzo IP 255.255.255.255 è l\' indirizzo di Broadcast di default'
            elif self.ip == [127, 0, 0, 1]:
                 self.ritorno = 'Indirizzo IP 127.0.0.1 è l\' indirizzo di Loopback di default'
        #se sono avvenuti errori in self.trova() esce e da come risultato ERRORE
        else:
            self.ritorno = 'ERRORE'
        #tupla finale che contiene (Frase di risposta, Ip base 10, Ip base 2)
        self.finale = (self.ritorno,self.indirizzo,self.binario)

    #Nelle prime tre classi di ip oltre ai controlli di appartenenza alla classe è necessario
    # controllare se l'indirizzo inserito sia privato.
    def classea(self):
        if 0 <= self.ip[0] <= 127:
            if self.ip[1] == 0 and self.ip[2] == 0 and self.ip[3] == 0:
                if self.ip[0] == 10:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato di Rete della Classe A'.format(self.indirizzo)
                else:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo di Rete della Classe A'.format(self.indirizzo)
            elif self.ip[1] == 255 and self.ip[2] == 255 and self.ip[3] == 255:
                if self.ip[0] == 10:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato di Broadcast della Classe A'.format(self.indirizzo)
                else:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo di Broadcast della Classe A'.format(self.indirizzo)
            elif self.ip[0] == 10:
                self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato della Classe A'.format(self.indirizzo)
            else:
                self.ritorno = 'L\'Indirizzo IP {0} appartiene alla Classe A'.format(self.indirizzo)
            self.future = 1

    def classeb(self):
        if 128 <= self.ip[0] <= 191:
            if self.ip[2] == 0 and self.ip[3] == 0:
                if self.ip[0] == 172 and self.ip[1] == 16:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato di Rete della Classe B'.format(self.indirizzo)
                else:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo di Rete della Classe B'.format(self.indirizzo)
            elif self.ip[2] == 255 and self.ip[3] == 255:
                if self.ip[0] == 172 and self.ip[1] == 31:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato di Broadcast della Classe B'.format(self.indirizzo)
                else:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo di Broadcast della Classe B'.format(self.indirizzo)
            elif self.ip[0] == 172 and 16 <= self.ip[1] <= 31:
                self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato della Classe B'.format(self.indirizzo)
            else:
                self.ritorno = 'L\'Indirizzo IP {0} appartiene alla Classe B'.format(self.indirizzo)
            self.future = 2

    def classec(self):
        if 192 <= self.ip[0] <= 223:
            if self.ip[3] == 0:
                if self.ip[0] == 192 and self.ip[1] == 168:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato di Rete della Classe C'.format(self.indirizzo)
                else:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo di Rete della Classe C'.format(self.indirizzo)
            elif self.ip[3] == 255:
                if self.ip[0] == 192 and self.ip[1] == 168:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato di Broadcast della Classe C'.format(self.indirizzo)
                else:
                    self.ritorno = 'Indirizzo IP {0} è un indirizzo di Broadcast della Classe C'.format(self.indirizzo)
            elif self.ip[0] == 192 and self.ip[1] == 168:
                self.ritorno = 'Indirizzo IP {0} è un indirizzo Privato della Classe C'.format(self.indirizzo)
            else:
                self.ritorno = 'L\'Indirizzo IP {0} appartiene alla Classe C'.format(self.indirizzo)
            self.future = 3

    def classed(self):
        if 224 <= self.ip[0] <= 239:
            self.ritorno = 'L\'Indirizzo IP {0} appartiene alla Classe D'.format(self.indirizzo)

    def classee(self):
        if 240 <= self.ip[0] <= 255 and 0 <= self.ip[3] <= 254:
            self.ritorno = 'L\'Indirizzo IP {0} appartiene alla Classe E'.format(self.indirizzo)

class Bitwise:
    esci = False
    dizio   = {'ip1':[],'ip2':[],'subnetmask':[]}
    address = {'ip1':[],'ip2':[],'subnetmask':[]}
    binario = {'ip1':[],'ip2':[],'subnetmask':[]}
    ritorno = ''

    def trova(self, indirizzo,dove):
        self.dizio[dove] = str(indirizzo).split('.')
        if len(self.dizio[dove]) == 4:
            try:
                self.dizio[dove] = list(map(int, self.dizio[dove]))
                self.address[dove] = str(indirizzo)
                self.binario[dove] = '.'.join(map(lambda x: str(bin(x))[2:], self.dizio[dove]))
                if not all(i <= 255 for i in self.dizio[dove]):
                    self.esci = True
            except ValueError:
                self.esci = True
            except IndexError:
                self.esci = True
            except TypeError:
                self.esci = True
        else:
            self.esci = True

    def __init__(self,ip1,ip2,subnetmask):
        self.trova(ip1,'ip1')
        self.trova(ip2,'ip2')
        self.trova(subnetmask,'subnetmask')
        if not self.esci:
            for key,value in self.binario.items():
                # bit a 0 riempitivi
                copia = self.binario[key]+'.'
                uno = ''
                for j in range(4):
                    self.binario[key] = self.binario[key][:self.binario[key].find('.')]
                    for i in range(8 - len(self.binario[key])):
                        self.binario[key] = '0' + self.binario[key]
                    uno += '.' + self.binario[key]
                    self.binario[key] = copia[copia.find('.')+1:]
                    copia = copia[copia.find('.')+1:]
                self.binario[key] = uno[1:]
            for i in range(4):
                if (self.dizio['ip1'][i] & self.dizio['subnetmask'][i]) != (self.dizio['ip2'][i] & self.dizio['subnetmask'][i]):
                    self.ritorno = 'No'
                    self.esci = True
                    break
        if not self.esci:
            self.ritorno = 'Si'
        self.ritorno = 'La messa in and è andata a buon fine? {0}'.format(self.ritorno)

class Subnetting:
    esci = False
    dizio   = {'ip' : [], 'subnetmask' : []}
    address = {'ip' : '', 'subnetmask' : ''}
    binario = {'ip' : '', 'subnetmask' : ''}
    ritorno = ''
    n_host_max = 0
    n_sub_max  = 0

    def pulisci(self):
        self.esci = False
        self.dizio   = {'ip' : [], 'subnetmask' : []}
        self.address = {'ip' : '', 'subnetmask' : ''}
        self.binario = {'ip' : '', 'subnetmask' : ''}
        self.ritorno = ''
        self.n_host_max = 0
        self.n_sub_max  = 0

    def trova(self, indirizzo,dove):
        self.dizio[dove] = str(indirizzo).split('.')
        if len(self.dizio[dove]) == 4:
            try:
                self.dizio[dove] = list(map(int, self.dizio[dove]))
                self.address[dove] = str(indirizzo)
                self.binario[dove] = '.'.join(map(lambda x: str(bin(x))[2:].rjust(8,'0'), self.dizio[dove]))
                if not all(i <= 255 for i in self.dizio[dove]):
                    self.esci = True
            except ValueError:
                self.esci = True
            except IndexError:
                self.esci = True
            except TypeError:
                self.esci = True
        else:
            self.esci = True

    def __init__(self,indirizzo, subnetmask):
        self.pulisci()
        self.trova(indirizzo,'ip')
        self.trova(subnetmask,'subnetmask')
        if not self.esci:
            #whichclass identifica la classe di appartenenza dell'indirizzo ip
            whichclass = IdentificaClassi(indirizzo).future
            copia = self.binario['subnetmask']
            #se si tratta di un indirizzo di classe A/B/C allora non da errore
            if whichclass < 4:
                #controlla se ci sono uno SOLO nei MSB(sx) e NON negli ottetti dedicati alla parte host
                self.binario['subnetmask'] = ''.join(map(lambda x: str(bin(x))[2:].rjust(8,'0'), self.dizio['subnetmask']))
                #se ci sono uni dopo gli zeri la subnet è sbagliata
                if not '1' in self.binario['subnetmask'][self.binario['subnetmask'].find('0'):]:
                    print(self.binario['subnetmask'])
                    #prende solamente l ottetto/gli ottetti dedicati alla parte host
                    for j in range(whichclass):
                            self.binario['subnetmask'] = self.binario['subnetmask'][8:]
                    meno = {1:24,2:16,3:8}
                    n_bit_1 = len(self.binario['subnetmask'][:self.binario['subnetmask'].find('0')])
                    print(n_bit_1)
                    self.n_sub_max = 2**n_bit_1
                    self.n_host_max = (2**(meno[whichclass]-n_bit_1))-2
                    self.finale = (self.n_host_max, self.n_sub_max)
                else:
                    self.esci = True
        if self.esci:
                self.finale = 'ERRORE'

class Cidr:
    esci = False
    dizio   = {'ip' : [], 'subnetmask' : []}
    binario = {'ip' : '', 'subnetmask' : ''}
    range_dec = []
    range_bin = []
    range_dec_fin = []
    fratto = 254
    n_bit_1 = 0
    finale = ()

    def pulisci(self):
        self.esci = False
        self.dizio   = {'ip' : [], 'subnetmask' : ''}
        self.binario = {'ip' : ''}
        self.range_dec = []
        self.range_bin = []
        self.fratto = 254
        self.n_bit_1 = 0
        self.finale = ()

    def trova(self, indirizzo,dove):
        self.dizio[dove] = str(indirizzo).split('.')
        if len(self.dizio[dove]) == 4:
            try:
                self.dizio[dove] = list(map(int, self.dizio[dove]))
                self.binario[dove] = '.'.join(map(lambda x: str(bin(x))[2:], self.dizio[dove]))
                if not all(i <= 255 for i in self.dizio[dove]):
                    self.esci = True
            except ValueError:
                self.esci = True
            except IndexError:
                self.esci = True
            except TypeError:
                self.esci = True
        else:
            self.esci = True

    def __init__(self,indirizzo,n_host):
        self.pulisci()
        self.trova(indirizzo,'ip')
        whichclass = IdentificaClassi(indirizzo).future
        if not self.esci:
            if (whichclass == 3) & (254 < n_host < 65535):
                n_indirizzi = round(n_host/self.fratto)
        		#crea range_dec
                for i in range(n_indirizzi):
                    lista_tmp = []
                    lista_tmp.append(self.dizio['ip'][0])
                    lista_tmp.append(self.dizio['ip'][1])
                    lista_tmp.append(self.dizio['ip'][2]+i)
                    self.range_dec.append(lista_tmp)
                cont1 = 0
                cont2 = 0
        		#corregge il range_dec per eventuali errori
                for i in range(n_indirizzi):
                    #aumenta anche il secondo ottetto se il terzo è uguale a 255
                    if (self.range_dec[i][2] > 255) & (self.range_dec[i][1] < 255) & (self.range_dec[i][0] < 223):
                        self.range_dec[i][2] = cont1
                        self.range_dec[i][1] += 1
                        cont1 += 1
        			#aumenta anche il primo ottetto se sia il terzo che il secondo ottetto sono uguali a 255
                    elif (self.range_dec[i][2] > 255) & (self.range_dec[i][1] == 255) & (self.range_dec[i][0] < 223):
                        self.range_dec[i][2] = cont1
                        self.range_dec[i][1] = cont2
                        self.range_dec[i][0] += 1
                        cont1 += 1
                        cont2 += 1
                    elif (self.range_dec[i][2] > 255) & (self.range_dec[i][1] == 255) & (self.range_dec[i][0] == 223):
                        del self.range_dec[i:]
                        break
            else:
                self.esci = True
        if not self.esci:
            #per creare subnet ho bisogno di indirizzi in binario
            string = ''
            for i in range(3):
                string += str(bin(self.range_dec[0][i]))[2:].rjust(8,'0')
            self.range_bin.append(string)
            string = ''
            for i in range(3):
                string += str(bin(self.range_dec[len(self.range_dec)-1][i]))[2:].rjust(8,'0')
            self.range_bin.append(string)
            mask_result = ''
            for i in range(24):
                if self.range_bin[0][i] == self.range_bin[1][i]:
                    mask_result += '1'
                else:
                    mask_result += '0'
            if mask_result.find('0') != -1:
                self.n_bit_1 = len(mask_result[:mask_result.find('0')])
            #se la maschera and è composto da 24 1 allora non è necessario fare il Cidr
            elif mask_result == '111111111111111111111111':
                self.n_bit_1 = 24
                self.esci = True
            if not self.esci:
                self.dizio['subnetmask'] = '.'.join(map(lambda x: str(int(x,2)), re.findall('........','1'*self.n_bit_1+'0'*(32-self.n_bit_1))))
                self.finale = ( str('.'.join(map(lambda x: str(x), self.range_dec[0]))+'.'+str(self.dizio['ip'][3])+'-'+'.'.join(map(lambda x: str(x), self.range_dec[len(self.range_dec)-1]))+'.'+str(self.dizio['ip'][3])) , self.dizio['subnetmask'])
            else:
                self.finale = ('Non è necessario fare il CIDR')
        elif (whichclass == 3) & (n_host < 255):
            self.finale = ('Non è necessario fare il CIDR per n_host minori di 255')
        elif self.finale == ():
            self.finale = 'ERRORE'
#--------------------------------MAIN PROGRAM--------------------------------
#IdentificaClassi(ip)------>classe a/b/c/d/e
#print(IdentificaClassi('192.168.10.8').future)
#print('\n')
#Subnetting(ip, subnetmask)---->Controlla se la subnetmask è corretta e da max_host e n_subnet
print(Subnetting('123.255.0.0','255.255.255.252').finale)
print('\n')
#Bitwise(ip1,ip2,subnetmask)------>Messa in And Bitwise ip1&subnetmask ip2&subnetmask
#print(Bitwise('192.168.10.8','192.168.10.2','255.255.255.128').ritorno)
#print('\n')
#CIDR(ip, n bit a 1)
#print(Cidr('223.5.25.0',255).finale)
uscita = True
while not uscita:
    ip = input('Inserisci indirizzo ip(192.168.1.1): ')
    print(IdentificaClassi(ip).finale,'\n')
    domanda = input('Vuoi fare subnetting o messa in and o supernetting?(1 o 2 o 3): ')
    try:
        if domanda[0] == '1':
            subnetmask = input('Inserisci Subnet mask(255.255.255.0): ')
            print(Subnetting(ip,subnetmask).finale,'\n')
        elif domanda[0] == '2':
            ip1= input('Inserisci un secondo indirizzo Ip(192.168.1.2): ')
            subnetmask = input('Inserisci Subnet mask(255.255.255.0): ')
            print('La Messa in And è andata a buon fine? ',Bitwise(ip,ip1,subnetmask).ritorno,'\n')
        elif domanda[0] == '3':
            try:
                n_host = int(input('inserisci numero host:(500): '))
            except ValueError:
                n_host = int(input('inserisci numero host:(500): '))
            print(Cidr(ip,n_host).finale,'\n')
        if input('Vuoi uscire? (S/N): ')[0] == 'S':
            uscita = True
    except IndexError:
        pass
